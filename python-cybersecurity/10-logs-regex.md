# 10 — Regular Expressions and Log Analysis

Regex describes text patterns. Python's re module can search, split and validate text. Use raw strings for patterns.

~~~python
import re

pattern = re.compile(r"\b(4\d{2}|5\d{2})\b")
print(pattern.findall("HTTP codes: 200, 401, 503"))
~~~

## Named groups
~~~python
line = "2026-01-01 10:00:00 user=lab_user action=login_failed"
match = re.search(r"user=(?P<user>\S+) action=(?P<action>\S+)", line)
if match:
    print(match.group("user"), match.group("action"))
~~~

For stable CSV or JSON formats, use the appropriate parser instead of regex. Complex regex can be hard to maintain and may perform poorly.

## Log-analysis workflow
Identify source and format, preserve originals, parse a working copy, normalize timestamps carefully, group events, compare with baseline and surrounding activity, then document limitations.

A cluster of failed logins may result from a forgotten password or misconfigured service as well as an attack. Investigate context; do not classify by count alone.

## Exercise
Create ten synthetic log lines. Extract usernames and actions, count failed logins and handle malformed lines. Explain false-positive possibilities.
