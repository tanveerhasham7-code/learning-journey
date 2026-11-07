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
- [ ] Users, groups and permissions
- [ ] Processes, services and packages
- [ ] Networking and firewall basics
- [ ] Bash scripting
- [ ] Logs and monitoring
- [ ] Linux hardening
- [ ] Kali setup and isolated lab connection
- [ ] Authorized security-tool labs
- [ ] Final secure-server project

## Final portfolio project: Secure a Linux server
Create a non-root administrator, update the OS, review services and listening ports, configure a host firewall, review SSH securely, inspect authentication logs, run an authorized service inventory from Kali, remediate unnecessary exposure and write a before/after report.
