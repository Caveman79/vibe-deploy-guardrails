# Python 01 — Read CSV and JSON without losing meaning

[Course plan](../../CURRICULUM.md) · [Setup](../../docs/setup.md)

**Practice time:** 2–4 hours plus repetition. Prerequisite: SQL track and basic Python variables, lists, loops and functions. Use the course folder as your terminal working directory.

## Understand

A CSV is a table-shaped text file. JSON can represent records and nested structures. An identifier is a label, not a number to total; missing minutes are not zero. Python helps inspect and transform these files without manual spreadsheet edits.

## Hands-on lab

Create the optional data environment from the course root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --require-hashes -r requirements-data.txt
.venv/bin/python -c "import pandas, requests; print(pandas.__version__, requests.__version__)"
```

If .venv already exists, reuse it. On Windows use WSL as described in setup. Create evidence/inspect.py using csv.DictReader and json.load to read the two fixture files. Print row count, field names and the first synthetic record.

## Deliberately broken example

Read minutes as text, then try summing the strings. Explain the difference between concatenation, conversion, and validation. Do not make invalid text disappear with a broad exception handler.

## Your task

Write an inspection script that reports missing minute values and mission IDs absent from missions.json. Write its summary as JSON.

## Verify and keep evidence

Nine CSV rows, eight mission lookup records, one blank minutes field and one unknown mission M99.

## What AI may get wrong

Inferring numeric types for identifiers or treating JSON text as a Python dictionary without parsing.

## Where this appears in deployment work

Before an integration, inspect what the customer actually exports and write down the format contract.

## No-AI check

Close the assistant for 15 minutes. Explain the data flow and reproduce a small part yourself. Record the difference between what you completed unaided and with assistance. Then use official documentation and the assistant to correct gaps.
