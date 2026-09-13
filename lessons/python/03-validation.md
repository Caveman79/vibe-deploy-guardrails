# Python 03 — Debug and automate a transformation

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

An exception is a reported failure. Catch known errors at the command boundary; preserve a nonzero exit so another process can detect failure. Logging records what happened without publishing raw data or credentials.

## Hands-on lab

Make a copy of the CSV under evidence/. Remove the minutes header, then run the analyzer with --csv pointing to that copy and --output evidence/bad-run. Expect a clear failure and no new valid report. Restore the header and rerun. Compare report output from two valid runs.

## Deliberately broken example

Change the analyzer to catch every exception and write an empty report. Explain why downstream users could mistake failure for zero activity. Keep this proposed fault on a practice branch and restore it before proceeding.

## Your task

Write an automation that runs the analyzer, checks its exit status, and only presents the report if it succeeded. State whether existing output is old or new; never use an old report as evidence of a failed run.

## Verify and keep evidence

Two valid runs yield identical summary data. Malformed headers fail. Logs contain counts and event names, not complete source rows. Keep failure text and the corrected run in evidence.

## What AI may get wrong

Swallowing failures, logging everything, and writing a success-shaped empty file after an error.

## Where this appears in deployment work

Reliable integration work depends on distinguishing no records from failure to retrieve or parse records.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
