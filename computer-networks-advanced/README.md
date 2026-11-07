# Computer Networks — Advanced Theory, Security Engineering & Practical Labs

A structured, hands-on learning track for a cybersecurity student. The aim is to understand how enterprise networks are designed, configured, monitored, troubleshot and defended.

> **Important:** These are learning instructions and lab resources. A lab is not complete merely because its guide is in this repository. Run it in your own isolated/authorized environment, record the actual result, and then add evidence.

## What you will learn
- Enterprise network architecture, Ethernet switching, VLANs, trunks, STP and link aggregation
- IPv4/IPv6 subnetting, routing, static routes and OSPF concepts
- ACLs, firewall policy, segmentation and least privilege
- DNS, DHCP, NTP and other infrastructure services
- Wireless security, VPNs, TLS and secure remote access
- Packet analysis with Wireshark, safe asset discovery with Nmap
- Network monitoring, logs, flow records, SNMP and incident triage
- Troubleshooting methodology and a secure enterprise capstone

## Recommended learning order
1. Read [Network architecture](01-network-architecture.md) and revise the foundations in the repository's [Networking section](../networking/README.md).
2. Study switching, routing and IPv6.
3. Configure access controls and infrastructure services.
4. Analyze packets, then learn safe discovery and monitoring.
5. Complete the labs in [Practical lab workbook](14-practical-labs.md).
6. Build the [Secure enterprise network capstone](15-capstone-project.md).

## Modules
| Module | Subject |
|---|---|
| 01 | [Advanced network architecture](01-network-architecture.md) |
| 02 | [Switching, VLANs, trunks, STP and EtherChannel](02-switching-vlans-stp.md) |
| 03 | [Routing and OSPF](03-routing-ospf.md) |
| 04 | [IPv6 networking and security](04-ipv6.md) |
| 05 | [ACLs, firewalls and filtering](05-acls-firewalls.md) |
| 06 | [DNS, DHCP, NTP and infrastructure services](06-network-services.md) |
| 07 | [Wireless networking and Wi-Fi security](07-wireless-security.md) |
| 08 | [Packet analysis with Wireshark](08-wireshark-analysis.md) |
| 09 | [Network discovery and Nmap](09-network-discovery-nmap.md) |
| 10 | [VPN, IPsec and TLS](10-vpn-ipsec-tls.md) |
| 11 | [Monitoring, logs, SNMP and flow data](11-network-monitoring.md) |
| 12 | [Network segmentation and Zero Trust](12-segmentation-zero-trust.md) |
| 13 | [Troubleshooting methodology](13-troubleshooting.md) |
| 14 | [Practical lab workbook — 16 labs](14-practical-labs.md) |
| 15 | [Capstone project](15-capstone-project.md) |
| — | [Lab report template](LAB-REPORT-TEMPLATE.md) |

## Lab environment
Suggested tools: Cisco Packet Tracer (or equivalent network simulator), VirtualBox, two or more Linux VMs, Wireshark, and Nmap. Start with a simulator. If using real VMs, use host-only/internal networks and snapshots. Do not bridge a test network to a school, workplace, public Wi-Fi or the internet unless the network owner has explicitly approved the activity.

## Evidence standard
For each lab, save:
- A short objective and network diagram
- Addressing/VLAN/routing table where relevant
- Commands/configuration with secrets removed
- Screenshots or sanitized output showing the result
- A short security analysis: what could go wrong, how to detect it, and how to reduce risk
- What failed, how it was diagnosed, and what you learned

Use the [lab report template](LAB-REPORT-TEMPLATE.md). Never upload passwords, VPN keys, private keys, real customer data, unredacted packet captures or personal IP information.

## Responsible-use boundary
Only inspect systems and networks you own or have explicit permission to test. Discovery scans, packet captures, configuration changes and security tests can affect availability and privacy. Keep exercises in an isolated lab, use synthetic data, and follow written scope.

## Completion checklist
- [ ] I can explain each module without copying the text.
- [ ] I can build and verify a small routed, segmented network.
- [ ] I can interpret DNS, TCP, TLS and DHCP packet exchanges.
- [ ] I can explain the purpose and limits of ACLs, firewalls and VPNs.
- [ ] I can collect and interpret network logs/flow data.
- [ ] I have completed labs and attached genuine evidence.
- [ ] I have documented the capstone design and security decisions.
