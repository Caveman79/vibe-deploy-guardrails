# Explain the work, with evidence

This course supports practical technical fluency; it does not certify professional software engineering or guarantee a role. Describe what you personally changed, what the reference implementation supplied, where AI helped and what you can demonstrate unaided.

| Concept | Plain explanation | Demonstrate or qualify |
| --- | --- | --- |
| JOIN | Connect records using a shared identifier, like matching a mission to its operator. | Show how a left join keeps an operator with no qualification. |
| API | An agreed way for programs to request and exchange information. | Fetch all pages, inspect HTTP status and validate the response. |
| Staging / production | A rehearsal environment versus the system people rely on. | Explain separate credentials/data and why a name alone provides no isolation. |
| CI/CD | Automated checks and a repeatable release path. | Point to a run and distinguish tests, deployment and release approval. |
| Rollback | Restore a verified prior software/configuration state. | Show recovery and explain data migration limitations. |
| Observability | Evidence that helps explain what a system is doing and why it failed. | Follow a request ID; identify absent alerts or functional metrics. |
| Least privilege | Grant only the access needed for a task. | Explain read-only SQL, container user and repository permissions. |
| Secrets | Credentials that grant access, not ordinary settings. | Keep them out of source/history/logs; rotate exposed credentials. |
| Auditability | Records that connect a change to its reason, checks and authority. | Trace commit → PR → checks → image → release → incident/recovery. |

## Diagnose a failing deployment
Clarify the affected customer, onset and last known-good version. Check health, functional behavior, configuration and logs with a request ID. Compare the deployed image/config with the approved release. Contain exposure, agree recovery authority, restore a tested compatible state and verify customer behavior. Record uncertainty instead of guessing a root cause.

## Questions before release
What changed? What customer behavior did we test? Which failure cases remain? Who approves? What access and secrets are needed? How will we detect harm? What threshold stops rollout? Can we recover both code and data? Who owns the response?

## Practice and portfolio
Complete the [practical drills](interview-drills/README.md) and [unaided checkpoints](assessments/checkpoints.md). Show a query, a tested change and a recovery record. Use the [case-study template](case-studies/TEMPLATE.md) for actual work only after sanitizing and checking disclosure permission. The supplied fictional example is not your employment history.

A truthful introduction: “I bring operational experience and have been building technical fluency through a synthetic deployment project. I can demonstrate this query and explain the release controls I practiced. I would partner with engineers for production architecture and security decisions.” Replace the details with your own evidence; do not imply course completion before doing it.
