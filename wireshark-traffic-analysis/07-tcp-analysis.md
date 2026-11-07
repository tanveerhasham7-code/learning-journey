# 07 — TCP Deep Dive and Connection Analysis

## 1. What TCP provides
TCP is a connection-oriented transport protocol. It provides a reliable, ordered byte stream using sequence numbers, acknowledgments, retransmissions, flow control and congestion control.

## 2. Three-way handshake
A normal connection setup:
1. Client sends SYN with an initial sequence number.
2. Server replies SYN-ACK, acknowledging the client's SYN and providing its own sequence number.
3. Client sends ACK.

A successful handshake shows that the endpoints (and any path devices) completed connection setup at that moment. It does not prove the application is healthy or safe.

Display filter:
```text
tcp.flags.syn == 1
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.flags.syn == 1 && tcp.flags.ack == 1
```

## 3. TCP flags
- SYN: establish connection
- ACK: acknowledgment field is valid
- FIN: orderly close request
- RST: reset/abort
- PSH: push indication
- URG: urgent pointer significance
- ECE/CWR: congestion notification signaling

Flags must be interpreted in sequence and context.

## 4. Sequence and acknowledgment numbers
Sequence numbers identify byte positions in the stream. Acknowledgment numbers indicate the next byte expected. Wireshark often uses relative sequence numbers for readability. Analyze the conversation rather than treating one number in isolation.

## 5. Window and flow control
The receive window tells the sender how much data the receiver is prepared to accept. Window scaling can expand the effective window. Zero-window events can indicate a receiver temporarily cannot accept more data; inspect endpoint performance and adjacent packets.

## 6. Retransmissions and duplicate ACKs
Retransmissions can indicate packet loss, congestion, wireless interference, overloaded endpoints or capture artifacts. Duplicate ACKs may be part of loss recovery. Do not label every retransmission as an attack.

Useful filters:
```text
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.duplicate_ack
tcp.analysis.lost_segment
tcp.analysis.zero_window
tcp.flags.reset == 1
```

## 7. Connection teardown
A normal close often uses FIN/ACK exchanges in both directions. RST abruptly resets a connection. A reset can come from an endpoint or an intermediate device; identify direction and correlate with firewall/server logs.

## 8. Follow TCP stream
Right-click a TCP packet and choose Follow → TCP Stream. This groups the conversation and can show readable application data when unencrypted. For TLS, the application payload remains encrypted unless authorized decryption is configured.

## 9. Analyst workflow for a failed connection
1. Find the initial SYN.
2. Check whether SYN-ACK returns.
3. Check whether final ACK occurs.
4. Inspect retransmissions, RST and ICMP errors.
5. Confirm destination service is listening.
6. Check routing, ACL/firewall and NAT logs.
7. Correlate endpoint timestamps.

## Practical lab
Start a local test web server on a VM and connect from another VM. Capture the handshake, data exchange and close. Repeat with the server stopped and compare the result. Record how a refused connection differs from a silent timeout.

## Security perspective
Many scans and connection probes create SYN traffic, but normal applications do too. Establish baseline, examine destination diversity and rate, and correlate with asset inventory before classifying activity.
