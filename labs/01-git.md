# Lab 01 — Record and reverse a change

**Time:** 40–60 minutes

[Course home](../README.md) · [Previous lab](00-baseline.md) · [Next lab](02-review.md)

Git is configuration control: it records snapshots and lets you inspect exactly what changed.
Prerequisite: Lab 00. Stop the app. Commands run from the repository root.

## Procedure

If you cloned this repository, it already has Git history. If you extracted a ZIP,
initialize history once:

```bash
git init -b main
git add .
git commit -m "Establish course baseline"
```

If Git requests your identity, set your chosen name and email with `git config user.name`
and `git config user.email`, then retry the commit. See [setup](../docs/setup.md).
Do not run `git init` in your home folder.

```bash
git status
git switch -c practice/change-record
```

Create `docs/practice-note.md` in your editor containing: `Every release needs recovery evidence.`

```bash
git diff
git status
git add docs/practice-note.md
git diff --cached
git commit -m "Document recovery evidence requirement"
git log --oneline -3
```

An untracked new file appears in `status`, not ordinary `diff`; staged content appears
in `diff --cached`. “Staged” means selected for the next commit.

## Introduce and recover a fault

Change your note to say `Recovery is optional.` Review the diff, stage only that file,
and commit with message `Practice an incorrect policy`. Run:

```bash
git revert --no-edit HEAD
git log --oneline -4
```

Expect your original sentence to return and a new revert commit in history. Revert
preserves the record; deleting history would remove useful evidence. This procedure
assumes the incorrect policy was your most recent commit on this practice branch.

## Debrief and completion evidence

Record the good commit, bad commit and revert commit in `evidence/01-git.md`.
Use `git status` to confirm no pending tracked edits. Return to `main` with
`git switch main`. Keep the practice branch for your evidence; do not merge the fault exercise.
Explain the difference between restoring source code and rolling back a running deployment.

[Course home](../README.md) · [Previous lab](00-baseline.md) · [Next lab](02-review.md)
