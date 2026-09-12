# Pre-release checklist

Copy this into a PR or release record. An unchecked item needs an owner and a decision,
not a guessed checkmark. For the local training app, mark inapplicable items with a reason.

- [ ] Intent and observable acceptance criteria are clear.
- [ ] Diff is small, understood, and tied to a recorded change.
- [ ] Reviewer and release authority are identified; independence limits disclosed.
- [ ] Functional and negative-path tests passed for this source revision.
- [ ] CI, container check and current scans passed, or a specific exception is approved.
- [ ] Runtime, direct/transitive dependencies and base image are identified.
- [ ] Configuration validated; staging/prod identity and data separation understood.
- [ ] No secrets in source, history, image, prompts, evidence or logs.
- [ ] App and pipeline use minimum permissions.
- [ ] Exact image and source identities recorded; same image tested and promoted.
- [ ] Post-release smoke check and observation window are specified.
- [ ] Stop criteria and on-call/release owner are named.
- [ ] Known-good image AND configuration retained; recovery rehearsed.
- [ ] Data changes assessed; restore/forward-fix plan exists if rollback cannot undo them.
- [ ] Feature flag state, cohort, expansion criteria and retirement owner recorded.
- [ ] Release result and follow-up discrepancies captured.
