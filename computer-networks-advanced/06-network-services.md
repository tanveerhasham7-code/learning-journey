# 06 — DNS, DHCP, NTP and Infrastructure Services

## 1. DNS
The Domain Name System maps names to records such as IPv4 (A), IPv6 (AAAA), aliases (CNAME), mail exchangers (MX), name servers (NS), text (TXT) and reverse lookup (PTR).

A typical lookup may involve a stub resolver, recursive resolver, root server, top-level domain server and authoritative server. Caching reduces repeated queries; TTL controls how long cached data may be retained.

Security topics:
- DNSSEC provides data-origin authentication and integrity for signed DNS data; it does not encrypt ordinary DNS queries.
- DoH and DoT encrypt client-to-resolver communication, but do not automatically make a resolver trustworthy.
- Monitor unusual query volume, suspicious domains, unexpected TXT use, high NXDOMAIN rates and unauthorized DNS servers.
- Restrict zone transfers and protect registrar/DNS administration with MFA and change control.

Useful commands:
```bash
dig example.com A
dig example.com MX
dig -x 192.0.2.10
nslookup example.com
```

## 2. DHCP
Dynamic Host Configuration Protocol automatically provides clients with network configuration. The familiar IPv4 DORA sequence is Discover, Offer, Request, Acknowledge. DHCP options may include subnet mask, default gateway, DNS servers and lease duration.

Security risks include rogue DHCP servers and DHCP starvation. Defenses include DHCP snooping, trusted/untrusted switch ports, rate limits and monitoring. Exact feature names vary by vendor.

## 3. NTP
Network Time Protocol synchronizes clocks. Accurate time is essential for correlating firewall, endpoint, authentication and SIEM events. A clock mismatch can make an incident timeline misleading.

Use approved time sources, monitor offset, restrict administration and avoid exposing unnecessary NTP services.

## 4. Other common services
- **SSH:** encrypted remote administration; prefer key-based authentication and restricted management sources.
- **SNMP:** device monitoring; prefer SNMPv3 with authentication and privacy over older community-string approaches.
- **Syslog:** sends device/application messages to a log collector; protect transport and restrict who can send or read logs.
- **RADIUS/TACACS+:** centralize network access or device administration authentication, depending on design.
- **AAA:** authentication, authorization and accounting.

## Practical lab
Use a simulator or isolated Linux VMs. Configure a DHCP scope, inspect a DNS lookup with dig/nslookup, verify system time synchronization and send a test syslog message to a local collector if available. Capture DHCP DORA and DNS query/response packets in Wireshark.

## Analyst exercise
Create a small timeline from synthetic DNS, DHCP and firewall logs. Explain how a DHCP lease record can associate an IP with a device at a particular time, why clock synchronization matters and why an IP address alone is not a permanent user identity.
