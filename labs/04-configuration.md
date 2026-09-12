# Lab 04 — Separate environments and handle secrets

**Time:** 45–60 minutes

[Course home](../README.md) · [Previous lab](03-testing.md) · [Next lab](05-dependencies.md)

Use the same code with intentional configuration. Prerequisite: Lab 03.
Dev is a workbench, test is for repeatable checks, staging rehearses deployment, and
production serves real users. Separate processes and labels in this lab simulate that
separation; real environments also need separate credentials, data and infrastructure.

## Procedure

In terminal A:

```bash
APP_ENV=staging APP_VERSION=practice-a python3 -m guardrails.app --port 8001
```

In terminal B:

```bash
python3 scripts/smoke.py --url http://127.0.0.1:8001 --version practice-a --environment staging
```

Expect a pass. Stop terminal A with Ctrl+C. Then try:

```bash
APP_ENV=production python3 -m guardrails.app
```

Expect startup rejection: only `prod` is an accepted label. Try `ROLLOUT_PERCENT=101`
the same way; expect rejection. A misspelled setting must not silently change behavior.
Recover with the valid staging command.

## Secret drill with fake material only

The reference app needs no secrets. Create a local `.env` file containing
`DEMO_TOKEN=not-a-real-credential`, then run:

```bash
git check-ignore .env
git status --short
```

Expect `.env` to be ignored. This does not protect a secret already committed to
history, copied into an image, logged or pasted into an AI conversation. Do not use
`git add -f` to bypass it. Delete this fake `.env` in your editor when finished.

For a future service, keep actual credentials in a managed secret store; inject them
only into the service that needs them. Give staging a different credential from production.
If a credential leaks, revoke/rotate it first and assess exposure; deleting one line
from the latest commit is not sufficient recovery.

## Completion evidence

Record the valid staging response, invalid-startup message and ignore result without
real credentials. Explain why `APP_ENV=prod` does not create a secure production environment.
Stop the app before the next lab.

[Course home](../README.md) · [Previous lab](03-testing.md) · [Next lab](05-dependencies.md)
