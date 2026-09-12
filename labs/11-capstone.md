# Lab 11 — Deliver a controlled AI-assisted change

**Time:** 90–150 minutes

[Course home](../README.md) · [Previous lab](10-flags.md)

Your mission: add a `missing_checks` list to readiness responses without weakening the
release rule. Prerequisite: Labs 00–10. Use a fresh branch from the reference `main`.

## Acceptance criteria

- Missing or false checks appear in this order: `review`, `tests`, `rollback`.
- All checks true produces an empty list and `ready:true`.
- Invalid fields still return HTTP 400; missing evidence still means not ready.
- The list contains only known check names, never raw user input.
- Guidance rollout and health/version reporting retain their existing behavior.
- No new package, credential, write endpoint or elevated permission is needed.

## Procedure

1. Write the acceptance criteria and recovery plan in a PR draft before asking AI to code.
2. Ask for the smallest change and an explanation of each changed line.
3. Add meaningful tests for all-pass, one-fail, all-missing, invalid input and flag boundaries.
4. Run the tests and inspect the diff independently. Use [AI review](../docs/ai-review.md).
5. Commit, push and collect CI/scan evidence. Resolve blockers rather than disabling gates.
6. Build an identified image. Verify the new field in a browser/HTTP response in staging;
   the existing smoke test alone does not check this new requirement.
7. Complete the release record and obtain review/release authority, or disclose solo mode.
8. Rehearse local promotion, observe the acceptance criteria and restore the known-good image.
9. Close with a short after-action review: intended outcome, actual outcome, surprise, improvement.

## Assessment

| Criterion | Pass evidence |
| --- | --- |
| Requirements | Specific examples for new behavior and preserved behavior |
| Configuration control | Small diff, commit SHA and PR/review record |
| Verification | Tests catch a plausible bug; current CI/scan results recorded |
| Limited authority | No unexplained dependency, secret or permission increase |
| Delivery | Exact tested image identity and environment settings recorded |
| Recovery | Restored baseline with a successful functional check |
| Honest reporting | Executed checks distinguished from unrun checks and assumptions |

Pass all seven criteria. A working feature with no recovery evidence is incomplete.
An AI-written explanation is not evidence that a command ran. Ask a partner to assess
your record, then explain the release decision aloud without relying on software jargon.

There is no single required code solution: review should assess the acceptance criteria.
Keep your final feature on its own branch/PR so the course baseline remains available.

[Course home](../README.md) · [Previous lab](10-flags.md)
