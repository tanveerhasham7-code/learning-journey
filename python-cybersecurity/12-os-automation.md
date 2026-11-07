# 12 — Operating-System Automation

The os module provides operating-system functions, platform reports system details and pathlib handles paths. Collect only information required for the task.

~~~python
import os
import platform
from pathlib import Path

print(platform.system(), platform.release())
print("Working directory:", Path.cwd())
print("Home directory exists:", Path.home().exists())
print("CPU count:", os.cpu_count())
~~~

## Environment variables
~~~python
import os
mode = os.getenv("APP_MODE", "lab")
print(mode)
~~~

Environment variables are not automatically a secure secret store. Processes and diagnostics may expose them. Never print all environment variables into a public report.

## Safe inventory
For your own lab, collect OS name, Python version and hostname. Avoid serial numbers, usernames, IP addresses and device identifiers in public evidence unless intentionally sanitized.

## Exercise
Write a script that reports OS name, Python version, hostname and the number of files in a dedicated test folder. Do not enumerate other users' files or the entire home directory.
