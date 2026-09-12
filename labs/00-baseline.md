# Lab 00 — Establish a baseline

**Time:** 25–40 minutes

[Course home](../README.md) · [Next lab](01-git.md)

Your mission is to distinguish “a program started” from “the required behavior works.”
A baseline is the configuration and behavior you can reproduce before making changes.
Prerequisite: [setup](../docs/setup.md).

## Procedure

1. From the repository root, run `python3 -m unittest discover -s tests -v`.
   Expect 10 passing tests in the starting reference version.
2. Run `python3 -m guardrails.app`. Leave this terminal open.
3. Open `http://127.0.0.1:8000/healthz`. Expect status `ok`, environment `dev`, version `local`.
4. Follow the home-page links for all checks passing and one check failing.
5. In a second terminal in the same folder, run `python3 scripts/smoke.py`.
6. Create your private practice evidence folder: `mkdir -p evidence`.
   Write `evidence/00-baseline.md` with the Python version and the observed results.

## Introduce a fault

In the second terminal, run:

```bash
python3 scripts/smoke.py --version wrong-version
```

Expect a nonzero exit and a health/config mismatch. The app is responding, but it is
not the release you asked to verify. Repeat the original smoke command to recover.
Stop the app using Ctrl+C when finished.

## Debrief and completion evidence

Record why a green health response alone is insufficient. Pass when you can produce a
successful functional check and explain why the wrong-version check failed without
changing the test to hide the discrepancy.

[Course home](../README.md) · [Next lab](01-git.md)
