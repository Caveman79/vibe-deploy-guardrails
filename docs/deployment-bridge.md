# Connect the preserved deployment labs to the scenario

Use these prompts alongside the existing hands-on instructions. Keep the functional
checks and failure drills in those labs; this adds the implementation-role context.

| Phase | Deliberate discrepancy and learner task | Verification | AI pitfall | Deployment-job connection |
| --- | --- | --- | --- | --- |
| Change control | A PR claims only wording changed but alters approval logic. Compare the diff with intent. | Demonstrate a failing mixed-check test before repair. | Approving a polished summary without inspecting changed lines. | Translate requirements into acceptance evidence. |
| Environments | C02 receives C01's wind limit; the service still returns HTTP 200. Record expected configuration and reject the wrong one. | Compare customer ID, limit, release version and environment. | Treating process health as customer correctness. | Customer implementation requires configuration control. |
| Dependencies | A scan finds a base-image vulnerability. Propose a patch with a retained baseline. | New image scan plus same functional tests, not a scan suppression. | Removing the gate to make CI green. | Decide what evidence is needed before accepting supplied components. |
| Least privilege | An AI proposal requests admin access for a read-only report. Remove the unnecessary privilege. | Explain and test the denied write operation in Docker. | “Run as root” as generic troubleshooting. | Match privileges to the actual operational task. |
| Deployment | A newer source revision runs with an old version label or wrong customer configuration. | Smoke check identity and business behavior in staging and simulated prod. | Rebuilding between environments and assuming the image is identical. | Keep source, artifact and configuration identities distinct. |
| Observability | Missions API returns 503 because the training DB was not created. Diagnose the missing dependency. | Restore the fixture DB and recheck mission count; preserve sanitized logs. | Logging tokens or returning an empty list on database failure. | Explain failure cause and customer impact separately. |
| Recovery | Optional guidance confuses operators during limited introduction. Stop expansion and restore prior flag/image state. | Same representative requests pass after recovery; record time. | Assuming a rollback reverses data changes. | Coordinate incident action and communications. |
| Auditability | A release record has a green check but no source/image identity or approver. Repair the evidence package. | Another person can follow the record to the exact run and recovery procedure. | Inventing results or claiming independent approval by AI. | Demonstrate accountability without inflated technical claims. |

For each phase, spend 15 minutes without AI explaining the failure and the next three
checks. Then use AI to critique your explanation, retaining the original answer.
