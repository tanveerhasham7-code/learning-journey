# 06 — Functions and Modules

Functions group reusable logic and make programs easier to test.

~~~python
def is_valid_port(port):
    return isinstance(port, int) and 1 <= port <= 65535

print(is_valid_port(443))
print(is_valid_port(70000))
~~~

Use meaningful names, small responsibilities and documented assumptions. Parameters provide inputs; return sends a result back.

## Scope and arguments
Variables created inside a function are normally local. Pass required values as parameters instead of relying on hidden global state. Avoid mutable default values such as a list; use None and create a fresh list inside the function.

~~~python
def summarize_event(event_type, severity="medium"):
    return {"type": event_type, "severity": severity}
~~~

## Modules
A module is a Python file that can be imported. Useful standard-library modules include pathlib, hashlib, json, csv, re, logging, argparse and socket.

~~~python
from pathlib import Path
import hashlib
~~~

Use the main guard so reusable functions do not run automatically when imported:

~~~python
if __name__ == "__main__":
    print("Program started")
~~~

## Exercise
Create helpers.py with a port validator and username normalizer. Import them into main.py and test valid and invalid input. Separate reusable logic from input/output.
