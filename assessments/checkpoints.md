# Practical checkpoints

Use a 30–60 minute no-AI attempt, followed by an assisted review. Official syntax docs
are allowed; generated answers and reference solutions are closed for the initial attempt.
Retain the first attempt and your corrected version. A partner can change customer IDs
or thresholds to make memorized answers less useful.

Score each task 0 (cannot explain), 1 (works with help), or 2 (works and can explain unaided).
Advance when every task scores 2 on a fresh attempt, or record the specific gap and
repeat practice before relying on that skill. This is a course rubric, not a hiring standard.

## Week 2

- List C02 missions ordered by planned time.
- Sum authoritative flight minutes for each customer and reconcile the grand total.
- Include operators whose qualification record is absent; explain INNER versus LEFT JOIN.
- Diagnose the fanout query without accepting the displayed total.

Expected checks: C02 has M03, M04, M06, M08; minutes 75/60, total 135;
O04 has no qualification. The cross join inflates 135 to 405.

## Week 4

- Use a CTE and window function to find the latest flight for each customer.
- Classify qualification status as of a fixed date, including missing records.
- Identify duplicates, invalid durations, bad dates and missing references in intake.
- Explain the M05/M06/M07 exception report and its operational limitations.

Expected checks: F02/F04 are latest; O02 expired and O04 missing; intake has 9 rows,
4 accepted after explicit rules; M05/M06 held, M07 no holds under this limited rule.

## Week 6

- Inspect the CSV and produce a validated pandas summary that reconciles with SQL.
- Fetch all mission API pages and detect a response with a missing pagination marker.
- Handle a stopped server as failure rather than zero records.
- Explain why authentication, customer filtering and authorization differ.

Expected checks: 4 accepted, 5 rejected, 135 minutes; API full export 8 missions.
Show a nonzero failed-client exit and no new success report.

## Week 8

- Make a small branch/PR and explain the exact diff.
- Add a test that catches a plausible defect and demonstrate red → green.
- Reject invalid configuration and demonstrate a denied container write.
- Identify exact source revision, runtime image and dependency evidence.

## Week 10

- Identify wrong environment/version despite a responding health endpoint.
- Diagnose one 400 versus one 503 and describe impact without exposing secrets.
- Rehearse known-good recovery and verify representative behavior afterward.
- Explain what image rollback cannot undo.

## Week 12

- Complete the integrated capstone and security review.
- Deliver a 5-minute technical/operational handover with honest limitations.
- Complete three unfamiliar interview drills without AI.
- Publish only selected sanitized evidence; use the case-study template without inventing outcomes.

For weeks 8–12, expected evidence is the reproducible action, identity, run output and
explanation, not a predetermined “green” result. A discovered blocker handled correctly
can demonstrate good judgment; it does not justify marking the deployment successful.
