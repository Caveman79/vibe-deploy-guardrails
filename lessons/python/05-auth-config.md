# Python 05 — Separate identity, access and customer settings

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

Authentication asks who or what is calling. Authorization asks what it may do. A customer filter is neither. Environment variables configure a process; secret values must not be committed. A real system needs scoped identity and permissions beyond this local bearer-token demonstration.

## Hands-on lab

The optional /api/customer-config endpoint requires DEMO_API_TOKEN (at least 16 characters). Start it locally in Bash with a freshly generated synthetic token:

In the first terminal, stop the server with Ctrl+C. Create a private file once, without printing the token:

```bash
python3 -c 'import os,secrets; fd=os.open(".env.demo",os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600); os.write(fd,("export DEMO_API_TOKEN="+secrets.token_urlsafe(24)+"\n").encode()); os.close(fd)'
source .env.demo
python3 -m guardrails.app
```

If the file already exists, keep it and use `source .env.demo`. In the second terminal, in the same course folder and with the Phase 2 virtual environment active:

```bash
source .env.demo
python -m ops_data.config_client
```

Expected: customer C01, max_wind_kts 20. The ignored `.env.demo` file is local training storage, not a production secrets manager. Do not print or share it.

## Deliberately broken example

With no configured server token expect 503; with no/wrong client token expect 401; with a correct token and C01 expect max_wind_kts=20. The token grants the whole demo endpoint, not per-customer isolation. It must not be deployed publicly.

## Your task

Compare C01 and C02 configuration: 20 versus 15 knots. Write a config validator for fixtures/customer-config.json that rejects wrong customer, unknown environment and nonpositive limits. Explain why a client-side filter cannot enforce customer isolation.

## Verify and keep evidence

Keep only statuses and sanitized config results, not tokens. Close the exercise with unset DEMO_API_TOKEN in each terminal and restart without it. Delete only the training file with `rm .env.demo` when finished. Explain authentication versus authorization unaided.

## What AI may get wrong

Hard-coding tokens, placing them in URL query strings, leaking headers, or assuming authentication automatically scopes access.

## Where this appears in deployment work

Customer-specific configuration errors can cause a technically healthy deployment to behave incorrectly. Confirm identity, scope and expected configuration independently.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
