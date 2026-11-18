# Linux Administration & Kali Linux for Cybersecurity

**Portfolio learning track | Theory + practical labs | Beginner to intermediate**

This section documents the Linux skills a cybersecurity student should understand before using security tools: Linux architecture, terminal, filesystems, accounts, permissions, processes, services, packages, networking, Bash, logs, hardening, Kali Linux and authorized security-tool practice.

> Portfolio honesty: These are detailed study notes and lab instructions. Mark a lab complete only after you personally run it and add sanitized evidence.

## Learning outcomes
- Explain Linux distributions, kernel, shell, filesystem hierarchy and boot process.
- Manage files, users, groups, permissions, processes and services.
- Inspect packages, storage, networking, sockets and logs.
- Write basic Bash automation.
- Apply least privilege and basic Linux hardening.
- Set up Kali safely in a virtual lab and use tools only with authorization.
- Document lab results professionally.

## Contents
1. [Linux fundamentals](01-linux-fundamentals.md)
2. [Terminal and file operations](02-terminal-and-files.md)
3. [Filesystem and storage](03-filesystem-and-storage.md)
4. [Users, groups and permissions](04-users-groups-permissions.md)
5. [Processes and services](05-processes-and-services.md)
6. [Package management](06-package-management.md)
7. [Linux networking](07-linux-networking.md)
8. [Bash scripting](08-bash-scripting.md)
9. [Logs and monitoring](09-logs-monitoring.md)
10. [Linux hardening](10-linux-hardening.md)
11. [Kali Linux setup](11-kali-linux.md)
12. [Kali security tools](12-kali-security-tools.md)
13. [Practical lab workbook](13-practical-labs.md)
14. [Troubleshooting](14-troubleshooting.md)
15. [Skill checklist](15-skill-checklist.md)
16. [Glossary and resources](16-glossary-resources.md)
17. [Lab report template](LAB-REPORT-TEMPLATE.md)
18. [Example system inventory script](scripts/README.md)

## Suggested lab environment
Use VirtualBox or another hypervisor with an Ubuntu VM for administration and a Kali VM for security learning. Add a second Ubuntu VM as a target if your computer has enough resources. Prefer Host-only or Internal Network mode for isolated exercises. Do not bridge vulnerable targets to campus, workplace or public networks.

Example private lab addressing:
| VM | Address | Role |
|---|---|---|
| Ubuntu-Admin | 192.168.56.10/24 | Linux administration |
| Kali-Lab | 192.168.56.20/24 | Security workstation |
| Ubuntu-Target | 192.168.56.30/24 | Owned test server |

## Evidence standards
For each completed lab, save the objective, theory, topology, commands actually run, expected and actual output, sanitized screenshots, troubleshooting notes and security lesson. Never commit passwords, private keys, API tokens, cookies or sensitive logs.

## Progress
- [ ] Linux fundamentals and terminal
- [ ] Filesystem and storage
- [x] Users, groups and permissions (Labs 3–4 completed)
- [x] Processes, services and package management (Labs 5–6 completed)
- [x] Linux network diagnostics (Lab 7 completed); firewall basics completed (Lab 10)
- [x] Bash scripting (Lab 8 completed)
- [x] Logs and monitoring (Lab 9 completed)
- [ ] Linux hardening
- [x] Kali setup and isolated lab connection (Lab 11 completed)
- [x] Authorized security-tool labs (Labs 12–13 completed; further tool practice may continue)
- [x] Final secure-server project (Lab 14 learner-confirmed completed; evidence not supplied)


## Practical lab progress

- [x] [Lab 1 — Linux system identification](lab/lab-01-system-identification.md) — completed with three screenshot evidence images.
- [x] [Lab 2 — Files and directories](lab/lab-02-files-and-directories.md) — completed (17 November 2026; command-based report, no screenshots).
- [x] [Lab 3 — Users and groups](lab/lab-03-users-and-groups.md) — completed (18 November 2026; command-based report, no screenshots).
- [x] [Lab 4 — Linux file permissions](lab/lab-04-permissions.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 5 — Processes and services](lab/lab-05-processes-and-services.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 6 — Package management](lab/lab-06-package-management.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 7 — Network diagnostics](lab/lab-07-network-diagnostics.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 8 — Bash inventory script](lab/lab-08-bash-inventory-script.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 9 — Log analysis](lab/lab-09-log-analysis.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 10 — Firewall basics (UFW)](lab/lab-10-firewall-basics.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 11 — Kali-to-Ubuntu lab connection](lab/lab-11-kali-to-ubuntu-connection.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 12 — Nmap authorized inventory](lab/lab-12-nmap-authorized-inventory.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 13 — Wireshark packet analysis](lab/lab-13-wireshark-packet-analysis.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).
- [x] [Lab 14 — Final project: Secure a Linux server](lab/lab-14-secure-linux-server-project.md) — learner-confirmed practice completed (18 November 2026; no screenshots or terminal output supplied).

## Final portfolio project: Secure a Linux server
**Status: Learner-confirmed completed (18 November 2026).** The capstone practice is marked complete based on the learner's confirmation. No screenshots or terminal output were supplied, so specific server settings, scan findings, remediation and retest outcomes are not independently verified. See the [Lab 14 project report](lab/lab-14-secure-linux-server-project.md).
