# 13 — Nmap in an Authorized Lab

## Purpose
Nmap discovers hosts and services on networks you are authorized to assess. It is useful for building an asset inventory and checking whether unnecessary services are exposed.

## Prepare a safe target
Use a VM you own on a host-only/internal lab network. Example target: 192.168.56.20. Confirm the address from the VM console before scanning.

## Basic commands
```bash
# Check Nmap version
nmap --version

# Ping/host discovery against one lab host
nmap -sn 192.168.56.20

# Scan common TCP ports on your lab host
nmap 192.168.56.20

# Identify service versions on selected common ports
nmap -sV -p 22,80,443 192.168.56.20

# Save results in normal, XML and grepable formats
nmap -oA lab-host-scan 192.168.56.20
```

Only use these examples against your own isolated target or a target for which you have explicit written authorization. Do not scan public IP ranges, campus networks or third-party systems without permission.

## Interpret results
- open: a service accepted connections.
- closed: host responded but no application is listening on that port.
- filtered: probes could not determine whether the port is open, often due to filtering.
- service/version: an estimate; verify with system configuration.

## Defensive follow-up
For every open port, ask:
1. Is the service required?
2. Is it patched and securely configured?
3. Should access be restricted to a management subnet?
4. Is authentication strong and encrypted?
5. Are logs monitored?

## Report template
- Scope/authorization:
- Date/time:
- Scanner host:
- Target lab host:
- Command used:
- Open ports/services:
- Risk observations:
- Recommended remediation:
- Retest result:
