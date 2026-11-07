# 20 — Skills Checklist, Troubleshooting and Resources

## Skills checklist
- [ ] Install Python and create a virtual environment.
- [ ] Use variables, types, conditions and loops.
- [ ] Work with strings, lists, sets and dictionaries.
- [ ] Write functions and import modules.
- [ ] Read/write files and handle exceptions.
- [ ] Use pip and document dependencies.
- [ ] Build a CLI with argparse.
- [ ] Parse synthetic logs using CSV, JSON and regex.
- [ ] Collect minimal local system inventory.
- [ ] Explain TCP, UDP, DNS, ports and HTTP.
- [ ] Build a localhost-only socket exercise.
- [ ] Calculate SHA-256 and explain HMAC.
- [ ] Explain dedicated password hashing.
- [ ] Build IOC matching and test false positives.
- [ ] Complete the defensive triage capstone.

## Troubleshooting
Python not recognized: verify installation and PATH; on Windows try py --version.
ModuleNotFoundError: activate the correct environment and inspect python -m pip list.
PermissionError: check permissions; do not run as administrator by default.
UnicodeDecodeError: identify encoding; do not silently discard evidence bytes.
Connection refused: confirm the local server is running on the expected address and port.
Timeout: check connectivity and use bounded retries.
Unexpected output: inspect a sanitized sample and add tests.

## Official resources
- Python tutorial: https://docs.python.org/3/tutorial/
- Python library: https://docs.python.org/3/library/
- Python security warnings: https://docs.python.org/3/library/security_warnings.html
- Python Packaging Guide: https://packaging.python.org/
- Requests documentation: https://requests.readthedocs.io/
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- NIST Incident Handling Guide: https://csrc.nist.gov/pubs/sp/800/61/r2/final
- MITRE ATT&CK: https://attack.mitre.org/

A topic is complete only when you can explain it, write or modify a working example, run it in an authorized lab, interpret the result and document limitations.
