# SQL 09 — Build an operational exception report

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

Combine the SQL skills into one advisory report. This is a fictional training rule, not flight authorization: planned missions need an available aircraft, a qualification valid on the mission date, and an approved risk record.

## Hands-on lab

Begin without the solution. Inspect the relevant tables and write your own query in evidence/mission-holds.sql. Run it with ops_data.query. When ready, compare:

```bash
python3 -m ops_data.query sql/solutions/09-mission-holds.sql
```

The reference returns separate hold indicators instead of hiding reasons behind one yes/no field. This lets an operator assign corrective action.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT m.mission_id, CASE WHEN a.status != 'available' THEN 1 ELSE 0 END AS aircraft_hold, CASE WHEN q.expires_on IS NULL OR date(q.expires_on)<date(m.planned_at) THEN 1 ELSE 0 END AS qualification_hold, CASE WHEN r.decision IS NULL OR r.decision!='approved' THEN 1 ELSE 0 END AS approval_hold FROM missions m JOIN aircraft a ON a.aircraft_id=m.aircraft_id LEFT JOIN qualifications q ON q.operator_id=m.operator_id AND q.qualification='mission_operator' LEFT JOIN risk_approvals r ON r.mission_id=m.mission_id WHERE m.status='planned' ORDER BY m.mission_id;
```

## Deliberately broken example

Use INNER JOIN for risk_approvals. M06 disappears because its missing approval has no row. The absence is exactly the discrepancy the report should reveal.

## Your task

Produce a customer-specific report for C01. Include reasons and an assessment timestamp in your written evidence. Brief the difference between database evidence and verified operational reality in under two minutes.

## Verify and keep evidence

M05 holds for aircraft, qualification and approval. M06 holds for qualification and approval. M07 has no holds under this limited fictional rule. C01 report contains M05 and M07.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Calling “no hold found” safe-to-fly, treating a filter as access control, or inventing requirements beyond the supplied rule.

## Where this appears in deployment work

Deployment strategists translate workflow requirements into testable rules while making the limits of those rules explicit.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Continue to Python](../python/01-files.md)
