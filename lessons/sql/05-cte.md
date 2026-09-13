# SQL 05 — Break a complex question into inspectable steps

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

A common table expression (CTE), introduced by WITH, names an intermediate result for this query. A subquery asks a question inside another query. Neither automatically saves a permanent table.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/05-cte.sql
```

First run just the totals calculation yourself. Then restore the full query. It compares each customer total with the average of customer totals, not the average flight duration.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
WITH totals AS (SELECT m.customer_id, SUM(f.minutes) AS total_minutes FROM missions m JOIN flight_logs f ON f.mission_id=m.mission_id GROUP BY m.customer_id) SELECT customer_id,total_minutes FROM totals WHERE total_minutes > (SELECT AVG(total_minutes) FROM totals);
```

## Deliberately broken example

Replace AVG(total_minutes) with SELECT AVG(minutes) FROM flight_logs. It is valid SQL but compares unlike units of analysis: customer totals versus individual flights.

## Your task

Use a CTE to list completed missions with their flight duration, then find those longer than the mean flight duration. Explain the intermediate row grain and the final threshold.

## Verify and keep evidence

Reference above-customer-average result: C01 = 75 (average customer total 67.5). Longer-than-average flights: F02 = 45 and F04 = 40; mean flight duration 33.75.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Confusing a mean of totals with a mean of individual records, or adding nested logic without inspecting intermediate rows.

## Where this appears in deployment work

A small, explainable transformation is easier to validate with a customer than a large opaque query.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](06-dates-case.md)
