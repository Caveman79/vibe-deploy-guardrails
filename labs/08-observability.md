# Lab 08 — Use operating evidence to investigate a fault

**Time:** 40–60 minutes

[Course home](../README.md) · [Previous lab](07-ci.md) · [Next lab](09-release-rollback.md)

Logs explain events; metrics summarize rates and timing; traces connect work across
services. This small app implements structured request logs only.
Prerequisite: Lab 07 (or local app access for the logging portion).

## Procedure

Run the app in one terminal and open these paths in the browser:

- `/healthz`: expect HTTP 200.
- `/api/readiness?review=yes`: expect HTTP 400 with `invalid request`.
- `/missing`: expect HTTP 404.

Each handled GET produces one JSON log line. Compare `status`, `route`, `duration_ms`,
`environment`, `version`, and `request_id`. Browser developer tools show the matching
`X-Request-ID` response header. An unknown path is logged as `unknown`, protecting its content.

Repeat a valid readiness request with `tests=false`. Expect HTTP 200 and `ready:false`.
That is an operational hold, not a server crash. A useful monitor must understand both
HTTP status and business behavior.

## Fault isolation drill

Ask a partner to choose either a bad query or a wrong version for a smoke check.
Identify which evidence distinguishes invalid input from wrong deployed configuration.
Do not log all query parameters to make diagnosis easier; a real query may contain secrets.
Recover by correcting the request/configuration, then repeat the same check.

## Define stop criteria

For this training rehearsal, use: any wrong approval/hold answer, unexpected version,
or failed smoke check means **stop immediately**. Observe at least 20 representative
requests over 2 minutes before expanding a feature. Record 400s you intentionally caused
separately from unexpected errors. This is a classroom criterion, not a universal
production service-level objective.

## Completion evidence

Keep three sanitized event examples and explain which one represents a release blocker.
For real operation, propose an owner, central log retention/access, error-rate and latency
metrics, and a paging threshold. A terminal scrolling by is not a monitoring service.
Stop the app after the drill.

[Course home](../README.md) · [Previous lab](07-ci.md) · [Next lab](09-release-rollback.md)
