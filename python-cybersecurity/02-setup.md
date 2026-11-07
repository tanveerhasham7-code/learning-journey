# 02 — Setup and Development Environment

## Install and verify
Install a current supported Python 3 release from python.org or your operating system's trusted package manager.

~~~bash
python --version
~~~

On Linux/macOS, use python3 --version if that is the installed command. On Windows, the Python launcher may work as py --version.

## Editor and project
VS Code or another trusted editor can provide syntax highlighting, terminal and debugging. Create a project:

~~~bash
mkdir python-security-labs
cd python-security-labs
~~~

Create hello.py and run it. Keep source, sample data, output, tests and documentation separate.

## Virtual environment
A virtual environment isolates dependencies from system Python.

Windows PowerShell:
~~~powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
~~~

Linux/macOS:
~~~bash
python3 -m venv .venv
source .venv/bin/activate
python --version
~~~

Leave it with deactivate. If activation is blocked, read the error and follow platform documentation rather than weakening machine-wide policy.

## Suggested layout
~~~text
python-security-labs/
  .venv/
  data/
  output/
  scripts/
  tests/
  README.md
~~~

Do not commit .venv, secrets or private datasets. Add them to .gitignore.

## Exercise
Create the project, run hello.py, create and activate a virtual environment, then deactivate it. Record Python version and OS in your report. Sanitize local usernames and paths.
