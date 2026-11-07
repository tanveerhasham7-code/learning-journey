# 18 — Python for Cybersecurity: 16 Practical Labs

Perform exercises only on your own computer or isolated lab VMs. Use synthetic data unless explicitly authorized. Instructions are not proof that labs have been performed.

1. **Python setup:** install Python 3, create a project and virtual environment, run hello.py and document versions.
2. **Input validation:** accept a port number and reject letters, negatives, zero and values above 65535.
3. **Event counters:** count synthetic login events by type and username; explain why counts are not proof of attack.
4. **Functions/modules:** build a helper module with a port validator and username normalizer; import and test it.
5. **File handling:** read a synthetic log, handle missing-file errors and write a separate summary.
6. **SHA-256 integrity:** hash a test file, change a copy and compare digests.
7. **CSV/JSON:** parse synthetic events, count types and export a JSON summary.
8. **Regex parser:** extract fields from sample logs and count malformed lines.
9. **Failed-login triage:** summarize failures by account and time window as review candidates, not confirmed attacks.
10. **IOC matcher:** compare synthetic indicators with synthetic events and explain false positives.
11. **Localhost sockets:** create a server bound only to 127.0.0.1 and a client; exchange one message and stop the server.
12. **HTTP request:** send one GET to example.com with a timeout; record status and content type.
13. **System inventory:** collect OS name, Python version and hostname from your own lab; sanitize output.
14. **Integrity manifest:** hash a dedicated test folder and report added, changed and removed files.
15. **Unit testing:** test valid, invalid, missing and malformed inputs.
16. **Mini triage tool:** combine file hashing, synthetic log parsing and IOC matching into a read-only report.

## Evidence for each lab
- Screenshot of code or command being run.
- Screenshot or text output showing the actual result.
- Short explanation of what the result means.
- Errors encountered and how they were resolved.
- Confirmation that data is synthetic or authorized and sanitized.

Never publish credentials, API tokens, private keys, raw production logs, personal data or sensitive IP addresses.
