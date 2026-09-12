# Lab 05 — Inspect the parts list and scan findings

**Time:** 45–60 minutes

[Course home](../README.md) · [Previous lab](04-configuration.md) · [Next lab](06-docker.md)

Dependencies are supplied components, including your runtime and operating system.
Prerequisite: Lab 04. Docker is needed for the executable scan; otherwise read the
workflow now and return after Lab 06.

## Procedure

Read `requirements.txt`: the reference app needs no third-party Python packages.
That does **not** mean it has no dependencies. Inspect `Dockerfile` and list Python,
the base operating system, GitHub Actions, and the Trivy scanner used by CI.

```bash
docker build -t guardrails:scan .
docker save guardrails:scan -o /tmp/guardrails-image.tar
docker run --rm -v /tmp/guardrails-image.tar:/scan/image.tar:ro aquasec/trivy:0.69.3 image --input /scan/image.tar --exit-code 1 --severity HIGH,CRITICAL
```

Expect a report, not necessarily zero findings. The vulnerability database changes;
a network/database failure also stops the job and is not a clean scan. Review findings
by package, installed/fixed version, severity and whether the vulnerable component is used.
Remove the archive after the exercise to reclaim disk space.

Read `.github/workflows/security.yml`: a separate filesystem scan checks secrets and
configuration. Image scanning covers OS/runtime packages. It does not prove source-code
logic is secure, and the filesystem scan is not a complete Git-history secret scan.

## Triage exercise

Suppose a scan reports a HIGH finding with a fixed base-image release. Write a proposed
change: update the base, rebuild, rescan, rerun tests, rehearse and record a new image ID.
Do not add `continue-on-error` to turn red into green. If a risk must be accepted, record
the specific finding, rationale, approver, compensating control and expiry date.

## When AI proposes a package

Before installation: verify its name against the publisher's official documentation,
check its maintenance/license, and explain why the standard library is insufficient.
Use a virtual environment and record direct dependencies plus a resolved, hash-verified
lock of transitive dependencies. Review lock changes and scan that environment with a
maintained tool such as [pip-audit](https://pypi.org/project/pip-audit/).
The starter has no Python package lock because it has no external Python packages.

## Completion evidence

Keep a dated scan outcome and a sample triage decision. Identify which dependencies
Dependabot tracks here (Actions and the Docker base), and which tool needs a manual
version review (the scanner image referenced inside a shell step).

[Course home](../README.md) · [Previous lab](04-configuration.md) · [Next lab](06-docker.md)
