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
import sqlite3
import time
from urllib.parse import parse_qs, urlsplit
import uuid
from guardrails import ui, course
from ops_data import api as data_api
from ops_data.seed import DEFAULT_DB

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


PAGE = ui.home()


def handler_for(config, db_path=DEFAULT_DB):
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
                route = url.path if url.path in {"/", "/course", "/lesson", "/learn", "/check", "/healthz", "/api/readiness", "/api/missions", "/api/ops-summary", "/api/customer-config"} else "unknown"
                if route == "/":
                    body = PAGE
                    content_type = "text/html; charset=utf-8"
                elif route == "/course":
                    body = course.index()
                    content_type = "text/html; charset=utf-8"
                elif route == "/lesson":
                    query = parse_qs(url.query, keep_blank_values=True, max_num_fields=1)
                    if set(query) != {"name"} or len(query["name"]) != 1:
                        raise ValueError("invalid lesson")
                    body = course.lesson(query["name"][0])
                    content_type = "text/html; charset=utf-8"
                elif route in {"/api/missions", "/api/ops-summary", "/api/customer-config"}:
                    status, body = data_api.response(route, url.query, self.headers.get("Authorization", ""), db_path)
                elif route == "/learn":
                    query = parse_qs(url.query, keep_blank_values=True, max_num_fields=1)
                    if set(query) != {"step"} or query["step"] not in [[str(i)] for i in range(1, 6)]:
                        raise ValueError("invalid lesson step")
                    body = ui.lesson(int(query["step"][0]), config, is_ready)
                    content_type = "text/html; charset=utf-8"
                elif route == "/healthz":
                    body = {"status": "ok", "environment": config.environment, "version": config.version}
                elif route in {"/api/readiness", "/check"}:
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
                    if route == "/check":
                        body = ui.check_page(body)
                        content_type = "text/html; charset=utf-8"
                else:
                    status, body = 404, {"error": "not found"}
            except ValueError:
                status, body = 400, {"error": "invalid request"}
            except sqlite3.Error:
                status, body = 503, {"error": "training database unavailable; run python3 -m ops_data.seed in the course folder"}
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
