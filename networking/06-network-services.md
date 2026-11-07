# 06 — Core Network Services: ARP, DHCP, DNS and NAT

## ARP
Address Resolution Protocol maps an IPv4 address to a MAC address on the local link. A host uses an ARP request (broadcast) and receives an ARP reply. ARP is not used to discover a remote server's MAC; the host resolves the local default gateway instead.

Useful commands:
- Windows: `arp -a`
- Linux: `ip neigh`

Security: ARP spoofing/poisoning can redirect local traffic. Defenses include switch protections such as Dynamic ARP Inspection where supported, segmentation and encrypted application protocols.

## DHCP
Dynamic Host Configuration Protocol automatically provides network configuration such as IP address, subnet mask, default gateway and DNS server.

Common DORA sequence:
1. Discover
2. Offer
3. Request
4. Acknowledge

UDP ports: server 67, client 68. Use reservations for predictable addresses and protect trusted DHCP infrastructure with DHCP snooping where supported.

## DNS
Domain Name System translates names such as example.com into records such as A (IPv4) and AAAA (IPv6). Other records include CNAME, MX, NS, TXT and PTR.

Useful commands:
- Windows/Linux: `nslookup example.com`
- Linux: `dig example.com`

DNS security topics: spoofing, cache poisoning, tunneling, malicious domains, DNSSEC validation and protective DNS filtering.

## NAT and PAT
Network Address Translation changes IP addressing as traffic crosses a router/firewall. PAT (many-to-one port translation) allows multiple private hosts to share a public IPv4 address. NAT is not a substitute for a firewall.

## Other useful services
- NTP: time synchronization (important for log correlation).
- SNMP: network monitoring and management; prefer secure versions/configurations.
- SSH: encrypted remote administration.
- HTTP/HTTPS: web traffic.
- Syslog: centralized event messages.

## Lab
Capture a DHCP lease process and a DNS lookup in Wireshark. Identify message types, client/server addresses, DNS question and answer. Use only your own lab traffic.
