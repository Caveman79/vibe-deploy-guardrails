# SQL 03 — Count flights without inventing activity

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

GROUP BY collects rows with a shared value. COUNT(*) counts rows, COUNT(column) excludes NULL, and SUM adds numeric values. Always identify the unit: here durations are minutes, not hours.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/03-aggregate.sql
python3 -m ops_data.query sql/broken/03-join-fanout.sql
```

The first query joins each flight to its mission and groups by customer. The second multiplies every flight by every qualification because its join condition is always true. It runs successfully while giving a wrong answer.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT m.customer_id, COUNT(f.flight_id) AS flights, SUM(f.minutes) AS total_minutes FROM missions m JOIN flight_logs f ON f.mission_id=m.mission_id GROUP BY m.customer_id ORDER BY m.customer_id;
```

## Deliberately broken example

The broken query reports 405 minutes. Trace why four flights became twelve joined rows. Compare COUNT(*) before and after the join.

## Your task

Write a query for total flight minutes by aircraft. Then include aircraft that have no flights, using a left join. Show the difference between a NULL sum and a displayed zero; state your reporting convention.

## Verify and keep evidence

Reference customer totals: C01 = 75 minutes, C02 = 60; two flights each. Authoritative total = 135. A01 = 75, A03 = 60, A02 has no flights.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Double-counting after a many-to-many join, or summing the unvalidated intake file.

## Where this appears in deployment work

A plausible dashboard number can still be wrong. Reconcile totals to source records before briefing leadership.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](04-joins.md)
