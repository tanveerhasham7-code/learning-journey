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
Evidence: [completed Lab 1 report with three embedded screenshots](lab/lab-01-system-identification.md). **Status: Completed (17 November 2026).**

## Lab 2 — Files and directories
Create a practice folder and three files; write/read content; copy, rename, move and delete files; create a subdirectory; use `less` and `find`; inspect the final tree and disk usage with `pwd`, `ls -R` and `du -sh`. Evidence: [completed Lab 2 report](lab/lab-02-files-and-directories.md). **Status: Completed (17 November 2026; learner-confirmed command execution, no screenshots).**

## Lab 3 — Users and groups
Create two temporary users and a shared group; configure a group-owned `2770` setgid directory; verify both users can create files; inspect ownership; then remove the test users, group and directory. Evidence: [completed Lab 3 report](lab/lab-03-users-and-groups.md). **Status: Completed (18 November 2026; learner-confirmed command execution, no screenshots).**

## Lab 4 — Permissions
Create a file in a dedicated home-directory practice folder; test modes `600`, `640` and `644`; inspect each with `stat`; restore mode `600`; then clean up. Reference: [Lab 4 permissions procedure](lab/lab-04-permissions.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 5 — Processes and services
Start a harmless `sleep 300` process; identify its PID, owner and state with `ps` and `pgrep`; terminate it gracefully with `kill -TERM`; verify it ended; inspect the actual state of NetworkManager using `systemctl status`. Reference: [Lab 5 processes and services procedure](lab/lab-05-processes-and-services.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 6 — Package management
Refresh package metadata with `sudo apt update`; inspect the `tree` package using `apt show`; install it with `sudo apt install tree`; verify using `tree --version` and `dpkg -s`; remove it with `sudo apt remove tree`; explain the difference between `apt update` and `apt upgrade`. Reference: [Lab 6 package management procedure](lab/lab-06-package-management.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 7 — Linux network diagnostics
Connect owned Kali and Ubuntu VMs to the same Host-only or Internal Network. Record actual interface addresses and routes; ping Ubuntu from Kali; inspect `ip neigh`; test DNS with `getent hosts` or `nslookup` when a resolver is available; inspect listening sockets with `ss -tuln`; complete an IP plan and network diagram. Reference: [Lab 7 network diagnostics procedure](lab/lab-07-network-diagnostics.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 8 — Bash inventory script
Create `system-inventory.sh` to collect hostname, date, OS release, kernel, current user, interface addresses, routes, disk usage and listening TCP/UDP sockets. Run as a normal user, inspect the timestamped report, and redact sensitive details before sharing. Reference: [Lab 8 Bash inventory script procedure](lab/lab-08-bash-inventory-script.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 9 — Log analysis
Inspect authentication events on your own Linux lab VM using `journalctl` and, if present, `/var/log/auth.log`. Identify failed and successful SSH authentication messages, timestamps, usernames and source addresses where recorded. Generate at most one controlled failed attempt only if SSH is already safely configured; otherwise analyze existing logs or use the clearly labeled fictional examples in the guide. Never test external systems. Reference: [Lab 9 authentication log analysis procedure](lab/lab-09-log-analysis.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 10 — Firewall basics
Inspect UFW status and existing rules; on a disposable VM with console access, apply a reviewed default policy, add only a necessary narrowly scoped inbound rule, enable UFW safely, and verify active rules. Include a snapshot/console rollback plan; do not test external systems. Reference: [Lab 10 UFW firewall basics procedure](lab/lab-10-firewall-basics.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 11 — Kali-to-Ubuntu lab connection
Connect both owned VMs to the same isolated Host-only network; inspect actual interface addresses and routes; verify same-subnet addressing; test ping in both directions; and inspect ARP/neighbor tables. Example IPs are illustrative only. Reference: [Lab 11 Kali-to-Ubuntu connection procedure](lab/lab-11-kali-to-ubuntu-connection.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 12 — Nmap authorized inventory
From Kali, scan only your own Ubuntu VM on the isolated lab network. Confirm its actual IP, check reachability, run host discovery and TCP service/version detection, verify listening services locally on Ubuntu, and document evidence-based hardening recommendations. Example IPs are not assumed to match your network. Reference: [Lab 12 Nmap authorized inventory procedure](lab/lab-12-nmap-authorized-inventory.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 13 — Wireshark packet analysis
Capture and analyze your own ICMP ping and DNS lookup on the isolated lab network. Identify Ethernet/IP addresses, protocols, ports where applicable, and request/response behavior. Save only reviewed, sanitized evidence. [Detailed Lab 13 guide](lab/lab-13-wireshark-packet-analysis.md). **Status: Reference prepared — learner execution and evidence pending.**

## Lab 14 — Final project: Secure a Linux server

Capstone project: assess and harden your own isolated Ubuntu Server VM using Kali as the authorized assessment workstation. Establish a baseline, review accounts and permissions, inventory services, review firewall and SSH safely, inspect logs, perform a single-host Nmap inventory, document evidence-based findings, apply justified remediation, and retest.

**Detailed guide:** [Lab 14 — Secure Linux Server Project](lab/lab-14-secure-linux-server-project.md).

**Status: Project blueprint prepared — implementation and evidence pending.** Do not mark complete until actual VM checks, remediation and retesting are documented.

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
