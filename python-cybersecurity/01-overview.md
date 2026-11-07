# 01 — Python and Cybersecurity

## What is Python?
Python is a readable, general-purpose programming language used for automation, data processing, scripting and testing. Python is a tool, not a substitute for cybersecurity fundamentals. A badly written script can expose secrets, destroy data or produce misleading results.

## Where defenders use it
- SOC: parse alert exports, normalize fields and summarize events.
- Incident response: collect approved system details, calculate hashes and build timelines.
- Threat intelligence: compare supplied indicators of compromise (IOCs) with logs.
- Network defense: inspect lab connections and automate authorized checks.
- Application security: test input validation in intentionally vulnerable local labs.
- Cloud and infrastructure: call approved APIs and validate configurations.
- Forensics support: organize metadata and calculate hashes while preserving originals.

## Key vocabulary
- Automation: using code for repeatable tasks.
- IOC: an indicator that may relate to malicious activity, such as a hash or domain.
- False positive: benign activity incorrectly flagged.
- False negative: a real issue that is not detected.
- Telemetry: collected information about system or network activity.

## Workflow
1. Define the objective and authorized scope.
2. Identify inputs, outputs and possible side effects.
3. Write a small, readable program.
4. Test with synthetic or copied lab data.
5. Validate input and handle errors.
6. Verify output independently.
7. Document limitations and clean up.
8. Publish only sanitized code and evidence.

## First program
~~~python
print("Python for Cybersecurity")
print("Learning defensive automation")
~~~

Run with python hello.py, or python3 hello.py on systems that use that command.

## Check yourself
Why must a script's output be verified? Name three defensive tasks Python can help with.
