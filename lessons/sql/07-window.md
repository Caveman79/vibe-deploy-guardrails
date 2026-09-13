# SQL 07 — Compare trends without losing individual records

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

Window functions compute across related rows while retaining each row. PARTITION BY separates customers; ORDER BY defines sequence. A running SUM is different from GROUP BY because the flight records remain visible.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/07-window.sql
```

Read each output row. C01’s running totals are 30 then 75; C02’s are 20 then 60. ROW_NUMBER ranks the newest flight within each customer. A secondary ID sort makes ties deterministic.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT m.customer_id, f.flight_id, f.minutes, SUM(f.minutes) OVER(PARTITION BY m.customer_id ORDER BY f.landed_at, f.flight_id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_minutes, ROW_NUMBER() OVER(PARTITION BY m.customer_id ORDER BY f.landed_at DESC, f.flight_id DESC) AS newest_rank FROM flight_logs f JOIN missions m ON m.mission_id=f.mission_id ORDER BY m.customer_id,f.landed_at,f.flight_id;
```

## Deliberately broken example

Remove PARTITION BY. Customers now share one running total. Remove ORDER BY from the SUM window: the value becomes the entire partition total rather than the running total.

## Your task

Use a CTE around ROW_NUMBER and return only the most recent flight for each customer. Explain why filtering the window alias belongs in the outer query. Add a LAG(minutes) window to compare each flight with the previous flight for that customer.

## Verify and keep evidence

Latest flights: C01/F02 and C02/F04. LAG for each first flight is NULL. Four records remain in the reference output.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Forgetting partitions, unstable tie ordering, and assuming every database uses identical window-frame defaults.

## Where this appears in deployment work

You may need latest customer configuration, trend analysis or incident sequencing without throwing away detailed records.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](08-quality.md)
