# Lab 03 — Make the functional check fail for the right reason

**Time:** 40–60 minutes

[Course home](../README.md) · [Previous lab](02-review.md) · [Next lab](04-configuration.md)

A useful test distinguishes acceptable behavior from a plausible mistake.
Prerequisite: Lab 02; work from a clean `main` on `practice/test-fault`.

## Procedure

```bash
git switch -c practice/test-fault
python3 -m unittest discover -s tests -v
```

Read `is_ready` in `guardrails/app.py` and the tests in `tests/test_app.py`.
The unit tests cover all eight combinations of three boolean checks. HTTP integration
tests exercise request parsing and real responses. `scripts/smoke.py` checks a running
service, including its version and environment. There is no browser automation suite;
the manual link exercise is the browser check.

## Inject a fault

In `is_ready`, change only `all(...)` to `any(...)`. Save and rerun the tests.
Expect failures for mixed true/false checks: the program now approves incomplete evidence.
Do not change the expected answers to make the suite green.

Restore the edited function in your editor to `all(...)`, then rerun the tests. Expect green.
Use `git diff` to ensure the fault is gone.

## Extend your understanding

Predict the answer for `{"review": "false", "tests": True, "rollback": True}`.
The string `"false"` is truthy in Python, but the rule uses `is True`, so approval is false.
This demonstrates why input meaning matters more than “not empty.”

## Completion evidence

Save the name and explanation of a failing test and the restored passing result.
Pass when you can explain why one test checks the rule and another checks the HTTP
boundary. A passing suite supports the covered requirements; it does not prove that
no security or operational defects exist. Return to `main` after restoring the file.

[Course home](../README.md) · [Previous lab](02-review.md) · [Next lab](04-configuration.md)
