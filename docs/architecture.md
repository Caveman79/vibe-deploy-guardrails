# What the reference app does

The app is deliberately small enough to read. `guardrails/app.py` contains a validated
configuration object, a release-rule function, a deterministic cohort function, and
an HTTP request handler. `python3 -m guardrails.app` starts it.

| Request | Result |
| --- | --- |
| `GET /` | Browser landing page with sample links |
| `GET /healthz` | Process response, environment label, version label |
| `GET /api/readiness` | `ready: false`; missing checks default to false |
| `GET /api/readiness?review=true&tests=true&rollback=true` | `ready: true` |
| Unknown path | HTTP 404 |
| Unknown, repeated, oversized or invalid readiness field | HTTP 400 |

The three checks must be explicit booleans in Python, or the exact strings `true` and
`false` in the HTTP query. A successful HTTP response does not necessarily mean a
release is ready: HTTP 200 with `ready: false` is an expected hold decision.

`APP_ENV` accepts `dev`, `test`, `staging`, or `prod`; `APP_VERSION` is a printable release
label with restricted characters; `ROLLOUT_PERCENT` accepts integers from 0 to 100.
Invalid configuration prevents startup. The environment label alone creates no isolation.

A percentage rollout adds advisory `guidance` to a stable cohort's response. It cannot
change the release rule. Cohorts are demonstration identifiers, not authenticated users.
Anyone can choose one, so this must never gate access or privileges.

Logs contain time, event, a generated request ID, recognized route, HTTP status,
duration, version and environment. Raw queries, headers, client identifiers and unknown
path strings are excluded. There is no persistence, login, external service, secret
requirement, command execution or write endpoint. The server does not serve arbitrary files.

## Boundaries

Python's standard HTTP server makes the code easy to inspect but is not suitable for
public production serving. The app has no TLS, access control, durable storage,
centralized metrics or sophisticated resource-abuse protection. See the
[Python documentation](https://docs.python.org/3/library/http.server.html).

The `prod` environment in these labs is a **local simulation**. Use synthetic data only.
Do not expose it through a public tunnel or bind its Docker host port to every interface.
For a real service, choose a maintained production server/platform, authentication,
network controls, monitoring and an operational owner; repeat the tests after changes.
