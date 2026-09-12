# Lab 02 — Review a small AI-assisted change

**Time:** 40–60 minutes

[Course home](../README.md) · [Previous lab](01-git.md) · [Next lab](03-testing.md)

A pull request is a change package. Tests provide repeatable checks; review evaluates
intent, assumptions and missing checks. Prerequisite: Lab 01.

## Procedure

1. Start on `main` with a clean status. Run `git switch -c practice/review-wording`.
2. Ask an AI assistant to improve one sentence in the app's home-page `PAGE` text.
   Require it to keep endpoints and release logic unchanged.
3. Run `git diff`. Identify every changed file and explain every changed line.
4. Run the tests. Confirm the links still describe their behavior.
5. Commit only your intended edits.
6. Follow [GitHub setup](../docs/github-setup.md) if needed, then push your branch and
   open a PR against `main`. Complete the provided PR template.
7. Ask a second person to compare your stated intent with the diff and evidence.
   Resolve their comments in a follow-up commit; run the checks again.

If GitHub is not connected yet, perform steps 1–5 locally and write a review record.
The hosted approval exercise remains outstanding until you complete it on GitHub.

## Spot a proposed fault

Consider this proposed “simplification,” without committing it:

```python
return any(checks.values())
```

The intended requirement is that **every** required check passes. Supply an example
where the proposed change incorrectly approves a release. Ask your reviewer to explain
why the apparently readable code violates the requirement.

## Solo mode and completion evidence

A PR author cannot supply independent GitHub approval for their own PR. For solo
practice, take a break and review using [the AI review checklist](../docs/ai-review.md),
then record `solo review; no independent human verification`. Do not represent an AI's
approval as human release authority. Keep a PR link or local diff, findings, responses
and test result in your evidence. Return to `main` when done; merging is optional.

[Course home](../README.md) · [Previous lab](01-git.md) · [Next lab](03-testing.md)
