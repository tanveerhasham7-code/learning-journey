# 14 — Network Troubleshooting Method

## Use a repeatable process
1. Define the problem: who is affected, what fails, when it began and what changed.
2. Establish scope: one device, one VLAN, one site or many?
3. Check physical and link status.
4. Verify IP address, subnet mask, gateway and DNS.
5. Test progressively: loopback → own interface → gateway → remote IP → hostname.
6. Check routes, VLANs, ACLs and firewall rules.
7. Verify the destination service is listening.
8. Capture packets and inspect where communication stops.
9. Make one controlled change at a time.
10. Document cause, fix, validation and prevention.

## Common problems
- Wrong subnet mask: hosts may incorrectly decide a destination is local.
- Missing default gateway: local communication works but remote networks fail.
- Duplicate IP: intermittent or conflicting connectivity.
- Wrong VLAN/access port: host joins the wrong broadcast domain.
- Trunk mismatch: VLAN traffic fails between switches/devices.
- Missing route: router does not know where to forward packets.
- DNS failure: IP connectivity works but hostname resolution fails.
- Firewall block: packets or sessions are denied by policy.
- MTU issue: small packets work but larger transfers fail.

## Useful tests
- `ping` tests reachability (ICMP may be blocked).
- `traceroute`/`tracert` helps reveal path behavior.
- `nslookup`/`dig` tests DNS.
- `ip route`/`route print` checks routing.
- `ss`/`netstat` checks sockets.
- Wireshark/tcpdump provides packet-level evidence.

## Incident response mindset
Preserve relevant logs and timestamps, avoid changing evidence unnecessarily, record actions, escalate according to policy and do not investigate beyond your authorization.
