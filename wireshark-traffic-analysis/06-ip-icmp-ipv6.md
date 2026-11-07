# 06 — IPv4, IPv6, ICMP and Fragmentation

## 1. IPv4 fields
Inspect source/destination addresses, TTL, protocol, total length, identification, flags and fragment offset. TTL decreases at each router; it helps prevent packets circulating forever.

## 2. IPv4 fragmentation
If a packet is too large for a link and fragmentation is permitted, IPv4 may split it into fragments. The destination reassembles them. Fragmentation can complicate inspection and may be mishandled by some security devices. Path MTU Discovery is used to avoid fragmentation where possible.

Wireshark may label fragmented packets and show reassembly details when enough fragments are captured. Missing fragments can prevent full reassembly.

## 3. ICMP
ICMP carries network control and error information. Common types include echo request/reply (ping), destination unreachable and time exceeded (used by traceroute methods).

ICMP is not inherently malicious. Blocking all ICMP can break diagnostics and Path MTU Discovery. Apply sensible policy rather than blanket assumptions.

Filters:
```text
icmp
icmp.type == 8
icmp.type == 0
icmp.type == 3
ip.ttl <= 2
```

## 4. IPv6 essentials
IPv6 uses 128-bit addresses and no broadcast. Neighbor Discovery uses ICMPv6. Important traffic includes router solicitation/advertisement, neighbor solicitation/advertisement and ICMPv6 errors.

Filters:
```text
ipv6
icmpv6
ipv6.addr == 2001:db8::1
icmpv6.type == 135
icmpv6.type == 136
```

## 5. Security analysis
Review unexpected source addresses, unusual fragmentation, abnormal ICMP volume, unexpected router advertisements and inconsistent IPv4/IPv6 policy. Fragmentation patterns can be benign. Confirm with host, firewall and topology context.

## Practical lab
Capture ping and traceroute to a destination you are allowed to test. Identify echo request/reply and time-exceeded messages. In a simulator, configure IPv6 and observe neighbor discovery. Record how TTL/hop limit changes across routed hops.

## Troubleshooting
If large transfers fail but small pings work, investigate MTU and Path MTU Discovery. Do not change MTU blindly; gather packet and interface evidence first.
