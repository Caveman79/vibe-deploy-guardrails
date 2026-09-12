"""Small read-only HTTP app. Training use on a local machine only."""
import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
import os
import re
import time
from urllib.parse import parse_qs, urlsplit
import uuid

LOG = logging.getLogger("guardrails")
CHECKS = ("review", "tests", "rollback")


@dataclass(frozen=True)
class Config:
    environment: str = "dev"
    version: str = "local"
    rollout_percent: int = 0

    @classmethod
    def from_env(cls, env=None):
        env = os.environ if env is None else env
        environment = env.get("APP_ENV", "dev")
        if environment not in {"dev", "test", "staging", "prod"}:
            raise ValueError("APP_ENV must be dev, test, staging, or prod")
        version = env.get("APP_VERSION", "local")
        if not re.fullmatch(r"[A-Za-z0-9._-]{1,64}", version):
            raise ValueError("APP_VERSION must be 1-64 letters, digits, dots, underscores or hyphens")
        raw = env.get("ROLLOUT_PERCENT", "0")
        if not re.fullmatch(r"[0-9]{1,3}", raw) or not 0 <= int(raw) <= 100:
            raise ValueError("ROLLOUT_PERCENT must be an integer from 0 to 100")
        return cls(environment, version, int(raw))


def is_ready(checks):
    """Release requires all three explicit boolean checks, with no missing evidence."""
    return all(checks.get(name) is True for name in CHECKS)


def in_cohort(cohort, percent):
    """Stable bucket across restarts; demonstration flag, never authorization."""
    bucket = int.from_bytes(hashlib.sha256(cohort.encode()).digest()[:4], "big") % 100
    return bucket < percent


PAGE = b"""<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Release Readiness | Vibe Deploy Guardrails</title>
<style>body{font:18px/1.6 system-ui;max-width:740px;margin:64px auto;padding:0 24px;color:#183047;background:#f5f8fa}h1{line-height:1.15}a{color:#005ea8}li{margin:12px 0}small{color:#485e70}</style>
<small>VIBE DEPLOY GUARDRAILS / LOCAL TRAINING APP</small>
<h1>Good deployment is controlled change.</h1>
<p>Before release: independent review, functional checks, and a known-good recovery plan.</p>
<ul><li><a href="/healthz">Check service health</a></li>
<li><a href="/api/readiness?review=true&amp;tests=true&amp;rollback=true">All evidence present</a></li>
<li><a href="/api/readiness?review=true&amp;tests=false&amp;rollback=true">Functional check failed</a></li>
<li><a href="/api/readiness?cohort=training-team">Missing evidence</a></li></ul>
<p>This app reports supplied evidence. It does not verify approvals or authorize a real release.</p>
</html>"""


def handler_for(config):
    class Handler(BaseHTTPRequestHandler):
        server_version = "Guardrails"
        sys_version = ""

        def setup(self):
            super().setup()
            self.connection.settimeout(5)

        def log_message(self, format, *args):
            # Never log raw URLs, headers, request bodies or client identifiers.
            pass

        def do_GET(self):
            started = time.monotonic()
            request_id = uuid.uuid4().hex
            route = "unknown"
            status = 200
            body = {}
            content_type = "application/json"
            try:
                url = urlsplit(self.path)
                route = url.path if url.path in {"/", "/healthz", "/api/readiness"} else "unknown"
                if route == "/":
                    body = PAGE
                    content_type = "text/html; charset=utf-8"
                elif route == "/healthz":
                    body = {"status": "ok", "environment": config.environment, "version": config.version}
                elif route == "/api/readiness":
                    if len(url.query) > 1024:
                        raise ValueError("query too long")
                    query = parse_qs(url.query, keep_blank_values=True, max_num_fields=4)
                    if set(query) - {*CHECKS, "cohort"} or any(len(v) != 1 for v in query.values()):
                        raise ValueError("unknown or repeated field")
                    checks = {}
                    for name in CHECKS:
                        value = query.get(name, ["false"])[0]
                        if value not in {"true", "false"}:
                            raise ValueError("checks must be true or false")
                        checks[name] = value == "true"
                    cohort = query.get("cohort", ["training-team"])[0]
                    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,40}", cohort):
                        raise ValueError("invalid cohort")
                    body = {"ready": is_ready(checks), "checks": checks, "version": config.version}
                    if in_cohort(cohort, config.rollout_percent):
                        body["guidance"] = "Confirm independent review and rehearse recovery before release."
                else:
                    status, body = 404, {"error": "not found"}
            except ValueError:
                status, body = 400, {"error": "invalid request"}
            payload = body if isinstance(body, bytes) else json.dumps(body).encode()
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; frame-ancestors 'none'")
            self.send_header("X-Request-ID", request_id)
            self.end_headers()
            self.wfile.write(payload)
            LOG.info(json.dumps({"timestamp": datetime.now(timezone.utc).isoformat(),
                "event": "request", "request_id": request_id, "route": route,
                "status": status, "duration_ms": round((time.monotonic()-started)*1000, 2),
                "environment": config.environment, "version": config.version}))
    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["127.0.0.1", "0.0.0.0"], default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    try:
        config = Config.from_env()
        if not 1 <= args.port <= 65535:
            raise ValueError("port must be 1-65535")
    except ValueError as error:
        parser.error(str(error))
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    with ThreadingHTTPServer((args.host, args.port), handler_for(config)) as server:
        LOG.info(json.dumps({"event": "startup", "environment": config.environment, "version": config.version}))
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
