# Capstone: a controlled customer pilot

Allow 8–12 hours after the preceding phases; repeat until you can explain your work. This is a local deployment rehearsal with synthetic data, not a real flight or customer release.

## Mission
Harborline must deliver a customer-specific readiness briefing. M05 and M06 have unresolved holds. M07 passes the three modeled checks; this does not certify flight safety. Build a small change that exposes those reasons clearly without silently excluding missing qualifications.

## Your work
1. Write your own query joining missions, operators, qualifications, aircraft and approvals. State each table’s grain. Use 2026-09-15 as the assessment date and include every planned mission.
2. Run the CSV intake validator. Record 4 accepted rows, 5 quarantined rows, 135 minutes and the reasons for rejection. Explain why coercing bad values to zero conceals problems.
3. Fetch all mission API pages. Produce a dated C01 briefing with four missions and 75 accepted flight minutes. Label synthetic source data and avoid treating these counts as live operational truth.
4. Add a read-only briefing endpoint or improve its browser presentation on a new branch. Validate the customer parameter. Test missing qualifications, invalid inputs and the positive case.
5. Open a pull request with the problem, evidence, limitations and recovery plan. Ask a reviewer to explain one failure case independently. If working alone, label self-review honestly.
6. Build and check a container. Record the image digest, config, commit and test evidence. Rehearse dev, test, staging and prod labels locally; a label alone does not isolate environments.
7. Deliberately introduce a harmless bad version label in staging. Diagnose using health, request IDs and logs, then restore the previous image/config. Verify a functional request after recovery.
8. Enable guidance for a small deterministic cohort, compare control and enabled responses, then disable it. A feature flag is not permission to access another customer’s data.
9. Run security scans, inspect dependency changes and document branch/release controls actually configured. Do not mark a documented control as enforced.
10. Write a case study and give a five-minute demonstration without AI assistance.

## Acceptance evidence
Save evidence locally, then sanitize any selected portfolio material. Include your SQL, intake report, tests, PR link, image digest, release record, request result before/after rollback, scan outcomes and remaining risks. Never include credentials.

A reviewer should reproduce all three planned-mission results, find the rejected intake rows, distinguish C01 from C02, and trace a release back to a commit and functional check. Explain a JOIN, pagination, least privilege and rollback unaided. Use the [checkpoint rubric](assessments/checkpoints.md); incomplete evidence means more practice, not a failed career transition.

## Deliberately broken proposal
“The endpoint returned 200 and CI was green, so promote it. If anything fails, roll back the image, including the database.” Identify why this is inadequate: functional correctness, review/release authority, customer configuration and data compatibility require separate evidence. An old image does not undo changed data. This training database is seeded and read-only; a real system needs tested backup/restore and migration compatibility plans.

## AI pitfalls and job relevance
AI may hide missing rows with inner joins, confuse environment labels with isolation, or write a rollback plan that cannot recover state. Your deployment role is to make those assumptions visible and ask for evidence before expanding customer exposure.
