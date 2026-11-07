# 08 — UDP and Common UDP Protocols

## 1. UDP basics
UDP is connectionless and has a small header: source port, destination port, length and checksum. It does not establish a TCP-style session or guarantee delivery, ordering or retransmission. Applications can implement their own reliability.

## 2. Common UDP use cases
- DNS commonly uses UDP/53, with TCP also used in defined situations.
- DHCPv4 uses UDP ports 67 and 68.
- NTP commonly uses UDP/123.
- Many voice/video and real-time applications use UDP.
- QUIC, used by HTTP/3, runs over UDP.

Port numbers are conventions, not proof of protocol identity.

## 3. What to inspect
Look at source/destination IP, ports, packet length, timing, direction, response patterns and application decode. UDP has no handshake, so use the application exchange and context to understand a flow.

## 4. Filters
```text
udp
udp.port == 53
udp.srcport == 123
udp.dstport == 67
udp.length > 1200
```

## 5. UDP troubleshooting
A missing response may be caused by packet loss, firewall policy, wrong destination, application failure or asymmetric routing. Unlike TCP, there is no built-in transport acknowledgment to show delivery. Compare request and response at both endpoints if possible.

## 6. Security analysis
Look for unexpected high-volume UDP, unusual destinations, repeated DNS requests, unexpected services and traffic patterns inconsistent with the host role. High UDP volume can be legitimate streaming, voice or QUIC. Context matters.

## Practical lab
Capture a DNS lookup and NTP synchronization request from your own system where available. Identify UDP source/destination ports and request/response pairing. Compare the DNS exchange with a TCP-based connection in another lab.
