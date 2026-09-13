# Local delivery and rollback rehearsal

This is the executable deployment target for the course: disposable Docker containers
on your own machine. Nothing here creates a cloud service. Read the
[architecture boundaries](architecture.md) first. Use Bash and keep the same terminal
open throughout so the image variables remain set.

## 1. Capture the known-good release

Start at a clean, committed course baseline with Docker running. Ensure ports 8001/8002
and the container names below are unused. `git status --short` should be empty.

```bash
git switch -c practice/release-rehearsal
python3 -m unittest discover -s tests -v
docker build -t guardrails:baseline .
BASELINE_IMAGE=$(docker image inspect guardrails:baseline --format '{{.Id}}')
BASELINE_COMMIT=$(git rev-parse HEAD)
bash scripts/container-check.sh "$BASELINE_IMAGE"
```

Record `BASELINE_IMAGE` and `BASELINE_COMMIT` in your release record using `echo "$BASELINE_IMAGE"`
and `echo "$BASELINE_COMMIT"`. Retain this local image; do not prune it during the drill.

## 2. Build a distinct candidate

In `guardrails/ui.py`, add a short sentence to the HTML returned by `home()`, such as
`<p>Training candidate: recovery procedure rehearsed.</p>`. Keep the endpoints and rule unchanged.
Inspect the diff, run tests and commit:

```bash
git diff
python3 -m unittest discover -s tests -v
git add guardrails/app.py
git commit -m "Add training candidate notice"
docker build -t guardrails:candidate .
CANDIDATE_IMAGE=$(docker image inspect guardrails:candidate --format '{{.Id}}')
CANDIDATE_COMMIT=$(git rev-parse HEAD)
test "$BASELINE_IMAGE" != "$CANDIDATE_IMAGE"
```

Record the candidate image and commit as above. A source commit and a runtime version
label are distinct: the label is supplied configuration, not cryptographic proof of source.
For this lab, use `candidate` and `baseline` as readable labels and retain the actual IDs.

## 3. Check staging

```bash
docker run -d --name vdg-staging --read-only --cap-drop=ALL --security-opt=no-new-privileges --memory=128m --cpus=1 --pids-limit=64 -p 127.0.0.1:8001:8000 -e APP_ENV=staging -e APP_VERSION=candidate -e ROLLOUT_PERCENT=0 "$CANDIDATE_IMAGE"
python3 scripts/smoke.py --url http://127.0.0.1:8001 --version candidate --environment staging
```

If the first request races startup, wait a second and retry the smoke command. If it
still fails, inspect `docker logs vdg-staging` and hold. Open the home page and verify
the candidate notice. Complete review, scan and release evidence before promotion.

## 4. Promote the same image to simulated production

```bash
docker run -d --name vdg-prod --read-only --cap-drop=ALL --security-opt=no-new-privileges --memory=128m --cpus=1 --pids-limit=64 -p 127.0.0.1:8002:8000 -e APP_ENV=prod -e APP_VERSION=candidate -e ROLLOUT_PERCENT=0 "$CANDIDATE_IMAGE"
python3 scripts/smoke.py --url http://127.0.0.1:8002 --version candidate --environment prod
docker inspect vdg-prod --format '{{.Image}}'
```

Confirm the reported ID equals the candidate ID; do not rebuild between environments.
Check representative requests during the [observation window](../labs/08-observability.md).
In a real service, environment data/identity would differ while the approved image remained the same.

## 5. Rehearse recovery

Run the deliberately wrong-version smoke command from Lab 09 and record the failure.
Then stop and replace only the disposable simulated-prod container:

```bash
docker rm -f vdg-prod
docker run -d --name vdg-prod --read-only --cap-drop=ALL --security-opt=no-new-privileges --memory=128m --cpus=1 --pids-limit=64 -p 127.0.0.1:8002:8000 -e APP_ENV=prod -e APP_VERSION=baseline -e ROLLOUT_PERCENT=0 "$BASELINE_IMAGE"
python3 scripts/smoke.py --url http://127.0.0.1:8002 --version baseline --environment prod
docker inspect vdg-prod --format '{{.Image}}'
```

Expect the baseline image ID, the baseline version, and the original home-page text.
This stop-and-replace approach has downtime. It is intentionally simple; it is not
zero-downtime deployment or traffic splitting. Record recovery time and results.
If your terminal was closed, restore variables from the recorded IDs before running commands.

## 6. Clean up

```bash
docker rm -f vdg-staging vdg-prod
git switch main
```

Keep the images until assessment is complete. The candidate commit remains on its
practice branch. These commands do not delete volumes or unrelated containers.

## What changes for real hosting

Before choosing a real target, agree on ownership, data sensitivity, cost and availability
requirements. Use a production server with TLS and appropriate authentication. Separate
service identities and data, centralize logs/metrics, test backups and define who can release.

Resolve a reviewed base-image digest from the official registry, change `FROM` to
`python:3.12-alpine@sha256:THE_VERIFIED_DIGEST`, and review updates regularly. The provided
Dockerfile uses a mutable training tag for accessibility; builds on different dates may differ.
The literal placeholder above is an explanation, not a runnable Dockerfile line.

Push a tested image to a registry and record its **registry digest**. A local image ID
and a registry manifest digest are not interchangeable. Promote the registry digest,
retain prior artifacts and compatible configuration, and scan new builds. Protect release
jobs with environment approvals, use narrowly scoped short-lived credentials when supported,
and do not expose deployment secrets to pull-request code.

The repository's manual workflow is a rehearsal, not full production CD. A real CD
pipeline should promote an already-tested artifact through staging and a protected release
job, verify deployment, and retain auditable evidence. Configure the target-specific
implementation only after those requirements are chosen.

## Base-image choice

The first hosted scan found HIGH/CRITICAL findings in the Debian slim base. This
standard-library-only app now uses the official Alpine variant to reduce unused OS
components. Alpine uses musl rather than glibc; revisit compatibility if native Python
packages are added. The same tests and full HIGH/CRITICAL scan remain required.

The image build also requires the Alpine `libuuid` security update (at least
`2.42.3-r1`). Package repository contents can change, so preserve and promote the
built image ID/digest instead of assuming a later rebuild is identical.
