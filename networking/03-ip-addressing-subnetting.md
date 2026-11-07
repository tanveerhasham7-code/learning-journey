# 03 — IPv4, Subnetting and CIDR

## IPv4 basics
An IPv4 address is 32 bits, written as four decimal octets, for example 192.168.1.10. Each octet ranges from 0 to 255.

An address is interpreted together with a subnet mask or prefix length. The prefix identifies the network portion; remaining bits identify host addresses.

Examples:
- 192.168.1.10/24 → mask 255.255.255.0
- 10.20.0.5/16 → mask 255.255.0.0
- 172.16.4.9/20 → mask 255.255.240.0

## Private IPv4 ranges
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

These are intended for private networks and are not globally routed on the public Internet.

## Important terms
- Network address: identifies the subnet.
- Host address: assigned to an interface within the subnet.
- Broadcast address: IPv4 address used to reach all hosts on a subnet.
- Default gateway: router interface used to reach other networks.
- CIDR: prefix notation such as /24.
- DHCP: can automatically provide IP configuration.

For a typical IPv4 subnet, number of addresses = 2^(32-prefix). Traditional usable host count is total addresses minus network and broadcast addresses, with special handling for /31 and /32.

## Worked example: 192.168.10.0/24
- Mask: 255.255.255.0
- Network: 192.168.10.0
- Usable host range: 192.168.10.1–192.168.10.254
- Broadcast: 192.168.10.255
- Total addresses: 256
- Traditional usable hosts: 254

## Worked example: split 192.168.10.0/24 into four equal subnets
Borrow 2 host bits, so /24 becomes /26. Each subnet has 64 total addresses and 62 traditional usable hosts.
1. 192.168.10.0/26 — hosts .1 to .62, broadcast .63
2. 192.168.10.64/26 — hosts .65 to .126, broadcast .127
3. 192.168.10.128/26 — hosts .129 to .190, broadcast .191
4. 192.168.10.192/26 — hosts .193 to .254, broadcast .255

## IPv6 overview
IPv6 uses 128-bit addresses, written in hexadecimal groups. It provides a vastly larger address space and supports modern network design. Learn global unicast, link-local, unique-local, multicast, SLAAC and DHCPv6.

## Lab
Use a subnet calculator only to check your manual work, not replace learning. Create two different /24 networks in Packet Tracer, connect them through a router, configure interface IPs and gateways, then test pings across networks.
