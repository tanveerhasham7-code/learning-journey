# 08 — Packet Analysis with Wireshark

## 1. What packet analysis tells you
A packet capture records traffic visible at a capture point. It can reveal protocols, timing, endpoints, retransmissions, DNS activity, TCP handshakes and TLS negotiation. It cannot show traffic that the capture point cannot observe, and encrypted payloads normally remain unreadable without legitimate decryption material.

## 2. Capture safely
Capture only your own lab traffic or traffic for which you have explicit permission. Prefer a host-only/internal VM network. Avoid collecting credentials or private communications. Use capture filters to reduce unnecessary data and remove sensitive material before sharing files.

## 3. Capture filters vs display filters
Capture filters are applied while capturing and use libpcap/BPF syntax. Display filters are applied after packets are captured and use Wireshark's display-filter language.

Examples of display filters:
```text
dns
dhcp
arp
icmp
icmpv6
tcp
tcp.port == 443
ip.addr == 192.0.2.10
tcp.flags.syn == 1 && tcp.flags.ack == 0
tls.handshake
```
These are examples; replace documentation addresses with your lab addresses.

## 4. TCP three-way handshake
A normal TCP connection begins with:
1. SYN — client requests a connection.
2. SYN-ACK — server acknowledges and offers its side of the connection.
3. ACK — client acknowledges.

Repeated SYNs without a completed handshake may indicate packet loss, filtering, service unavailability or scanning. Context is necessary before calling it malicious.

## 5. DNS analysis
Filter on `dns`. Identify query name, query type, response code, answer records and timing. Look for unexpected resolvers, repeated failures, unusual query volume and domains that do not fit the lab scenario. A strange-looking domain is a lead for investigation, not proof of malware.

## 6. TLS analysis
Use `tls.handshake` to inspect visible handshake metadata such as versions, cipher negotiation and certificate details where exposed. Modern TLS encrypts application data. Do not assume a capture can reveal passwords or web page contents.

## 7. TCP health indicators
Inspect retransmissions, duplicate ACKs, resets, zero windows and connection setup time. These can indicate congestion, packet loss, endpoint problems or policy devices. Correlate with endpoint and network logs.

## Practical lab
Generate a DNS lookup, ping and HTTPS request from a lab VM while capturing on the same isolated interface. Apply filters, identify the DNS exchange, ICMP packets and TCP handshake, then inspect TLS metadata. Save a sanitized screenshot and a short explanation.

## Analyst workflow
1. Define the question and time window.
2. Confirm capture point and scope.
3. Apply a narrow display filter.
4. Identify endpoints and protocol sequence.
5. Build a timeline.
6. Correlate with DNS, DHCP, firewall and endpoint logs.
7. State observations separately from conclusions.
