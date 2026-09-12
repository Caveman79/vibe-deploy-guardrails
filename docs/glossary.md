# Plain-language field guide

| Term | Meaning | Operational comparison |
| --- | --- | --- |
| Repository | Files plus their recorded change history | Controlled technical records |
| Commit | An identified snapshot of a change | Recorded configuration change |
| Branch | A separate line of development | Proposed modification package |
| Diff | The exact before/after lines | Change pages |
| Pull request (PR) | A proposal to review and merge a branch | Work package awaiting verification |
| Merge | Incorporate reviewed changes | Accept a configuration change |
| Unit test | Check one small rule | Component functional check |
| Integration test | Check connected components | Installed-system check |
| Smoke test | Short check of a running service | Initial post-maintenance check |
| Regression | Previously working behavior breaks | Introduced discrepancy |
| CI | Run automated checks when changes arrive | Repeatable inspection gate |
| Continuous delivery | Keep changes releasable; release may need approval | Ready for release authority |
| Continuous deployment | Automatically release changes after gates pass | Automated release under an approved policy |
| Environment | Runtime settings, identity, data and infrastructure | Operating configuration |
| Secret | A credential whose disclosure grants access | Controlled access material |
| Dependency | Software your software relies on | Supplied part or subsystem |
| Container image | Packaged app and runtime filesystem | Identified equipment package |
| Container | A running instance of an image | Equipment in operation |
| Digest / image ID | Content-derived identifier | Exact part/configuration identity |
| Least privilege | Only the access needed for the task | Limited authority by role |
| Observability | Evidence to understand runtime behavior | Instrumentation and fault records |
| Rollback | Restore a tested prior release and compatible configuration | Return to known-good state |
| Feature flag | Runtime control for optional behavior | Controlled introduction switch |
| Canary | A small initial rollout population | Limited operational introduction |
| SBOM | Software bill of materials | Parts list |
| Vulnerability scan | Compare software/configuration against known issues | Service bulletin review |
| Branch protection | Enforced rules for accepted changes | Configuration-control gate |

A tag is a convenient label, and may be moved. Record a commit SHA and image digest as
well. Neither an AI explanation nor a green health endpoint substitutes for independent evidence.
