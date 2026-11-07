# 03 — Capture Workflow and Interface Selection

## 1. Plan before capture
A useful capture begins with a question. Examples:
- Why does this lab client fail to resolve a test hostname?
- Does the TCP handshake complete?
- Which DHCP server supplied the address?
- Is a local application repeatedly retransmitting?

Define the host, interface, protocol, time window and authorization before starting.

## 2. Choosing the right interface
Traffic may travel through Ethernet, Wi-Fi, a VPN adapter, a virtual machine adapter, loopback or a bridge. Capturing the wrong interface may show little or no relevant traffic.

Method:
1. Inspect interface names and traffic graphs.
2. Generate a known action from your own test host.
3. Observe which interface increments.
4. Start the capture on that interface.
5. Confirm expected packets appear.

A VPN can change the path and visibility. A host-side capture may show encrypted tunnel traffic while a capture inside the VM may show inner traffic.

## 3. Capture options
Useful settings include:
- Capture filter: limits which packets are recorded.
- Promiscuous mode: requests frames not addressed to the capture interface, where the network and driver permit it. It does not defeat switch isolation.
- Snap length: maximum bytes captured per packet; truncating packets can hide payload fields.
- Buffer size and rotation: control memory and file growth.
- Name resolution: can make output readable but may generate additional lookups or affect interpretation.

For beginner labs, leave advanced settings at defaults unless you understand the effect.

## 4. Capture filter examples
BPF capture filters (examples):
```text
host 192.0.2.10
src host 192.0.2.10
dst host 192.0.2.20
net 192.0.2.0/24
tcp
udp port 53
port 443
icmp
```
Use documentation addresses only as examples; replace them with your own lab addresses. Capture filters use a different syntax from Wireshark display filters.

## 5. Start, generate, stop
1. Select the interface.
2. Apply a narrow capture filter only if required.
3. Start capture.
4. Generate one known activity.
5. Wait for the response.
6. Stop capture promptly.
7. Save the file and note the timezone and time window.
8. Apply display filters during analysis.

## 6. Capture vs display filtering
A capture filter determines which packets are saved. A display filter only hides or shows packets in the already saved capture. If a packet was excluded by a capture filter, a display filter cannot bring it back.

## 7. Common mistakes
- Capturing the wrong interface
- Starting after the connection already exists
- Capturing too long and collecting unrelated data
- Using display-filter syntax as a capture filter
- Filtering too narrowly and losing context
- Forgetting timezone or capture point
- Assuming absence in a capture means the event did not happen

## Practical exercise
Capture a DNS query and response from your own machine. Save the file. Apply `dns` as a display filter. Record the interface, capture duration, query name (use a harmless test domain) and response code.
