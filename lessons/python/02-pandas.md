# Python 02 — Reconcile a pandas report to SQL

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

A DataFrame is a table in memory. pandas is useful for joins, grouping and export; it does not guarantee that source data is correct. Validate the relationship in a merge to detect duplicate lookup keys.

## Hands-on lab

Read ops_data/analyze.py, then run:

```bash
.venv/bin/python -m ops_data.analyze
```

Open evidence/intake/report.json and quarantine.csv in your editor. The report groups accepted minutes by customer. The quarantine preserves original defective rows and explicit reasons.

## Deliberately broken example

Run python-track/broken_report.py with .venv/bin/python. It prints 200 minutes by coercing bad values, retaining a duplicate and accepting an unknown mission. The program finishing successfully does not validate its result.

## Your task

Create a second report grouped by mission. Use merge(validate="many_to_one"). Add a duplicate M01 to a COPY of the mission lookup and confirm validation rejects it.

## Verify and keep evidence

Accepted 4, rejected 5, total 135; C01 75, C02 60. Totals must reconcile with SQL 03. A conflicting duplicate flight identity must be quarantined rather than arbitrarily keeping a row.

## What AI may get wrong

Blind drop_duplicates, silent fillna(0), mismatched units and multiplying rows during merge.

## Where this appears in deployment work

A deployment engineer or strategist may need to reconcile a dashboard against source-system exports before a customer trusts it.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
