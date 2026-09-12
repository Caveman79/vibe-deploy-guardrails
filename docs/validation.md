# Validation record — 2026-09-12

This file reports preparation-environment evidence, not a hosted CI certification.

| Check | Result |
| --- | --- |
| Python unit and real-loopback HTTP integration suite | 10 tests passed on Python 3.14 |
| Local Markdown link targets | Passed for all supplied Markdown files |
| Python, YAML and shell syntax | Passed |
| Real app startup and smoke commands | Passed; wrong version rejected, 0/100 rollout checked, invalid configuration rejected |
| Lab 03 deliberate all-to-any fault | Functional-rule tests fail as intended in an isolated copy |
| Docker build and container smoke/hardening check | Not run: Docker is not installed in the preparation environment |
| Trivy vulnerability, secret and configuration scans | Not run: Docker/scanner unavailable locally |
| GitHub Actions execution | Not run: no GitHub connection/remote available |
| Branch and environment protection | Not configured; requires repository settings and a test PR |
| End-to-end Docker promotion/rollback lab | Not run locally; complete before declaring a verified release |

Do not infer a clean scan or green hosted pipeline from the presence of workflow files.
Review current scan findings, verify the container exercises and configure the hosted
gates before tagging a public release. Source and curriculum are ready for review;
the container and hosted operational checks remain release prerequisites.
