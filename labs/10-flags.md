# Lab 10 — Introduce an optional feature gradually

**Time:** 40–60 minutes

[Course home](../README.md) · [Previous lab](09-release-rollback.md) · [Next lab](11-capstone.md)

A feature flag changes behavior without changing the packaged code. It does not replace
review or access control. Prerequisite: Lab 09 (the exercise itself uses local Python).

## Procedure

Start with:

```bash
ROLLOUT_PERCENT=0 python3 -m guardrails.app
```

Open `/api/readiness?cohort=alpha`. There should be no `guidance` field.
Stop the app and repeat with `ROLLOUT_PERCENT=10`, then 50, then 100. Use the same
cohort each time. At 100 every valid cohort has guidance; at 0 none does.
At an intermediate percentage, try `alpha`, `bravo`, and `charlie`. The same cohort
stays in the same bucket across restarts. A sample of three need not match the configured
percentage: the percentage applies to hash buckets, not a guarantee for a tiny population.

Repeat the all-checks-passing and one-check-failing requests at 0 and 100. Readiness
must remain correct regardless of the flag. Record results before expansion.

## Kill-switch drill

Suppose the guidance is confusing users. Stop the app and restart with
`ROLLOUT_PERCENT=0`. Verify the guidance disappears and readiness still works.
This app reads configuration only at startup: changing a shell variable does not update
an already running process. Real flag services may support live updates with different
failure modes and audit requirements.

## Completion evidence

Record cohort, percentage, result, observation window, expansion approver and kill-switch
result. Assign a retirement date/owner to the flag in your release record. Explain why
client-chosen cohorts cannot be used for authentication, licensing, or privileged access.
Stop the app when finished.

[Course home](../README.md) · [Previous lab](09-release-rollback.md) · [Next lab](11-capstone.md)
