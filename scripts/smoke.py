"""Functional check: reject a wrong release even if its process is healthy."""
import argparse
import json
from urllib.request import urlopen


def check(base, version, environment):
    with urlopen(base + "/healthz", timeout=5) as response:
        health = json.load(response)
    if health != {"status": "ok", "version": version, "environment": environment}:
        raise RuntimeError(f"health/config mismatch: {health}")
    for query, expected in (("review=true&tests=true&rollback=true", True),
                            ("review=true&tests=false&rollback=true", False)):
        with urlopen(base + "/api/readiness?" + query, timeout=5) as response:
            result = json.load(response)
        if result.get("ready") is not expected or result.get("version") != version:
            raise RuntimeError("functional check failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:8000")
    parser.add_argument("--version", default="local")
    parser.add_argument("--environment", default="dev")
    args = parser.parse_args()
    check(args.url.rstrip("/"), args.version, args.environment)
    print("PASS: identity, health, approval and hold behavior")
