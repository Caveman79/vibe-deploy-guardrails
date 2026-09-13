# Start here — one step at a time

This course is for an experienced operator learning technical skills. You do not need
to know software-engineering vocabulary before you start. You do need to stop and
explain what a result means before trusting it.

## 1. Open the course folder in a terminal

The terminal is where commands go. The browser is where you read the guided pages.
Your terminal must be in the folder containing this file, `README.md`, and `guardrails/`.
Run `pwd` to see the folder and `ls` to list its files. If you downloaded the ZIP,
extract it first. If you cloned the repository, open that clone.

## 2. Start the guided app

Copy one line at a time:

```bash
python3 -m ops_data.seed
python3 -m guardrails.app
```

If the first command says the database already exists, that is fine: it is protecting
your work from being overwritten. Continue with the second command.

When you see `startup`, leave that terminal running. Open http://127.0.0.1:8000 in your
browser. Choose **Start SQL lesson 1**. The optional five-step browser orientation
explains what the app is and what its results mean.

Do not type new commands into the terminal while the server is running there. Open a
second terminal, enter the same course folder, and use that for the SQL exercises.
Ctrl+C stops the server. Closing it means the browser pages will stop responding.

## 3. Ask your first database question

In the second terminal, run:

```bash
python3 -m ops_data.query sql/start.sql
```

Expect eight rows: missions M01 through M08. A query asks for information; this tool
opens the training database read-only. Next read [SQL 01](lessons/sql/01-inspect.md).
No pandas, Docker, cloud account or API key is needed for the SQL phase.

## 4. Keep an honest learning record

Create a local evidence folder with `mkdir -p evidence`. Save queries, results,
explanations and mistakes there. This folder is ignored by Git. Later you will choose
sanitized evidence to share; do not publish your entire working folder by accident.

The [course plan](CURRICULUM.md) tells you what comes next. The [milestone record](assessments/milestones.md)
separates unaided understanding from AI-assisted work. If a command fails, use the
[troubleshooting guide](docs/setup.md) and copy the exact error when asking for help.
