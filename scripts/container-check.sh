#!/usr/bin/env bash
set -euo pipefail
image=${1:?Usage: bash scripts/container-check.sh IMAGE}
name="vdg-check-${RANDOM}-$$"
cleanup() { docker rm -f "$name" >/dev/null 2>&1 || true; }
trap cleanup EXIT
# Docker chooses an unused host port, bound only to this machine.
docker run -d --name "$name" --read-only --cap-drop=ALL --security-opt=no-new-privileges \
  --memory=128m --cpus=1 --pids-limit=64 -p 127.0.0.1::8000 \
  -e APP_ENV=staging -e APP_VERSION=container-test "$image" >/dev/null
port=$(docker port "$name" 8000/tcp | awk -F: '{print $NF}')
for attempt in $(seq 1 20); do
  if python3 scripts/smoke.py --url "http://127.0.0.1:$port" --version container-test --environment staging; then
    test "$(docker exec "$name" id -u)" != 0
    exit 0
  fi
  sleep 1
done
docker logs "$name"
exit 1
