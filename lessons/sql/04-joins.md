# SQL 04 — Keep the people whose records are missing

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

A JOIN matches related records by identity. An INNER JOIN keeps matches only; a LEFT JOIN retains every row from the left table and fills missing right-side fields with NULL. NULL means unknown or absent, not zero or false.

## Hands-on lab

Run:

```bash
python3 -m ops_data.query sql/solutions/04-joins.sql
python3 -m ops_data.query sql/broken/04-null.sql
```

The reference lists all four operators. Morgan Lake has no qualification record. The broken query uses = NULL; comparisons with NULL do not evaluate to true. Use IS NULL or IS NOT NULL.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT o.operator_id, o.name, q.expires_on FROM operators o LEFT JOIN qualifications q ON o.operator_id=q.operator_id AND q.qualification='mission_operator' ORDER BY o.operator_id;
```

## Deliberately broken example

Change the reference LEFT JOIN to JOIN and observe O04 disappear. Then put the qualification-name condition in WHERE instead of ON; explain how that can remove the missing-record row again.

## Your task

Write evidence/missing-qualification.sql using a left join and IS NULL. Explain why the table on the left matters. Add the name from operators without joining on names.

## Verify and keep evidence

Exactly O04 / Morgan Lake is missing a mission_operator qualification. An expired qualification is present but not current; that is a different question.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Dropping the very exceptions the customer needs to see, or joining on a non-unique human-readable name.

## Where this appears in deployment work

Implementation work often requires finding missing records, not merely displaying the records that already match.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](05-cte.md)
