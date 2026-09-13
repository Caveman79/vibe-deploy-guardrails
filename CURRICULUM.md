# Technical bridge — 8–12 weeks, self-paced

The central question: **How does an experienced operator become technically credible
enough to help deploy software and AI systems safely without pretending to be a software engineer?**

The default route is **12 weeks at 8–10 hours/week** (96–120 hours), including repetition,
debugging and evidence review. Lesson estimates are first-pass time, not the total learning
budget. Use roughly 2 hours reading, 4 hours doing, 1–2 hours debugging/repeating and
1–2 hours explaining and assessing each week.

An 8-week route at the same weekly hours is a 64–80 hour foundation route. It does not
promise equivalent depth: pass the checkpoints before compressing, reduce optional
extension tasks rather than skipping SQL, security or recovery, and extend the schedule
when evidence shows a gap. A 10-week route pairs adjacent phases after SQL. This is
learning evidence, not a credential or guarantee of eligibility for any particular job.

| Phase | Default weeks | Work and outcome |
| --- | --- | --- |
| 1. Data fluency | 1–4 | Nine SQL labs; interpret schema, join correctly, detect defects and explain exception reports |
| 2. Python for operators | 5–6 | Six data/API labs; pandas, CSV/JSON, validation, customer configuration and automation |
| 3. Software change control | 7 | Existing Git, review and test labs; commit an explainable change |
| 4. Reproducible environments | 8 | Dependencies, config, secrets, limited privileges and Docker |
| 5. Deployment | 9 | CI, environments, functional checks, logs and operating evidence |
| 6. Safe release | 10 | Same-artifact promotion, rollback, controlled feature rollout and release records |
| 7. Security and AI-code review | 11 | Scanning and adversarial review; investigate rather than suppress findings |
| 8. Capstone | 12 | Integrate, deploy locally, operate, recover, and prepare an honest portfolio handover |

## Phase 1 — SQL first

1. [Read an unfamiliar schema](lessons/sql/01-inspect.md)
2. [SELECT, WHERE and ORDER BY](lessons/sql/02-filter.md)
3. [GROUP BY and aggregation](lessons/sql/03-aggregate.md)
4. [JOINs and NULL](lessons/sql/04-joins.md)
5. [Subqueries and CTEs](lessons/sql/05-cte.md)
6. [CASE and date/time](lessons/sql/06-dates-case.md)
7. [Window functions](lessons/sql/07-window.md)
8. [Duplicates and data quality](lessons/sql/08-quality.md)
9. [Operational exception report](lessons/sql/09-mission-holds.md)

Weeks 1–2 focus on lessons 1–4; weeks 3–4 on 5–9. Repeat with different customer and
date filters. Use the [Week 2 and Week 4 checkpoints](assessments/checkpoints.md).

## Phase 2 — Python for operators

1. [CSV and JSON](lessons/python/01-files.md)
2. [pandas and reconciliation](lessons/python/02-pandas.md)
3. [Validation, logging and automation](lessons/python/03-validation.md)
4. [REST APIs and pagination](lessons/python/04-api.md)
5. [Authentication and configuration](lessons/python/05-auth-config.md)
6. [Customer handover report](lessons/python/06-integration.md)

Install optional dependencies only when you reach this phase. Complete the Week 6
checkpoint before using AI to assemble a larger integration.

## Phases 3–7 — Preserved deployment labs

The original labs remain intact as the practical deployment track. Their numbering is
historical, not the order of the SQL-first bridge. Start each lesson on a clean practice
branch and preserve the baseline.

- Phase 3: [Git](labs/01-git.md), [review](labs/02-review.md), [tests](labs/03-testing.md).
- Phase 4: [configuration/secrets](labs/04-configuration.md), [dependencies](labs/05-dependencies.md), [Docker/least privilege](labs/06-docker.md).
- Phase 5: [CI and protection](labs/07-ci.md), [observability](labs/08-observability.md).
- Phase 6: [promotion/rollback](labs/09-release-rollback.md), [feature rollout](labs/10-flags.md).
- Phase 7: repeat the scan portion of [dependencies](labs/05-dependencies.md), then [AI-code review](docs/ai-review.md) and [security drills](interview-drills/README.md).

Use the UAS scenario to connect these labs: the published app represents the customer's
mission-summary service. Version/configuration, validated input and recovered behavior
matter together. See [deployment job practice prompts](docs/deployment-bridge.md) for
a broken example, AI pitfall, verification task and role connection for each phase.

## Phase 8 — Integrated capstone

Use [the operational capstone](CAPSTONE.md). The smaller [original readiness-feature
capstone](labs/11-capstone.md) remains available as a rehearsal or extension.

Finish with [interview translation](INTERVIEW_TRANSLATION.md), practical drills,
a sanitized [case-study template](case-studies/TEMPLATE.md), and the portfolio checklist.
