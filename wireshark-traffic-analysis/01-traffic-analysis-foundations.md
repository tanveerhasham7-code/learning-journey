# 01 — Network Traffic Analysis Foundations

## 1. What is network traffic?
Network traffic is data moving between devices over a network. When you open a website, your device may first ask DNS for an address, establish a TCP connection, negotiate TLS, send an HTTP request and receive a response. These steps create packets that can be observed at a suitable capture point.

A packet analyzer such as Wireshark helps you inspect this communication. It is used by network engineers, SOC analysts, incident responders, malware analysts and application developers.

## 2. Why cybersecurity professionals analyze traffic
Traffic analysis can help answer:
- Which device communicated with which destination?
- When did the communication start and stop?
- Which protocol and port were used?
- Did a connection complete, reset or retransmit?
- Which DNS name was queried?
- Was traffic encrypted?
- Did a host contact an unexpected service?
- Is the observed behavior consistent with normal business activity?

Packet analysis is one evidence source. Combine it with endpoint telemetry, DNS logs, DHCP leases, firewall logs, identity records and asset inventory.

## 3. What Wireshark can and cannot show
Wireshark can decode protocol headers and, when visible, application fields. It can show timing, packet sizes, flags, retransmissions and conversation metadata.

It cannot automatically see every packet on a switched network. A capture sees traffic available to its interface or capture point. It cannot normally read encrypted TLS application content. It cannot prove a host is compromised just because a packet looks unusual.

## 4. The communication model
A simplified web request:
1. Application decides to access a hostname.
2. DNS resolves the hostname to an IP address (unless a cached answer is used).
3. IP selects a route to the destination.
4. TCP establishes a connection, if the application uses TCP.
5. TLS may authenticate the server and establish encryption.
6. HTTP carries the request and response.
7. TCP closes or reuses the connection.

Not all applications use this exact sequence. HTTP/3 uses QUIC over UDP, and cached DNS or persistent connections can change what appears in a capture.

## 5. OSI model as an analysis aid
| Layer | Examples | What to inspect |
|---|---|---|
| 7 Application | DNS, HTTP, DHCP | Names, requests, responses |
| 6 Presentation | TLS encoding/encryption concepts | Negotiation and encryption metadata |
| 5 Session | Session behavior | Dialogs and state |
| 4 Transport | TCP, UDP | Ports, flags, sequence, retransmission |
| 3 Network | IPv4, IPv6, ICMP | Addresses, routes, TTL/hop limit |
| 2 Data link | Ethernet, Wi-Fi | MAC addresses, VLAN tags |
| 1 Physical | Copper, fiber, radio | Link state and signal; not usually packet-decoded |

OSI is a teaching model; real protocols do not always fit neatly into one layer.

## 6. Key vocabulary
- **Frame:** Layer 2 data unit.
- **Packet:** commonly used for Layer 3 IP data unit.
- **Segment:** TCP transport data unit.
- **Datagram:** often used for UDP or IP data unit depending on context.
- **Payload:** data carried inside a protocol unit.
- **Capture point:** interface or device where packets are observed.
- **PCAP/PCAPNG:** file formats for packet captures.
- **Flow/conversation:** communication between endpoints over a protocol/port tuple.
- **Five-tuple:** source IP, destination IP, source port, destination port and transport protocol.

## 7. Analyst mindset
First establish what is normal for the host, service, time and network. Then investigate deviations. Record exact packet numbers and timestamps. Avoid jumping from “unusual” to “malicious.”

## Mini exercise
Draw the steps your computer takes when visiting a website. Mark where DNS, TCP, TLS and HTTP occur. Later, capture the same activity and compare the diagram with the packets.
