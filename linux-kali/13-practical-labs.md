# 13 — Linux Administration & Kali Practical Lab Workbook

**Run these labs only on VMs and networks you own or are authorized to test. Do not mark a lab complete until you have executed it and saved evidence.**

## Lab 1 — Linux system identification
Objective: identify OS, kernel, user and uptime.
```bash
cat /etc/os-release
uname -a
whoami
id
uptime
```
Evidence: terminal screenshot and explanation of kernel versus distribution.

## Lab 2 — Files and directories
Create a project folder, three files, copy and rename one, search for a phrase with grep, and inspect metadata with stat. Evidence: commands and final directory listing.

## Lab 3 — Users and groups
Create two test users and a shared group. Create a shared directory, assign group ownership and configure permissions. Log in as each test user and verify access. Evidence: id, getent group, ls -ld and access results. Remove test accounts when finished if appropriate.

## Lab 4 — Permissions
Create a file and test modes 600, 640 and 644. Explain which users can read/write it. Restore a sensible final mode. Never change permissions on system files.

## Lab 5 — Processes and services
Run a harmless sleep process, identify it with ps/pgrep, terminate gracefully and inspect a systemd service. Record process ID, owner and service state.

## Lab 6 — Package management
Update package metadata, inspect a small package, install it, verify it, then remove it. Explain why apt update differs from apt upgrade.

## Lab 7 — Linux network diagnostics
On two lab VMs, check interface addresses and routes, ping the other VM, inspect the neighbor table, resolve a domain if DNS is intentionally available, and inspect listening sockets. Save the IP plan and a simple diagram.

## Lab 8 — Bash inventory script
Write a script that records hostname, OS release, kernel, date, IP addresses, routes, disk usage and listening sockets. Run as a standard user and review the report for sensitive information before publishing.

## Lab 9 — Log analysis
Generate a few failed logins against your own SSH lab VM (if configured). Inspect journal/authentication logs, note timestamp, username and source. Compare with a successful login. Do not test external hosts.

## Lab 10 — Firewall basics
In a disposable VM with console access, inspect UFW status, allow the required lab management service, enable UFW and verify allowed/blocked behavior. Have a snapshot/rollback plan before changing firewall policy.

## Lab 11 — Kali-to-Ubuntu lab connection
Set Kali and Ubuntu VMs to the same Host-only or Internal Network. Example addresses:
- Kali: 192.168.56.20/24
- Ubuntu target: 192.168.56.30/24

Check ip -br addr, ping between VMs and inspect ARP/neighbor tables. A gateway is not required for communication within this same subnet.

## Lab 12 — Nmap authorized inventory
From Kali, scan only the Ubuntu target you own:
```bash
nmap -sn 192.168.56.30
nmap -sV 192.168.56.30
```
Record open ports and service versions. Confirm services from the Ubuntu VM itself. Recommend disabling or restricting unnecessary services.

## Lab 13 — Wireshark packet analysis
Capture your own ping and DNS query. Identify source/destination MAC and IP, protocol, ports where applicable, and request/response behavior. Save a sanitized capture only if it contains no private data.

## Lab 14 — Final project: Secure a Linux server
Scenario: you are responsible for a small Ubuntu server used by a fictional organization.

Deliverables:
1. Network diagram and IP address plan.
2. OS/kernel and package inventory.
3. Standard admin user and least-privilege explanation.
4. Permissions review for a project directory.
5. Running service and listening-port inventory.
6. Firewall policy and verification.
7. SSH configuration review and safe validation.
8. Authentication/system log review.
9. Kali-based authorized service inventory.
10. Before/after hardening comparison.
11. Findings, risk, remediation and retest report.

Report structure: executive summary, scope and authorization, environment/topology, methodology, findings/evidence, remediation, retest results, limitations and lessons learned.

## Evidence template
- Lab number/title:
- Date:
- Objective:
- VM/tool versions:
- Network mode and IP plan:
- Commands/configuration:
- Expected result:
- Actual result:
- Screenshot/file names (sanitized):
- Error and troubleshooting:
- Security lesson:
- Status: Not started / In progress / Completed
