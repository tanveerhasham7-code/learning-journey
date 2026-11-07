# 09 — Command-Line Arguments and subprocess

## argparse
A command-line interface makes scripts repeatable. argparse provides help text and named options.

~~~python
import argparse

parser = argparse.ArgumentParser(description="Summarize a lab log")
parser.add_argument("--input", required=True, help="Path to sample log")
args = parser.parse_args()
print(f"Input selected: {args.input}")
~~~

Run with python tool.py --help. Validate that the selected file is inside the intended lab folder.

## subprocess
Use subprocess only for known local commands. Prefer an argument list, fixed executable and shell=False. Never build a shell command by concatenating untrusted input.

~~~python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True,
    check=False,
    timeout=10
)
print(result.stdout or result.stderr)
~~~

Check returncode, stdout and stderr. Set timeouts and handle missing executables. Do not execute commands found inside logs.

## Exercise
Build a CLI that accepts a synthetic log path and prints the number of lines. Handle missing files and invalid arguments.
