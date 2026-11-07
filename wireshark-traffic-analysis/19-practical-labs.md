# 19 — Practical Workbook: 20 Wireshark Labs

## Lab rules
Use only your own traffic, an isolated VM network or a trusted synthetic training capture. Keep a record of capture point, timezone, duration and filters. Sanitize screenshots and exported files.

## Beginner labs
### Lab 01 — First capture
Install Wireshark, select the correct interface, capture 30 seconds of your own traffic, stop and save. Identify packet list, details and bytes panes.

### Lab 02 — Packet anatomy
Capture ping and inspect Ethernet, IP and ICMP fields. Identify source/destination MAC and IP, TTL and protocol.

### Lab 03 — DNS lookup
Run a harmless DNS query with dig/nslookup. Filter `dns`, identify query/response, type, transaction ID, answer and TTL.

### Lab 04 — ARP resolution
In a private LAN, generate traffic to a local peer. Inspect ARP request/reply and explain why the gateway MAC is used for off-subnet traffic.

### Lab 05 — DHCP DORA
Renew a test VM's DHCP lease. Identify Discover, Offer, Request and ACK plus assigned address, server identifier and options.

### Lab 06 — ICMP and traceroute
Capture ping and traceroute to a permitted destination. Identify echo and time-exceeded packets and explain hop-limit/TTL behavior.

## Intermediate labs
### Lab 07 — TCP three-way handshake
Connect to a local test service. Identify SYN, SYN-ACK and ACK, sequence/acknowledgment values and ports.

### Lab 08 — TCP close and reset
Capture a normal connection close, then connect to a closed local test port. Compare FIN-based close and RST behavior.

### Lab 09 — Retransmission analysis
Use a trusted training capture with packet loss or a controlled local lab condition. Find retransmissions and duplicate ACKs. Explain benign causes and why one retransmission is not proof of attack.

### Lab 10 — UDP and DNS
Identify UDP ports, request/response pairing and packet sizes. Compare UDP DNS with any TCP DNS exchange available in the lab.

### Lab 11 — HTTP request/response
Run a local test web server and request a harmless page. Identify method, host, URI and status code. Use synthetic content only.

### Lab 12 — TLS handshake
Visit a permitted HTTPS test endpoint. Inspect visible ClientHello/ServerHello metadata and explain why application data is encrypted.

### Lab 13 — Display filter practice
Use the filter cheat sheet. Apply at least ten filters, explain each result and record any filter syntax that differs by version.

### Lab 14 — Statistics investigation
Use Protocol Hierarchy, Conversations, Endpoints, I/O Graphs and Flow Graph to identify the busiest conversation and explain whether it is expected.

## Advanced defensive labs
### Lab 15 — DNS anomaly triage
Use synthetic or trusted training traffic. Find repeated failures or unusually long query labels. List benign explanations and additional evidence required before concluding tunneling.

### Lab 16 — Scan-like traffic analysis
Use a trusted training PCAP or simulator-generated lab capture. Identify source, destination range, ports and connection outcomes. Explain how authorized inventory scans can resemble malicious reconnaissance.

### Lab 17 — Beacon-like pattern review
Use synthetic events or a trusted training PCAP. Measure repeated connection intervals and destination consistency. Compare with legitimate update agents and monitoring systems.

### Lab 18 — Troubleshooting case
Create a local service failure or use a simulator. Find whether the failure occurs at DNS, TCP connection setup, TLS handshake or application response. Document the exact evidence.

### Lab 19 — TShark extraction
Read a lab capture with TShark. Export timestamps, IP addresses, ports and DNS names to CSV. Compare output with GUI analysis and protect the exported file.

### Lab 20 — SOC timeline
Combine synthetic DHCP, DNS, firewall and packet events. Normalize timestamps, map IP to device at the relevant time and write an evidence-based incident summary.

## Completion requirements
A lab is complete only when you have:
- Performed the steps in your own authorized environment
- Saved actual output or a sanitized screenshot
- Explained what the packets show
- Recorded limitations and alternative explanations
- Written one defensive/security lesson
