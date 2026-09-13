# Practical interview drills

Spend 10–15 minutes per drill without AI. Explain your reasoning aloud, then consult the reference hints below. Score 0 for missing/unsafe, 1 for partial or prompted, 2 for correct with an explanation and a check. These are practice scores, not employer hiring standards.

| Drill | Starting evidence | Task / verification |
| --- | --- | --- |
| Bad SQL | `sql/broken/03-join-fanout.sql` | Explain the inflated total; repair it and recover 135 minutes. |
| Dirty CSV | `fixtures/flight_intake.csv` | Find duplicates, absent/invalid minutes and orphan mission IDs. Predict 4 accepted / 5 quarantined before running the reference. |
| API | Running local app, `/api/missions` | Retrieve all 8 missions, handle pagination and describe timeout/non-200 behavior. |
| Exposed credential | Review-only text: `TOKEN = "FAKE_TRAINING_ONLY_NOT_A_SECRET"` | Explain why replacing a real leaked credential in the latest file is insufficient. Never introduce a real secret. |
| AI pull request | Proposal: `except Exception: return {"ready": True}` | Reject fail-open behavior. Propose a test proving missing evidence holds release. |
| Failed release | Health says r2; release record approves r1; functional test fails | Identify the mismatch, contain the rollout, request recovery authority and verify the restored version’s behavior. |
| Rollback | New code renamed a persisted database column | Explain why reverting only the image may fail; request migration compatibility and tested restore evidence. |
| Monitoring gap | Dashboard shows only HTTP 200 totals | Propose customer functional checks, error rate/latency alerts and an owner/runbook. Avoid logging tokens or raw customer records. |
| Customer configuration | C01 wind limit 20; C02 limit 15; shared default 20 | Show how a shared default could leak into C02. Require explicit customer lookup, validation and negative tests; these invented thresholds are not aviation guidance. |

## Reference hints — read after trying
Aggregate at the correct grain before joining a one-to-many table. Quarantine questionable input instead of silently repairing it. A successful first API page is not a complete dataset. Revoke/rotate an exposed real secret, investigate access and address history/caches under the organization’s process. Tests and health are evidence, not release authority. Record code, configuration and data compatibility together. Name the gap you cannot resolve and the engineer or owner who can help.

Save your first attempt, score and correction in `evidence/interview/`. Repeat a different variant; memorizing the reference answer is not the goal.
