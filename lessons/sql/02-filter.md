# SQL 02 — Ask a precise operational question

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: the preceding SQL lesson.

## Understand

SELECT chooses columns; WHERE chooses records; ORDER BY makes the order explicit. Filtering is not authorization: a caller may still be able to ask for another customer.

## Hands-on lab

Run the reference query:

```bash
python3 -m ops_data.query sql/solutions/02-filter.sql
```

Read its clauses from FROM to WHERE to SELECT to ORDER BY. It asks for planned Harbor Survey missions, not every mission or every customer. SQL strings use single quotes; exact status values are defined in the schema.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT mission_id, planned_at FROM missions WHERE status='planned' AND customer_id='C01' ORDER BY planned_at;
```

## Deliberately broken example

Change customer_id='C01' to customer_id='C02' AND status='completed' while accidentally retaining status='planned'. Why does the result become empty? Empty does not prove the customer has no records.

## Your task

Create evidence/planned.sql and return all planned missions for both customers, ordered by planned time. Then restrict it to C02. Explain AND versus OR with one concrete record.

## Verify and keep evidence

Both customers: M05, M06, M07. C02 only: M06. The reference query returns M05 and M07.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Using OR where AND is intended, or applying filters after aggregation to different data.

## Where this appears in deployment work

Requirements such as “active missions for this customer” must be translated into exact inclusion rules.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](03-aggregate.md)
