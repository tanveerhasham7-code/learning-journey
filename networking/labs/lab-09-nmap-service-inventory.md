# Lab 09 — Nmap Service Inventory

## Objective
Use Nmap from Kali Linux to discover an intentionally vulnerable Metasploitable 2 VM, identify its listening TCP ports and service versions, save scan output, and record defensive recommendations.

## Scope and authorization
- Scanner: Kali Linux VM
- Target: Metasploitable 2 VM owned and controlled for this lab
- Virtualization: VMware Workstation
- Network: isolated Host-only virtual network
- Kali address: `192.168.254.128/24`
- Target address: `192.168.254.129/24`
- Scope: one lab host only (`192.168.254.129`)
- Nmap version shown in evidence: 7.99
- Scan date shown in terminal: 16 November 2026

The scans were limited to the user's own Metasploitable 2 lab VM. No public, campus, or third-party systems were included.

## Lab setup and connectivity
Both VMs were configured to use the same Host-only network. The target's `eth0` address was confirmed as `192.168.254.129`; Kali's active `eth0` address was `192.168.254.128/24`.

A connectivity test was successful:
```bash
ping -c 4 192.168.254.129
```
Observed result: 4 packets transmitted, 4 received, 0% packet loss.

![Metasploitable 2 target IP configuration](screenshots/lab-09/Screenshot%202026-11-16%20214933.png)

![Kali Linux IP configuration](screenshots/lab-09/Screenshot%202026-11-16%20214959.png)

![Successful ping from Kali to Metasploitable 2](screenshots/lab-09/Screenshot%202026-11-16%20215135.png)

## Nmap commands performed

### 1. Verify Nmap installation
```bash
nmap --version
```
Nmap 7.99 was displayed.

### 2. Discover the target host
```bash
nmap -sn 192.168.254.129
```
Nmap reported that the host was up.

### 3. Basic TCP port scan
```bash
nmap 192.168.254.129
```
The scan reported 23 open TCP ports and 977 closed TCP ports in the default 1,000-port scan.

![Nmap version, host discovery and basic port scan](screenshots/lab-09/Screenshot%202026-11-16%20215352.png)

### 4. Service and version detection
```bash
nmap -sV 192.168.254.129
```
Nmap identified services and returned version information for many of the open ports.

![Nmap service and version detection](screenshots/lab-09/Screenshot%202026-11-16%20215558.png)

### 5. Save scan output in three formats
```bash
nmap -sV -oA lab-09-nmap-scan 192.168.254.129
```
The `-oA` option saved normal, XML, and grepable output:
- `lab-09-nmap-scan.nmap`
- `lab-09-nmap-scan.xml`
- `lab-09-nmap-scan.gnmap`

![Saved Nmap output files and scan results](screenshots/lab-09/Screenshot%202026-11-16%20220023.png)

The normal output file was then reviewed:
```bash
cat lab-09-nmap-scan.nmap
```

![Contents of the saved Nmap scan report](screenshots/lab-09/Screenshot%202026-11-16%20220155.png)

### 6. Run default scripts with service detection and save detailed output
```bash
nmap -sC -sV -oA lab-09-detailed-scan 192.168.254.129
```
This combined Nmap's default scripts with service/version detection and saved the results in three formats. The visible script output included anonymous FTP access being allowed and FTP control/data connections using plain text. This is a finding for the deliberately vulnerable training VM, not a recommendation for production systems.

![Default-script and service scan output](screenshots/lab-09/Screenshot%202026-11-16%20221108.png)

### 7. Extract TCP port lines from the detailed report
```bash
grep -E '^[0-9]+/tcp' lab-09-detailed-scan.nmap
```

![Extracted TCP ports, states and service/version details](screenshots/lab-09/Screenshot%202026-11-16%20221146.png)

## Observed open TCP services

The service/version scan and saved report showed the following open TCP ports:

| Port | Service identified | Version / detail observed |
|---:|---|---|
| 21 | FTP | vsftpd 2.3.4 |
| 22 | SSH | OpenSSH 4.7p1 Debian Ubuntu1 |
| 23 | Telnet | Linux telnetd |
| 25 | SMTP | Postfix smtpd |
| 53 | DNS | ISC BIND 9.4.2 |
| 80 | HTTP | Apache httpd 2.2.8 (Ubuntu) DAV/2 |
| 111 | rpcbind | RPC #100000 |
| 139 | NetBIOS-SSN | Samba smbd 3.x–4.x |
| 445 | Microsoft-DS / SMB | Samba smbd 3.0.20-Debian |
| 512 | exec | netkit-rsh rexecd |
| 513 | login | Service identified as login? |
| 514 | shell | Netkit rshd |
| 1099 | Java RMI | GNU Classpath grmiregistry |
| 1524 | bindshell | Metasploitable root shell |
| 2049 | NFS | NFS service |
| 2121 | FTP | ProFTPD 1.3.1 |
| 3306 | MySQL | MySQL 5.0.51a-3ubuntu5 |
| 5432 | PostgreSQL | PostgreSQL 8.3.0–8.3.7 |
| 5900 | VNC | VNC protocol 3.3 |
| 6000 | X11 | Access denied in service detection output |
| 6667 | IRC | UnrealIRCd |
| 8009 | AJP13 | Apache Jserv Protocol v1.3 |
| 8180 | HTTP | Apache Tomcat/Coyote JSP engine 1.1 |

Nmap service/version detection is a fingerprint-based estimate. Confirm versions and whether a service is actually required from the target's own configuration before making operational decisions.

## Security observations and defensive recommendations

This deliberately vulnerable VM exposes many services at once. In a real environment, an administrator should:

1. **Remove unnecessary services:** disable FTP, Telnet, rsh/rexec, legacy remote login, unused database listeners, demo applications, and other services that are not required.
2. **Replace insecure remote access:** do not use Telnet or rsh; use properly configured SSH with strong authentication and restricted management access.
3. **Protect file transfer:** avoid anonymous FTP and plaintext credentials; use SFTP or another approved encrypted transfer method.
4. **Restrict database access:** allow MySQL and PostgreSQL only from approved application or administration hosts; never expose them to every network segment.
5. **Harden SMB/NFS/RPC:** restrict file-sharing and RPC services to trusted hosts, remove legacy protocol support, and apply supported security updates.
6. **Review web and Java services:** patch supported web servers and application containers, remove unused applications, and restrict management interfaces.
7. **Apply firewall rules and segmentation:** permit only business-required ports between defined network zones; deny unnecessary inbound access by default.
8. **Monitor and retest:** review service logs, monitor authentication failures, patch systems, and repeat an authorized scan after changes.

No services were disabled or reconfigured during this inventory exercise. The recommendations are proposed defensive actions, not completed remediation.

## Outcome
- [x] Confirmed Kali and target VM addresses
- [x] Verified connectivity (0% packet loss)
- [x] Confirmed Nmap installation
- [x] Discovered the target host
- [x] Identified open TCP ports and service versions
- [x] Saved normal, XML and grepable scan outputs on Kali
- [x] Ran default scripts with service detection
- [x] Reviewed the extracted port list
- [x] Recorded security observations and defensive recommendations
- [ ] Applied remediation and performed a post-remediation retest (not part of this inventory run)

**Lab status: Completed — Nmap inventory and security review documented.** Remediation and retesting remain future work.

## What I learned
I learned how to verify Nmap, discover a live host, scan TCP ports, identify service versions, save scan output in multiple formats, and use the results to build a basic defensive service inventory.

## Evidence
All nine screenshots are embedded above and stored in [the Lab 09 screenshots folder](screenshots/lab-09/).
