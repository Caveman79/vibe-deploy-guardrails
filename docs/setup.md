# Setup and first aid

## Before you begin

A terminal runs commands; a text editor changes files; a browser displays the app.
Jupyter combines editing and execution in cells. Here you save `.py` files and run them
from the terminal so another person or a CI service can repeat the same steps.

Install Python 3.12 or newer from [Python](https://www.python.org/downloads/), Git from
[Git](https://git-scm.com/downloads), and a text editor you are comfortable with.
Docker is optional until Lab 06: use the [Docker installation guide](https://docs.docker.com/get-started/get-docker/).
Check its licensing terms for your organization. GitHub is optional until the review/CI exercises.

All command blocks assume **Bash**. On Windows, use a WSL terminal for the full course;
Docker must be available in that environment. Native PowerShell can run the three quickstart
Python commands using `py -3` instead of `python3`, but environment assignment and shell
scripts in later labs require Bash. Do not paste Bash blocks into a Jupyter cell.

1. Extract the ZIP and open its `vibe-deploy-guardrails` directory in your editor.
2. Open a terminal in that directory. `pwd` shows where you are; `ls` should show `README.md`.
3. Run `python3 --version` and `git --version`.
4. Follow the README quickstart. No package installation is needed.

For later experiments with packages, isolate them:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Use `deactivate` to leave the environment. A virtual environment isolates Python packages;
it is not a security sandbox. The `.env.example` file documents settings but does not
load them. Commands in the labs set configuration explicitly.

## If a command fails

| Symptom | Check and recovery |
| --- | --- |
| `python3: command not found` | Install Python, reopen the terminal, check the version. |
| `No module named guardrails` | Run from the folder containing `guardrails/` and `README.md`. |
| `Address already in use` | Stop your earlier app with Ctrl+C, or use `--port 8001` and update the browser/smoke URL. |
| Browser cannot connect | Keep the app terminal running and use `http`, not `https`. Check the port. |
| `PermissionError` creating a socket | Your sandbox may block local networking. Run on your own machine or an approved environment; do not disable tests to claim a pass. |
| Docker unavailable | Complete Labs 00–05 first. Install/start Docker before container labs. |
| Git asks for identity | Set your chosen commit name and email locally in this repository; a GitHub no-reply email can preserve privacy. |
| CI is red but local tests pass | Read the failing job: the container or security scan may be failing independently. |
| GitHub review cannot be approved by you | Independent approval requires a second person. Use the solo mode described in Lab 02. |

Never paste a real API key, password, or private operational data into an issue or an AI prompt.
