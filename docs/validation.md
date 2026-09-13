# Validation status

## v0.3 operator bridge

Local checks on 2026-09-13: 16 standard-library tests and 4 optional data-tool tests pass on Python 3.14.4; all local Markdown links resolve. Verified all nine reference SQL queries, 8-mission pagination, 4 accepted / 5 quarantined intake rows and 135 accepted minutes. Browser navigation from home to SQL lesson 1 displays explanations and labeled command boxes.

Hosted Python 3.12, container and security checks are required before merging this update; consult the pull request checks for the current result. The local environment has no Docker runtime. Branch protection is not enabled, and an independent human review and complete release/rollback rehearsal have not been performed for this update. The course includes those exercises; supplying an exercise is not evidence that a learner completed it.

## Previous release evidence

# Validation record — 2026-09-12

The course is published at [Caveman79/vibe-deploy-guardrails](https://github.com/Caveman79/vibe-deploy-guardrails).
All 46 initial files were compared byte-for-byte against a fresh GitHub clone.

## Verified checks

- 10 Python unit and real-loopback HTTP integration tests passed locally on Python 3.14.
- Actual app startup, smoke commands, wrong-version rejection, invalid configuration
  rejection, and 0/100-percent feature rollout were exercised locally.
- The deliberate Lab 03 `all` → `any` fault was caught in an isolated copy.
- Python, YAML and shell syntax and local Markdown links passed.
- Hosted Python tests, documentation links, Docker build, functional smoke check and
  non-root execution check passed in [CI](https://github.com/Caveman79/vibe-deploy-guardrails/actions/runs/34714355035).
- Source secret/configuration scanning and image dependency scanning passed the
  HIGH/CRITICAL gate in [Security](https://github.com/Caveman79/vibe-deploy-guardrails/actions/runs/34714355095).

Those hosted runs checked revision `86c31a67a7eb6f12b33e0187447121d159cea7b6`, merged
through [PR 4](https://github.com/Caveman79/vibe-deploy-guardrails/pull/4). A passing
scan means no findings at the configured threshold in that run, not proof of no vulnerabilities.

## Findings fixed during publication

The initial Debian slim image scan reported 53 HIGH and 3 CRITICAL findings. The
runtime now uses the official Python Alpine base with the patched `libuuid` package.
No scan suppressions or relaxed severity gates were added. Hosted testing also exposed
a logging-test race; it now waits for the matching request event before inspecting logs.
The PR records the changes and compatibility tradeoff. No independent human approval
is claimed for this AI-assisted preparation.

## Still to configure or rehearse

- Branch protection and environment approval rules: instructions supplied; not configured.
- Manual Release rehearsal workflow: not run as an independently approved release.
- Full promotion/rollback classroom procedure: not exercised end to end in the preparation
  environment, which lacks Docker; the automated container smoke check did run on GitHub.
- Public app hosting: intentionally not configured. The Python server is for local training.

Retain these distinctions when assessing the capstone. Future dependency/database changes
can change scan results; inspect the current run before making a release decision.
