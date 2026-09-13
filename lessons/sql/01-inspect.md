# SQL 01 — Read an unfamiliar schema

[Course plan](../../CURRICULUM.md) · [Scenario and schema](../../docs/scenario.md)

**Practice time:** 2–4 hours including repetition. Prerequisite: Start Here.

## Understand

A schema is the map of the records: tables, fields, identifiers, and relationships. Start with what one row means before asking for totals. A mission is not a flight log; one planned mission may have no flight yet.

## Hands-on lab

Create the synthetic database once, from the course folder:

```bash
python3 -m ops_data.seed
python3 -m ops_data.query sql/start.sql
python3 -m ops_data.query sql/solutions/01-inspect.sql
```

The seed command refuses to overwrite an existing database. If it says the file exists, continue with the queries. The first query returns M01 through M08. The schema query returns 12 tables.

Open `ops_data/schema.sql` in your editor. Find the primary key (record identity) and foreign keys (references to other records) for missions. Draw customer → mission → flight log. Note that qualifications use two fields as their combined identity.

## Read the reference SQL

This is the SQL inside the reference file. Read it alongside the explanation above; the Python command runs this saved query against your database.

```sql
SELECT name, sql FROM sqlite_schema WHERE type='table' ORDER BY name;
```

## Deliberately broken example

Treat a row in flight_intake as a completed flight. Explain why that is wrong by comparing flight_intake with flight_logs.

## Your task

First create the folder with `mkdir -p evidence`. In your text editor, create a new file and save it as `evidence/my-schema.sql` in the course folder. A `.sql` file is plain text containing a database question. Start with `SELECT aircraft_id, model, status FROM aircraft;`. `SELECT` names the fields to show; `FROM` names their table. Run `python3 -m ops_data.query evidence/my-schema.sql` in your second terminal. Then change the query yourself.

Write a query in evidence/my-schema.sql that lists aircraft IDs, model and status. Run it through ops_data.query. Explain which table records maintenance work and which stores the current aircraft status.

## Verify and keep evidence

Three aircraft; A02 is in maintenance. Your schema map must state the grain of at least five tables.

Save your query, result, and a three-sentence interpretation in `evidence/`. Run from the repository root. Do not submit only a screenshot of a green command.

## What AI may get wrong

Guessing field names or treating a current status as historical truth.

## Where this appears in deployment work

You often inherit a customer system before you receive a complete specification. A schema map turns assumptions into questions.

## No-AI check

Close the reference and assistant for ten minutes. Recreate or explain the main operation on a slightly different filter. Record what you could do unaided and what you needed help with. Looking up basic syntax in official documentation is allowed; generated solutions are not.

[Next SQL lesson](02-filter.md)
