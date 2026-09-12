# Publish and configure GitHub

Publishing the repository shares source and lessons. It does not deploy the app or
automatically enable branch protection. The optional ChatGPT/GitHub plugin is not
required for ordinary Git publishing.

## Prepare the local repository

Review the files, including hidden `.github/` content. Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
git status --short
```

If this is an extracted ZIP without Git history, run `git init -b main`, `git add .`,
and `git commit -m "Add Vibe Deploy Guardrails course"`. Set your chosen Git identity
if prompted. Check `git diff --cached` before the commit. Do not include secrets or
private release evidence. Review the [validation report](validation.md) for unrun checks.

## Create and push

On GitHub, create an empty repository named `vibe-deploy-guardrails` under your intended
account or organization. Choose Public to share the course. Do not initialize a README
or license there because the local repository already contains them.

Copy the HTTPS or SSH clone URL GitHub provides, then use it in place of `YOUR_REPOSITORY_URL`:

```bash
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Use your normal GitHub authentication flow. Do not paste a token into chat, source, or
a remote URL. If an `origin` already exists, inspect it with `git remote -v` before
changing anything. For an existing nonempty remote, integrate history through a reviewed
branch; do not force-push over someone else's work.

Confirm that hidden `.github/` files reached GitHub. Inspect Actions: CI and Security
should run. Review failures before declaring the repository release-ready. The local
environment used to prepare this course could not execute Docker or hosted workflows.

## Protect the default branch

Using repository Settings, configure a ruleset or branch protection for `main`:

- Require a pull request and one approving review when a second reviewer is available.
- Dismiss stale approvals after changes and require resolved conversations.
- Require the actual `tests`, `container` and `scan` checks from the first workflow runs.
- Require the branch to be up to date with the base branch before merge.
- Block force pushes and branch deletion; minimize and document bypass authority.
- Apply the rules to administrators where available.

Rules and availability depend on repository visibility and account plan. Verify them
with Lab 07's intentionally failing PR. If practicing alone, retain PR/check gates,
record the missing independent approval, and do not claim independent verification.

Optionally create `.github/CODEOWNERS` using real GitHub usernames or teams with repository
access, especially for workflows and security-sensitive files, then enable required
code-owner review. No fictitious owner is supplied in this starter.

## Protect the rehearsal environment

Create an environment named `training-release`. Restrict deployment branches to `main`,
add a required reviewer and prevent self-review where supported. The workflow's name
reference alone does not enable those protections. If unavailable, record that the
manual workflow is not independently approval-gated.

Run **Release rehearsal** from Actions on `main`, approve through the configured gate,
and inspect its summary. It creates and removes a runner-local container only.

## Complete the public-project setup

Enable available dependency alerts and secret scanning/push protection. Enable private
vulnerability reporting before inviting security reports. Inspect Dependabot PRs rather
than automatically accepting all updates. Add a repository description and topics such as
`ai-assisted-development`, `deployment`, `python`, `devops`, `learning`, and `vibe-coding`.

After all checks pass and limitations are reviewed, create a `v0.2.0` tag/release from the
approved commit. Cite the validation evidence and known limitations in the release notes.
Do not create a “verified” badge until the corresponding hosted check has actually run.

References: [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches),
[secure Actions usage](https://docs.github.com/en/actions/reference/security/secure-use).
