# 09 — Network Discovery and Nmap (Authorized Lab Only)

## 1. Purpose
Asset discovery helps defenders identify live hosts, exposed services and unexpected changes. Nmap is a network exploration and security auditing tool. It can generate traffic that triggers alerts or affects fragile devices, so only use it against systems you own or have written permission to assess.

## 2. Start with scope
Before a scan, write down:
- Authorized IP range or host
- Approved scan window
- Allowed scan types and rate
- Systems excluded from testing
- Contact and stop condition
- How results will be stored and protected

Do not scan public IP ranges, university/work networks or neighbors merely because they respond.

## 3. Safe lab examples
Against a host-only VM you control:
```bash
# Confirm the tool is installed
nmap --version

# Scan one explicitly authorized lab host for common TCP ports
nmap <LAB_VM_IP>

# Identify service/version information on that same lab host
nmap -sV <LAB_VM_IP>

# Save normal and XML output for your own lab report
nmap -oN lab-scan.txt -oX lab-scan.xml <LAB_VM_IP>
```
Replace the placeholder only with your own lab VM address. Do not copy these commands to an unknown target.

## 4. Understand scan output
- **Host discovery:** whether a host appears reachable using the selected probes.
- **Port states:** open, closed, filtered, and other states depending on scan method.
- **Service detection:** probes attempt to identify service and version; results may be imperfect.
- **OS detection:** an estimate based on network responses, not guaranteed identification.

“Filtered” does not mean the port is closed. “Open” does not automatically mean vulnerable.

## 5. Defensive interpretation
For every discovered service ask:
- Is the service required?
- Is it exposed to the correct zones only?
- Is the software supported and patched?
- Is authentication strong?
- Is management access restricted?
- Is the service logged and monitored?
- Does the asset owner recognize it?

## 6. Baseline and change detection
Keep an approved inventory and compare new scan results against it. Unexpected services or new hosts should be validated with asset owners. A scan is a snapshot and may miss intermittent, filtered or sleeping devices.

## Practical lab
Create two Linux VMs on an internal virtual network. Record their addresses, scan only the second VM, identify one intentionally enabled service, then close or firewall that service and repeat the scan. Explain what changed and what the scan cannot prove.

## Ethics and safety
No stealth, evasion, denial-of-service, exploitation or credential guessing is required for this learning module. Keep scan intensity low and stop if a system behaves unexpectedly.
