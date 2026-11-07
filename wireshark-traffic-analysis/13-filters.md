# 13 — Capture Filters and Display Filters

## 1. Two different filter languages
**Capture filters** use BPF/libpcap syntax and decide which packets are saved during capture. **Display filters** use Wireshark's own syntax and decide which saved packets are shown. Their syntax is not interchangeable.

## 2. Capture filter examples
```text
host 192.0.2.10
src host 192.0.2.10
dst net 192.0.2.0/24
tcp
udp port 53
port 443
icmp
```

## 3. Display filter basics
Display filters use protocol fields and comparison operators:
```text
ip.addr == 192.0.2.10
tcp.port == 443
udp.port == 53
dns
http
tls
icmp
arp
frame.len > 1000
```

## 4. Operators
- Equality: `==`
- Inequality: `!=`
- Greater/less: `>`, `<`, `>=`, `<=`
- Logical AND: `&&`
- Logical OR: `||`
- Logical NOT: `!`
- Membership/set: `in { ... }` where supported by the field and version

Example:
```text
ip.src == 192.0.2.10 && tcp.dstport == 443
dns || dhcp
!(arp || icmp)
```

## 5. Common security and troubleshooting filters
```text
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.flags.reset == 1
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.analysis.zero_window
dns.flags.rcode != 0
icmp
icmpv6
ip.ttl <= 2
frame.len > 1400
```

## 6. Build filters carefully
Start broad, then narrow. If a filter shows no packets:
1. Confirm the capture contains the traffic.
2. Check field spelling using Wireshark's autocomplete.
3. Inspect the packet details tree for exact field names.
4. Confirm protocol decode and port.
5. Remove conditions one at a time.

## 7. Follow a conversation
Right-click a packet and choose Follow Stream. This is often faster than writing a complex filter when you want to understand one TCP or UDP conversation.

## Practical exercise
Create a small capture containing DNS, ICMP and HTTPS from your own test host. Apply at least six display filters and explain why each packet appears. Save your filters in a notes file.
