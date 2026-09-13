# Python 04 — Call a local REST API and retrieve every page

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

An API is an agreed way for programs to request data or an action. REST-style APIs often use URLs, HTTP methods and JSON. HTTP 200 means a successful response; 400 means the request was invalid; 401 means credentials were not accepted; 503 means the service cannot currently fulfill the request.

## Hands-on lab

In terminal A, from the course root, create the database if needed and start the app:

```bash
python3 -m ops_data.seed
python3 -m guardrails.app
```

If seed reports an existing database, keep it. In terminal B, enter the SAME course folder before running:

```bash
.venv/bin/python -m ops_data.client
.venv/bin/python -m ops_data.client --customer C01 --output evidence/c01-missions.json
```

Read the client. It sets connect/read timeouts, checks status and JSON shape, follows numeric page offsets and refuses unbounded pagination.

## Deliberately broken example

Review python-track/broken_client.txt. It fetches only the first page, disables TLS verification and hides exceptions behind an empty list. Name the specific incorrect operational conclusion each defect could cause.

## Your task

Write a small client for /api/ops-summary using requests. Include timeout, raise_for_status and a field check. Stop the server briefly and observe a failure; restart and retry.

## Verify and keep evidence

Full client returns eight missions; C01 returns four. Each API page has at most three. Summary: 8 missions, 3 planned, 135 flight minutes, synthetic=true.

## What AI may get wrong

Ignoring pagination, not specifying timeouts, trusting response JSON shape, and treating any response as success.

## Where this appears in deployment work

Customer integrations need explicit contracts for failures, pagination, retries and incomplete data. A timeout is not proof no action occurred.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
