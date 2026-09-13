# Reference shelf

Primary documentation consulted while preparing the course. Account features and tool
versions can change; verify the current page when configuring a real repository.

- [Python HTTP server](https://docs.python.org/3/library/http.server.html): local-server API and production limitation.
- [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches): enforced review and status checks.
- [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use): restricted permissions, full action commit pins and secret boundaries.
- [Docker building best practices](https://docs.docker.com/build/building/best-practices/): base images, digest pinning and runtime users.
- [Trivy filesystem scanning](https://trivy.dev/docs/latest/target/filesystem/): secret and configuration scanners.
- [Trivy image scanning](https://trivy.dev/docs/latest/target/container_image/): packaged dependency scanning.
- [Trivy 0.69.3 release](https://github.com/aquasecurity/trivy/releases/tag/v0.69.3): reference scanner version; review newer versions before production adoption.
- [pip-audit](https://pypi.org/project/pip-audit/): optional Python dependency vulnerability auditing when packages are added.

The course deliberately uses no third-party Python runtime packages. Its versioned
scanner Docker tag and mutable Python base tag are not immutable digest pins; the labs
explain how to improve provenance and record the images actually used.

## Data and integration track

- [SQLite SELECT syntax](https://www.sqlite.org/lang_select.html)
- [SQLite date and time functions](https://www.sqlite.org/lang_datefunc.html)
- [SQLite window functions](https://www.sqlite.org/windowfunctions.html)
- [pandas read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Requests quickstart: status, timeouts and JSON](https://requests.readthedocs.io/en/latest/user/quickstart/)
