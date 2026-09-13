# Contributing

Help make controlled deployment understandable to someone whose first code ran in a notebook.
Beginner questions, unclear instructions, broken steps and accessibility improvements are welcome.

1. Open an issue describing the learner's problem, expected behavior and a small proposed scope.
2. Create a branch from `main`. Use synthetic data; keep private operational examples out of the repo.
3. Make a focused change. Explain new terms at first use and give expected results for commands.
4. Test behavior changes with meaningful input/output checks. For lab changes, actually follow the steps.
5. Run `python3 -m unittest discover -s tests -v` and `python3 scripts/check_docs.py`.
6. For runtime/Docker changes, build and run `bash scripts/container-check.sh IMAGE` and inspect scans.
7. Complete the PR template. State exactly what ran, what did not, and why.
8. Obtain review and resolve findings. Do not bypass failing gates just to finish a contribution.

AI-assisted contributions are welcome. The contributor remains responsible for correctness,
rights to contributed material, secrets and explaining the diff. Identify material AI
assistance when it helps the reviewer understand the work; never substitute generated
claims for test evidence. Contributions are provided under the repository's MIT license.

## Teaching with the course

Pair one learner as change author and another as reviewer/release authority. Swap roles
halfway through. Allow extra setup time, and let learners explain concepts in their own
operational vocabulary. Use synthetic data and local deployments. Evaluate the capstone
against its evidence rubric, not typing speed or familiarity with jargon.

For solo learners, distinguish a separate self-review from independent verification.
A learner who can articulate a limitation has demonstrated better judgment than one who
checks every box without evidence.

## Community conduct

Be respectful, specific and patient. Critique the change, not the contributor. Do not
harass, disclose private information or treat a beginner's question as a failure.
Maintainers may remove abusive content and restrict participation. Use GitHub's reporting
mechanism for abuse; report security issues through the process in SECURITY.md.

## Data and course changes

Keep all fixtures fictional. Update the expected totals, unaided checkpoints and reference answers together when changing fixtures. Run both test suites for optional data-tool changes. Regenerate the full hash lock when updating `requirements-data.in`; do not drop `--require-hashes` to make an update pass. State which learner path you tried and where its explanation was confusing.
