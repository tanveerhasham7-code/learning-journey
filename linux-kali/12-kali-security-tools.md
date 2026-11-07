# 12 — Kali Security Tools: Student-Level Overview

This guide explains common tools and how to start safely. Tool availability and exact syntax can change; consult each tool's official documentation.

## Nmap — network discovery and service inventory
Purpose: discover hosts and identify exposed services on an authorized scope.
```bash
nmap -sn 192.168.56.0/24
nmap -sV 192.168.56.30
```
Use only against your isolated lab subnet or explicitly authorized targets. Record scope, time, command and findings. Avoid aggressive scripts or high-rate scans until you understand impact and have approval.

## Wireshark and tcpdump — packet analysis
Wireshark provides a graphical packet analyzer; tcpdump is a command-line capture tool.
```bash
sudo tcpdump -i any -nn host 192.168.56.30
```
Capture only your own lab traffic. Useful Wireshark display filters include dns, arp, icmp and tcp. Protect capture files because they may contain private data.

## Burp Suite Community — web application testing
Burp Suite can intercept and inspect HTTP(S) requests between a browser and a test application. Use a deliberately vulnerable local training app or an application you own. Configure a separate lab browser profile. Never intercept other people's sessions.

## OWASP ZAP — web application security testing
ZAP is an open-source web application testing proxy. Begin with passive observation and a local training application. Active scanning sends test requests and must only be used where authorized.

## Metasploit Framework — controlled exploitation education
Metasploit supports security testing and exploit research. Study modules, payload concepts, sessions and reporting in an intentionally vulnerable isolated lab. Never run exploit modules against public systems or networks without explicit authorization.

## John the Ripper — password auditing
Password-auditing tools help assess password strength using hashes you are authorized to handle. Practice with sample hashes generated for your own lab. Do not collect or crack other people's password hashes.

## Gobuster and directory discovery
Directory discovery tools test paths on a web server. Use only a local training target or an authorized scope, with conservative request rates. Avoid scanning public websites without permission.

## Tool selection mindset
Before using any tool, answer:
1. What is the objective?
2. What target is in scope?
3. Do I have permission?
4. What is the expected impact?
5. What evidence will I collect?
6. How will I stop or roll back?
7. How will I report results responsibly?

## Professional workflow
Understand → define scope → obtain permission → prepare lab → test minimally → validate findings → document evidence → recommend remediation → retest.

A tool result is not automatically a confirmed vulnerability. Verify manually and explain limitations.
