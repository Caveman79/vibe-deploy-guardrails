# SQL 06 — Make qualification decisions repeatable

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

CASE expresses an explicit decision rule. SQLite stores these exercise dates as ISO text. date() extracts the date; julianday() supports day differences. This scenario uses UTC and a fixed assessment date: 2026-09-15.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/06-dates-case.sql
python3 -m ops_data.query sql/broken/06-time.sql
```

The reference treats a qualification as current through its expiry date. That convention is a fictional customer requirement, not a regulatory statement. The broken query changes with the real calendar.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT o.operator_id, CASE WHEN q.expires_on IS NULL THEN 'missing' WHEN date(q.expires_on) < date('2026-09-15') THEN 'expired' ELSE 'current' END AS qualification_state, CAST(julianday(q.expires_on)-julianday('2026-09-15') AS INTEGER) AS days_remaining FROM operators o LEFT JOIN qualifications q ON o.operator_id=q.operator_id AND q.qualification='mission_operator' ORDER BY o.operator_id;
```

## Deliberately broken example

Use <= instead of < for expiry. Explain how someone expiring on the assessment date changes classification. Insert no data into the authoritative database; demonstrate the boundary with SELECT date(...) expressions.

## Your task

Write a CASE expression classifying missions before 2026-09-15 as historical and others as upcoming. Then calculate qualification status at each mission’s planned time, not at the computer’s current time.

## Verify and keep evidence

O01 current, O02 expired, O03 current, O04 missing. O02 has -15 days remaining; O04 has NULL, not zero.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Timezone assumptions, text dates in mixed formats, hidden use of now, and missing boundary tests.

## Where this appears in deployment work

Customer acceptance rules depend on exactly when a qualification or approval must be valid. Ask and document the rule.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](07-window.md)
