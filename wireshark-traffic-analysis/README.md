# Wireshark & Network Traffic Analysis — Complete Cybersecurity Learning Track

A beginner-to-advanced course for learning how to capture, read, investigate and explain network traffic like a network defender, SOC analyst and incident responder.

> **Learning honesty:** The guides, examples and scripts are learning resources. They do not mean the labs have been run. Mark a lab complete only after you perform it in an authorized environment and save genuine, sanitized evidence.

## Course outcomes
By the end, you should be able to:
- Explain how data moves through Ethernet, IP, TCP, UDP and common application protocols.
- Capture traffic safely and choose the correct interface and capture scope.
- Read packet details, follow conversations and reconstruct protocol sequences.
- Write capture filters and display filters and understand the difference.
- Investigate DNS, DHCP, ARP, ICMP, TCP, HTTP and TLS behavior.
- Troubleshoot latency, retransmissions, resets, DNS failures and connection problems.
- Recognize suspicious patterns such as scanning, unusual DNS activity, beacon-like connections and unexpected data transfers without treating indicators as proof.
- Build a defensible SOC investigation timeline using packet evidence and supporting logs.
- Export, sanitize and document evidence responsibly.

## Course modules
| # | Module |
|---|---|
| 01 | [Traffic analysis foundations](01-traffic-analysis-foundations.md) |
| 02 | [Install and configure Wireshark](02-installation-and-setup.md) |
| 03 | [Capture workflow and interface selection](03-capture-workflow.md) |
| 04 | [Packet anatomy and encapsulation](04-packet-anatomy.md) |
| 05 | [Ethernet, MAC and ARP](05-ethernet-arp.md) |
| 06 | [IPv4, IPv6, ICMP and fragmentation](06-ip-icmp-ipv6.md) |
| 07 | [TCP deep dive](07-tcp-analysis.md) |
| 08 | [UDP and common UDP protocols](08-udp-analysis.md) |
| 09 | [DNS traffic analysis](09-dns-analysis.md) |
| 10 | [DHCP and address assignment](10-dhcp-analysis.md) |
| 11 | [HTTP and web traffic](11-http-analysis.md) |
| 12 | [TLS and HTTPS analysis](12-tls-https-analysis.md) |
| 13 | [Capture and display filters](13-filters.md) |
| 14 | [Statistics, conversations and expert information](14-statistics-and-io-graphs.md) |
| 15 | [Troubleshooting with packet evidence](15-troubleshooting.md) |
| 16 | [Security monitoring and threat hunting](16-security-threat-hunting.md) |
| 17 | [SOC investigation workflow and evidence handling](17-soc-investigation-workflow.md) |
| 18 | [TShark command-line analysis](18-tshark-cli.md) |
| 19 | [Practical workbook — 20 labs](19-practical-labs.md) |
| 20 | [Capstone: investigate a simulated incident](20-capstone-project.md) |
| — | [Display filter cheat sheet](FILTER-CHEATSHEET.md) |
| — | [Lab report template](LAB-REPORT-TEMPLATE.md) |
| — | [Glossary and learning resources](GLOSSARY-RESOURCES.md) |

## Recommended learning sequence
Study Modules 01–06 first. Then learn TCP/UDP and the application protocols. After that, practice filters, statistics and troubleshooting. Complete the security investigation modules only after you understand normal traffic.

## Lab environment
Recommended: Wireshark, TShark (installed with Wireshark on many platforms), one or two Linux/Windows VMs, and a host-only/internal virtual network. Generate traffic yourself using ordinary DNS lookups, ping, a local web server and test client. You can also use synthetic PCAPs or trusted training captures.

## Safety and privacy rules
- Capture only your own devices/lab or traffic for which you have explicit permission.
- Do not monitor public Wi-Fi, classmates, workplace or university traffic without written authorization.
- Packet captures can contain credentials, cookies, personal data, internal addresses and private communications.
- Prefer synthetic traffic. Use narrow capture scope and short capture durations.
- Do not upload raw captures publicly without reviewing and sanitizing them.
- Do not decrypt traffic unless you own the endpoints and are authorized to handle the relevant key material.
- Never publish TLS secrets, VPN keys, session cookies, tokens or private keys.

## Evidence checklist
For every lab, save: objective, topology, capture point, exact filter, relevant packet numbers, explanation of the protocol sequence, observations, limitations, screenshots with sensitive values removed, and what you learned. Use the report template.

## Portfolio rule
A packet capture proves only what was visible at that capture point and time. A suspicious packet or indicator is not proof of compromise. State observations, hypotheses and conclusions separately.
