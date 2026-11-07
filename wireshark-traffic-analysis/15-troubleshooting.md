# 15 — Troubleshooting with Packet Evidence

## 1. A repeatable method
1. Define exact symptom and time.
2. Identify affected client, destination and application.
3. Confirm capture point and scope.
4. Find the first relevant packet.
5. Follow the protocol sequence.
6. Identify where expected behavior stops.
7. Correlate with endpoint, DNS, firewall and server logs.
8. State a likely cause and confidence level.
9. Verify after an approved fix.

## 2. DNS failure
Symptoms: application cannot resolve a hostname.
Inspect DNS query, destination resolver, response code, retries and timing. Check client resolver settings, DNS server logs, network reachability and domain configuration. NXDOMAIN means the responding resolver reports the name does not exist; it does not automatically mean malicious activity.

## 3. TCP connection timeout
A client sends SYN but no SYN-ACK returns. Possible causes include firewall drop, routing failure, server down, asymmetric path or packet loss. Capture at both ends if authorized to identify where the SYN disappears.

## 4. Connection refused
A RST may indicate that the destination host is reachable but no service is listening or a device actively rejects the connection. Confirm with server listener state and firewall logs.

## 5. Slow application
Inspect DNS latency, TCP handshake time, retransmissions, RTT, zero-window events, server response delay and transfer duration. A slow application may be caused by the server or client rather than the network.

## 6. MTU problems
Small packets work but larger transfers stall. Inspect ICMP fragmentation-needed (IPv4) or Packet Too Big (IPv6) messages and path MTU behavior. Do not disable ICMP indiscriminately.

## 7. One-way traffic
If requests appear but responses do not, consider filtering, routing asymmetry, NAT, server behavior and capture location. A single capture point cannot always reveal where a packet was lost.

## 8. Common false conclusions
- Bad checksum in host capture may be checksum offload.
- Retransmission may be ordinary loss.
- RST may be a normal application close or rejection.
- Large transfer may be legitimate.
- Missing packet may be outside capture visibility.
- Strange DNS name may be application telemetry or CDN behavior.

## Practical exercise
Create three faults in a simulator or isolated lab, one at a time: wrong DNS server, blocked TCP service and wrong gateway. Capture each failure, identify the packet-level clue and document what additional logs would confirm the cause.
