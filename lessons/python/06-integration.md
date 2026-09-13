# Python 06 — Build a repeatable customer handover report

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

Bring the data flow together: API → validated records → Python transformation → report → operator interpretation. The goal is a repeatable handover with known assumptions, not a perfect-looking chart.

## Hands-on lab

Start the app and fetch a complete C01 mission export. Run the intake analyzer. Create evidence/handover.py that combines the customer mission count and accepted flight-minute total into evidence/handover.json, including a UTC generation timestamp, customer ID and the source file names.

## Deliberately broken example

Mix the C02 flight total into a C01 report. Add an explicit customer-ID check so that mismatch causes failure rather than a misleading handover.

## Your task

Produce a one-page handover explaining four C01 missions and 75 accepted flight minutes, rejected intake rows, and what the report does not establish about operational safety. State how you would handle a schema change, timeout or stale input.

## Verify and keep evidence

Preserve source exports, the script, the report and a successful repeat run. Complete the Week 6 no-AI checkpoint before moving to change-control labs.

## What AI may get wrong

Claiming live/current data from static fixtures, forgetting provenance, and presenting a generated result as verified operational truth.

## Where this appears in deployment work

A useful technical bridge ends with a decision-quality explanation for stakeholders, including uncertainty and next actions.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
