# 04 — Packet Anatomy and Encapsulation

## 1. Encapsulation
When an application sends data, each network layer adds its own header (and sometimes trailer). A simplified Ethernet + IPv4 + TCP + HTTP packet contains:
- Ethernet header
- IPv4 header
- TCP header
- HTTP bytes (if visible)
- Ethernet frame check sequence may or may not be visible in a host capture

The receiver removes and interprets these headers in reverse order. This is encapsulation and decapsulation.

## 2. Ethernet header
Common fields:
- Destination MAC address
- Source MAC address
- EtherType (identifies the payload protocol, such as IPv4 or IPv6)
- Optional 802.1Q VLAN tag
- Payload

The Ethernet frame is a local-link delivery unit. MAC addresses normally change at each routed hop, while the end-to-end IP source and destination usually remain the same unless NAT or another transformation is involved.

## 3. IP header
IPv4 fields include version, header length, total length, identification, flags, fragment offset, TTL, protocol, header checksum, source and destination addresses, and optional options.

IPv6 has a fixed base header with fields including traffic class, flow label, payload length, next header, hop limit and 128-bit source/destination addresses. Optional information uses extension headers.

## 4. TCP header
TCP includes source/destination ports, sequence and acknowledgment numbers, header length, flags, window size, checksum and optional options. TCP provides ordered, reliable byte-stream delivery with retransmission and flow/congestion control.

## 5. UDP header
UDP is smaller: source port, destination port, length and checksum. UDP does not provide TCP-style connection establishment or retransmission guarantees. Applications handle reliability if needed.

## 6. Ports and protocol identification
Ports identify application endpoints on a host, not a guaranteed application identity. A service can use a non-standard port, and traffic on a familiar port may not be the expected application. Validate with protocol decoding, endpoint context and service configuration.

## 7. Packet details and bytes panes
Select a packet. Expand each protocol layer in Packet Details. Selecting a field highlights corresponding bytes in Packet Bytes. This is useful for understanding how decoded values map to raw data.

## 8. Checksums and offloading
Host network cards and operating systems may calculate checksums or segment packets after the capture point. Wireshark can therefore show apparently incorrect checksums or unusually large segments in local captures. This may be an offload artifact rather than corruption on the wire.

## 9. Practical exercise
Capture a ping and a DNS lookup. Expand Ethernet, IP and ICMP/DNS fields. Identify source/destination MAC, source/destination IP, protocol, TTL/hop limit and payload type. Write how the frame and packet are related.

## Analyst warning
A packet is a single observation in a sequence. Interpret it with adjacent packets, direction, timing and capture location.
