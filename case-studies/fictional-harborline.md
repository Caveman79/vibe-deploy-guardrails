# Fictional example — qualification gaps in a customer mission report

**Entirely fictional training example. These are illustrative outcomes, not the author's
service record or measured professional results.**

## 1. Operating environment
Harborline UAS is preparing a local demonstration for two fictional customers.

## 2. Before condition
A report used inner joins and omitted missions with no risk-approval record.

## 3. Constraint
The team had a small export, no production access and a short demonstration window.

## 4. What changed
The fictional implementation lead clarified the missing-evidence rule, revised the query
with an engineer, and added a check for incomplete mission records.

## 5. Technical / operational design
A seeded SQLite dataset feeds a read-only report. Left joins preserve exceptions;
qualification, aircraft and approval holds are separate columns. Staging tests cover missing evidence.

## 6. Stakeholders
Customer operations lead, training lead, implementation lead, software engineer and release authority.

## 7. Risks and controls
Risks included disappearing records and treating the report as flight authority. Controls
were explicit fixture cases, review, fixed assessment dates and a clear advisory boundary.

## 8. Measured result
In the deterministic exercise, the corrected report returns three planned missions:
M05 and M06 with holds; M07 with no holds under the limited rule. The missing-approval
mission M06 remains visible. This is a fixture verification, not a measured business improvement.

## 9. Lessons
A query can run successfully and still hide the exceptions operators need to see.

## 10. Deployment-strategist relevance
The example connects stakeholder requirements, data semantics, technical verification
and operational interpretation without attributing professional engineering experience to a learner.
