# Python for Cybersecurity

A defensive Python notebook for cybersecurity students, covering programming foundations, automation, log analysis, networking, integrity checking, testing and practical labs.

> These notes and sample scripts are learning material, not proof that the labs have been performed. Mark a lab complete only after you run it, understand the result and add your own sanitized evidence.

## Learning outcomes
- Write Python programs with variables, conditions, loops, functions and data structures.
- Handle files, exceptions, modules, packages and virtual environments.
- Parse text, CSV, JSON and logs.
- Use operating-system information, command-line arguments and subprocess safely.
- Understand sockets, DNS, TCP/UDP, HTTP and APIs.
- Apply SHA-256 and HMAC correctly; understand password-storage principles.
- Build defensive tools for integrity checks, event summaries and IOC matching.
- Test, document and safely maintain scripts.

## Chapters
1. [Python and cybersecurity overview](01-overview.md)
2. [Setup and environment](02-setup.md)
3. [Syntax, variables and data types](03-basics.md)
4. [Conditions and loops](04-control-flow.md)
5. [Strings and data structures](05-data-structures.md)
6. [Functions and modules](06-functions.md)
7. [Files, paths and exceptions](07-files.md)
8. [Packages, pip and virtual environments](08-packages.md)
9. [CLI and subprocess](09-cli.md)
10. [Regex and log analysis](10-logs-regex.md)
11. [CSV and JSON](11-structured-data.md)
12. [Operating-system automation](12-os-automation.md)
13. [Networking and sockets](13-networking.md)
14. [HTTP, APIs and web security](14-http-apis.md)
15. [Hashing and cryptography](15-crypto.md)
16. [Defensive automation patterns](16-defensive-automation.md)
17. [Testing, debugging and quality](17-testing.md)
18. [16 practical labs](18-practical-labs.md)
19. [Capstone project](19-capstone.md)
20. [Checklist and resources](20-resources.md)
21. [Lab report template](LAB-REPORT-TEMPLATE.md)

## Safe lab rules
Use your own computer or disposable VM. Network exercises must target localhost, your own lab VMs or systems for which you have explicit permission. Use synthetic logs and test files. Do not scan public ranges, brute-force accounts, deploy malware, bypass access controls or collect other people's data.

## Sample scripts
- scripts/file_integrity.py — SHA-256 manifest for a dedicated lab folder.
- scripts/log_summary.py — summarizes synthetic CSV events.
- scripts/ioc_matcher.py — matches supplied test indicators to synthetic events.
- scripts/system_inventory.py — collects minimal local system details.

Never publish passwords, API tokens, private keys, production logs, personal data or sensitive network details. Use the lab report template and add evidence only after doing the work.
