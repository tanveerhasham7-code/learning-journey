# 10 — Practical Networking Labs (Beginner to Intermediate)

Complete each lab in order. Save topology files and screenshots in a separate `labs/` folder when possible.

## Lab 1 — Build a small LAN
**Topology:** 2 PCs → 1 switch.
- PC-A: 192.168.10.10/24
- PC-B: 192.168.10.20/24
Steps: connect both PCs, configure IPs, ping each other, inspect ARP table.
Expected: ping succeeds; switch learns source MAC addresses.

## Lab 2 — Connect two networks through a router
- LAN-A: 192.168.10.0/24, gateway 192.168.10.1
- LAN-B: 192.168.20.0/24, gateway 192.168.20.1
Configure router interfaces, bring them up, configure host gateways and test cross-network ping.
Expected: each host can reach the other subnet through the router.

## Lab 3 — VLAN segmentation
Create VLAN 10 (Admin) and VLAN 20 (Sales). Put separate access ports in each VLAN. Verify with `show vlan brief`. Confirm hosts in different VLANs cannot communicate without Layer 3 routing.

## Lab 4 — Trunk and inter-VLAN routing
Configure an 802.1Q trunk between switch and router or Layer 3 switch. Create gateways for VLAN 10 and 20. Test permitted communication. Add an ACL/policy to restrict one direction and verify the result.

## Lab 5 — DHCP
Configure a DHCP pool for a lab subnet. Exclude gateway/reserved addresses. Set clients to DHCP and inspect the assigned address, gateway and DNS. Capture the DORA sequence.

## Lab 6 — DNS
Use a local lab DNS service or a controlled test resolver. Query a known test hostname with `nslookup` or `dig`. Capture the request and response. Explain A, AAAA, CNAME and MX records.

## Lab 7 — Static routing
Connect two routers and two LANs. Configure routes in both directions. Inspect the routing table and use traceroute to understand the path.

## Lab 8 — Wireshark basics
Capture your own ping, DNS lookup and HTTP/HTTPS connection. Identify Ethernet, IP, TCP/UDP and application layers. Do not capture other people's traffic.

## Lab 9 — Nmap service inventory
Against a lab VM you own, run a limited discovery/port scan (see [Nmap lab](13-nmap-lab.md)). Identify listening services and recommend which should be disabled or restricted.

## Lab 10 — Network hardening review
Create a simple diagram with user, server, guest and management zones. Propose firewall rules, management access restrictions, logging and backup measures. Explain how segmentation reduces lateral movement.

## Final mini-project — Small Office Secure Network
Design:
- Admin VLAN 10 — 192.168.10.0/24
- Sales VLAN 20 — 192.168.20.0/24
- IT VLAN 30 — 192.168.30.0/24
- Guest VLAN 40 — 192.168.40.0/24
- Server VLAN 50 — 192.168.50.0/24

Deliverables:
1. Network topology diagram.
2. IP addressing/subnet table.
3. VLAN and trunk configuration.
4. Inter-VLAN routing.
5. ACL/firewall policy: guest cannot access internal networks; only required services are allowed.
6. DHCP/DNS design.
7. Wireshark evidence of selected traffic.
8. Nmap inventory of authorized lab hosts.
9. Troubleshooting notes and security recommendations.

Do not claim a lab is completed until you have personally run it and saved evidence.
