# Lab 09 — Promote one image and recover a known-good state

**Time:** 60–90 minutes

[Course home](../README.md) · [Previous lab](08-observability.md) · [Next lab](10-flags.md)

A tested source branch is not a running release. Promote the exact image you tested and
restore both image and configuration if required. Prerequisite: Lab 08 and Docker.
This exercise uses local ports; `prod` is a simulation.

## Procedure

Follow the complete commands in [deployment and rollback](../docs/deployment.md).
That procedure captures a baseline image, builds a visibly different candidate, checks
staging, runs the same candidate as simulated prod, and restores the retained baseline.
Use a dedicated clean practice branch and keep both images until the exercise passes.

Before promotion, copy [the release record](../checklists/release-record.md) into
`evidence/09-release.md`. Fill in both image IDs, source commits, configuration, the
smoke results, release authority and stop criteria. For solo work identify yourself
and disclose the lack of an independent approver.

## Introduce a discrepancy

After candidate promotion, run the smoke check with `--version deliberately-wrong`.
It should fail. Treat that as a release-identity discrepancy for the drill. Use the
recorded rollback procedure and verify the baseline identity and behavior.

This manufactured identity mismatch does not mean the candidate has a code defect;
it tests whether you can recognize conflicting evidence and carry out recovery.
Time the interval from your stop decision to a successful baseline smoke check.

## Completion evidence

Keep baseline/candidate identities, staging and prod-simulation checks, the failed
identity check, recovery time and restored smoke result. Explain why rebuilding a
mutable tag is not equivalent to deploying the retained known-good image.

The reference app stores no data. Before applying this technique to an app with a
database, rehearse schema compatibility and restoration. An older image may not read
a newer database. Stop and plan a restore or forward fix when rollback is unsafe.

[Course home](../README.md) · [Previous lab](08-observability.md) · [Next lab](10-flags.md)
