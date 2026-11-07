# 13 — Network Troubleshooting Methodology

## 1. Work methodically
A good network engineer does not randomly change settings. Use a repeatable process:
1. Define the symptom, affected users, assets and start time.
2. Determine scope: one host, one VLAN, one site or all users?
3. Check recent changes and known outages.
4. Form a testable hypothesis.
5. Test from the closest layer outward.
6. Make one controlled change at a time.
7. Verify service restoration and monitor for recurrence.
8. Document root cause, evidence and prevention.

## 2. Layer-oriented checks
- **Physical:** power, cable, link lights, Wi-Fi signal, interface errors.
- **Data link:** VLAN membership, trunk state, MAC learning, STP state.
- **Network:** IP address, mask/prefix, gateway, routes, ARP/NDP, packet loss.
- **Transport:** TCP/UDP reachability, ports, resets, retransmissions.
- **Application:** DNS, certificates, service status, proxy and application logs.

## 3. Useful commands
Linux:
```bash
ip address
ip route
ip neigh
ping -c 4 <lab-address>
traceroute <lab-address>
ss -tulpen
resolvectl status
dig <lab-domain>
```
Windows:
```powershell
ipconfig /all
route print
arp -a
ping <lab-address>
tracert <lab-address>
Test-NetConnection <lab-host> -Port <lab-port>
nslookup <lab-domain>
```
Use placeholders for systems you own or are authorized to troubleshoot.

## 4. Common symptoms
- Can ping gateway but not server: inspect routing, ACL/firewall and destination service.
- Can reach IP but not name: inspect DNS resolver, record and search suffix.
- One VLAN fails: inspect access VLAN, trunk allowed list, SVI/gateway and DHCP scope.
- Intermittent slowness: inspect loss, latency, interface errors, congestion, wireless interference and endpoint load.
- Only one application fails: inspect listener, certificate, proxy, application logs and required dependencies.

## 5. Security-aware troubleshooting
Preserve logs before making changes. Avoid disabling firewalls as a first step. If compromise is suspected, follow incident response procedures and coordinate containment with the owner. Do not reboot or wipe a potentially compromised device before evidence requirements are considered.

## Practical exercise
Use an intentionally misconfigured simulator network: wrong VLAN, wrong gateway, missing route or incorrect DNS server. Diagnose one fault at a time, record the evidence that isolated it, fix it and verify the result.
