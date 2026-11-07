# Wireshark Display Filter Cheat Sheet

These expressions filter packets already captured. They are not capture filters. Field availability may vary by protocol decoder/version.

## General
```text
frame
frame.len > 1000
eth
vlan
ip
ipv6
arp
icmp
icmpv6
tcp
udp
```

## Hosts and ports
```text
ip.addr == 192.0.2.10
ip.src == 192.0.2.10
ip.dst == 192.0.2.20
tcp.port == 443
tcp.dstport == 22
udp.port == 53
```

## TCP
```text
tcp.flags.syn == 1
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.flags.reset == 1
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.duplicate_ack
tcp.analysis.zero_window
tcp.stream == 0
```

## DNS and DHCP
```text
dns
dns.flags.response == 0
dns.flags.response == 1
dns.flags.rcode != 0
dns.qry.type == 1
dns.qry.type == 28
dhcp
bootp
```

## HTTP and TLS
```text
http
http.request
http.response
http.response.code >= 400
tls
tls.handshake
tls.alert_message
quic
```

## Combine conditions
```text
dns || dhcp
ip.src == 192.0.2.10 && tcp.dstport == 443
!(arp || icmp)
tcp.flags.syn == 1 && tcp.flags.ack == 0
```

## If a filter fails
Use autocomplete, inspect the decoded packet tree and check your Wireshark version. Start broad, then narrow one condition at a time.