# SQL 08 — Investigate duplicate and invalid intake records

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

Intake is evidence to inspect, not automatically trusted operational truth. Separate missing fields, duplicate identities, invalid values, bad timestamps and broken references. Record rejection reasons instead of silently “cleaning” them away.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/08-quality.sql
python3 -m ops_data.query sql/broken/08-cast.sql
```

Open the CSV and compare it with flight_intake. SQLite accepts loose types: casting the text ten to an integer yields zero. A cast is not proof of a valid number. Date functions return NULL for an invalid date.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT flight_id, COUNT(*) AS copies FROM flight_intake GROUP BY flight_id HAVING COUNT(*) > 1;
```

## Deliberately broken example

Count intake rows as flights or sum cast durations. The answer includes duplicates and defective records. Explain why COALESCE(minutes,0) hides a missing-duration discrepancy.

## Your task

Write separate queries for duplicate flight IDs; minutes IS NULL; negative numeric minutes; rows with no matching mission; and unparseable landed_at values. Keep each question separate before combining a report. For numeric validation, examine the original text as well as casts.

## Verify and keep evidence

Nine intake rows. F02 appears twice; F05 lacks minutes; F06 is negative; F07 references M99; F08 has nonnumeric minutes and an invalid date. Four accepted flights sum to 135 minutes after explicit validation and duplicate handling.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Automatically dropping all duplicates, discarding rejection evidence, or reporting missing data as zero.

## Where this appears in deployment work

Dirty customer data is common. A useful implementation preserves traceability and separates a data problem from a software fault.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](09-mission-holds.md)
