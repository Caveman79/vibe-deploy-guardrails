# Lab 06 — Package a release with limited privileges

**Time:** 45–60 minutes

[Course home](../README.md) · [Previous lab](05-dependencies.md) · [Next lab](07-ci.md)

An image is a packaged filesystem/runtime; a container is a running instance.
Prerequisite: Lab 05 and a working Docker installation. Return to this lab before
running Lab 05's scan if you deferred Docker setup.

## Procedure

```bash
docker build -t guardrails:practice .
bash scripts/container-check.sh guardrails:practice
```

The script chooses a temporary local port, checks expected behavior, verifies a non-root
user and removes its own container on exit. Expect the smoke PASS message and exit 0.
For inspection, launch a named instance:

```bash
docker run -d --name vdg-inspect --read-only --cap-drop=ALL --security-opt=no-new-privileges --memory=128m --cpus=1 --pids-limit=64 -p 127.0.0.1:8002:8000 guardrails:practice
docker exec vdg-inspect id
docker image inspect guardrails:practice --format '{{.Id}}'
```

Expect UID 10001. Open `http://127.0.0.1:8002`.
The app listens on all interfaces **inside** the container; the published host port is
restricted to loopback. The container cannot access arbitrary host files unless you
mount them, but a container is not a complete security boundary.

## Exercise a denied operation

```bash
docker exec vdg-inspect python -c "open('/app/should-not-exist', 'w').write('demo')"
```

Expect a nonzero exit because the filesystem is read-only. That failure is desired.
Do not “fix” it with root or privileged mode. If a real app needs storage, provide a
specific volume/path and only the permissions required.

## Recovery and evidence

```bash
docker rm -f vdg-inspect
```

This removes only the named disposable training container. Keep the image for later
labs. Record the image ID, UID, smoke result and denied-write result. If the name or
port was already taken, inspect your existing training container rather than deleting
unrelated containers. Read [deployment](../docs/deployment.md) before promoting an image.

[Course home](../README.md) · [Previous lab](05-dependencies.md) · [Next lab](07-ci.md)
