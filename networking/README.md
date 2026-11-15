# Networking for Cybersecurity — Learning & Practical Labs

A structured, beginner-to-intermediate networking notebook for a cybersecurity student. It combines concepts, commands, diagrams, lab build instructions, verification steps, and security observations.

## Learning order
1. [Networking foundations](01-networking-fundamentals.md)
2. [OSI and TCP/IP models](02-osi-tcpip-models.md)
3. [IPv4, subnetting and CIDR](03-ip-addressing-subnetting.md)
4. [Switching, VLANs and trunking](04-switching-vlans.md)
5. [Routing, static routes and dynamic routing](05-routing.md)
6. [Core services: ARP, DHCP, DNS, NAT](06-network-services.md)
7. [Protocols and ports](07-protocols-and-ports.md)
8. [Network security fundamentals](08-network-security.md)
9. [Practical lab setup](09-build-your-lab.md)
10. [Hands-on lab exercises](10-practical-labs.md)
11. [Linux and Windows commands](11-networking-commands.md)
12. [Wireshark packet analysis](12-wireshark.md)
13. [Nmap discovery in an authorized lab](13-nmap-lab.md)
14. [Troubleshooting methodology](14-troubleshooting.md)
15. [Cybersecurity networking checklist](15-cybersecurity-checklist.md)

## Practical labs completed / in progress

The following hands-on labs have their own detailed reports and screenshot evidence:

| Lab | Title | Status | Report | Screenshots |
|---|---|---|---|---|
| Lab 1 | Build and verify a basic LAN (2 PCs, 1 switch) | Completed; switch MAC-table check needs re-verification | [Open Lab 1 report](labs/lab-01-basic-lan.md) | [View Lab 1 screenshots](labs/screenshots/lab-01/) |
| Lab 2 | Connect two LANs through a Cisco 2911 router | Completed; bidirectional ping tested | [Open Lab 2 report](labs/lab-02-two-lans-router.md) | [View Lab 2 screenshots](labs/screenshots/lab-02/) |

[Open the complete Networking Labs index](labs/README.md) for the folder structure and all available lab reports.

## Recommended lab tools
- Cisco Packet Tracer: beginner-friendly switching, routing, VLAN, DHCP and ACL simulations.
- GNS3 or EVE-NG: more advanced network-device labs; images may require separate licensing.
- VirtualBox: isolated virtual machines for Linux/Windows host networking.
- Wireshark: packet capture and protocol analysis.
- Nmap: host and service discovery on systems you own or are explicitly authorized to test.

## Safe lab rules
Use private lab networks (for example 192.168.56.0/24 or 10.10.10.0/24), host-only/internal virtual networks where possible, and intentionally vulnerable targets only inside an isolated lab. Never scan, capture, disrupt, or access networks without permission. Do not bridge vulnerable machines directly to a public or campus network.

## How to document each lab
Record: objective, topology, device/VM names, IP plan, configuration, commands, expected result, actual result, screenshots (with secrets removed), troubleshooting, security lesson, and what you learned.

## Progress
- [ ] Complete fundamentals and OSI/TCP-IP
- [ ] Calculate IPv4 subnets confidently
- [ ] Build a small switched LAN
- [ ] Configure VLANs and inter-VLAN routing
- [ ] Configure static routing
- [ ] Observe DHCP, DNS, ARP and TCP handshakes
- [ ] Analyze captures in Wireshark
- [ ] Run a limited Nmap scan against lab targets
- [ ] Apply basic segmentation and access controls
- [ ] Write a final network-security lab report

This is a learning notebook, not a claim of professional certification or production-network experience.
