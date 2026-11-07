# 12 — Wireshark Packet Analysis

## What is Wireshark?
Wireshark is a packet analyzer that displays network traffic captured from an interface or read from a capture file. It helps students understand protocols and helps defenders investigate network behavior.

## Safe capture workflow
1. Start Wireshark.
2. Select your own lab interface (for example, a VirtualBox host-only adapter).
3. Start capture.
4. Generate a test: ping your lab gateway or run a DNS lookup.
5. Stop capture and save as .pcapng.
6. Apply a display filter and inspect packet details.

## Useful display filters
- `icmp` — ICMP traffic
- `arp` — ARP packets
- `dns` — DNS
- `dhcp` or `bootp` — DHCP (filter name depends on version)
- `tcp` — TCP
- `udp` — UDP
- `tcp.port == 443` — TCP port 443
- `ip.addr == 192.168.56.20` — packets involving an IP
- `tcp.flags.syn == 1 && tcp.flags.ack == 0` — initial TCP SYN packets

## What to inspect
- Frame: captured frame details and length.
- Ethernet: source and destination MAC addresses.
- IP: source/destination IP, TTL, fragmentation.
- TCP: ports, flags, sequence/acknowledgment numbers.
- UDP: source/destination ports and length.
- DNS: query name, record type, response.
- TLS: handshake metadata; encrypted application content is not normally readable without appropriate session secrets.

## Mini-labs
1. Capture ping and identify Echo Request/Reply.
2. Clear your lab VM's DNS cache, query a test name and inspect DNS.
3. Open a test HTTPS website and identify TCP handshake and TLS handshake metadata.
4. Compare a successful connection with a deliberately blocked lab connection.

## Analysis notes
Record timestamp, source/destination, protocol, ports, packet flags, observed behavior and conclusion. A single packet rarely proves malicious activity; correlate with endpoint, DNS, firewall and authentication logs.

## Privacy
Capture only traffic you own or have explicit permission to inspect. Avoid collecting passwords, personal data or unrelated users' traffic. Remove sensitive data before publishing captures.
