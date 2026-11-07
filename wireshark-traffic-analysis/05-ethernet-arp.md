# 05 — Ethernet, MAC Addresses, VLAN Tags and ARP

## 1. MAC addresses
Ethernet interfaces use link-layer addresses, commonly 48 bits. A switch learns source MAC addresses on ports and forwards frames based on its MAC address table. MAC addresses identify a network interface at Layer 2; they are not reliable proof of a person's identity and can be changed or spoofed.

## 2. Ethernet frame analysis
In Wireshark expand Ethernet II. Inspect source, destination and type. Broadcast destination is commonly ff:ff:ff:ff:ff:ff. Multicast and unicast have different destination patterns.

## 3. ARP purpose
IPv4 hosts use Address Resolution Protocol to learn the MAC address associated with a local IPv4 next-hop address. If the destination is outside the local subnet, the host usually resolves the default gateway's MAC, not the remote server's MAC.

Typical ARP exchange:
1. Request: “Who has this IPv4 address?”
2. Reply: “This IPv4 address is at this MAC address.”

ARP is a local-link protocol and has no built-in cryptographic authentication. A malicious or misconfigured device may send misleading ARP messages.

## 4. Wireshark filters
```text
arp
arp.opcode == 1
arp.opcode == 2
eth.addr == aa:bb:cc:dd:ee:ff
eth.src == aa:bb:cc:dd:ee:ff
vlan
```
Replace example MAC addresses with your own lab values.

## 5. Defensive interpretation
Potential warning signs include unexpected changes in gateway MAC mapping, many unsolicited ARP replies, duplicate IP warnings or unusual ARP volume. These can also result from failover, virtual machines, network changes or legitimate address management.

Defenses may include DHCP snooping with Dynamic ARP Inspection, static bindings for selected critical systems, port security, 802.1X and monitoring. Feature availability depends on switch platform and design.

## 6. VLAN tags
802.1Q inserts a VLAN tag into Ethernet frames on trunks. In captures, Wireshark may decode VLAN ID and priority fields. Whether tags are visible depends on capture location and NIC/driver offload.

## Practical lab
In an isolated LAN with two VMs, clear or wait for the neighbor cache, ping the other VM and capture ARP. Identify request and reply. Compare the target's MAC with the IP next-hop logic. Do not perform ARP spoofing on a real network.

## Investigation question
If a workstation reports that its gateway MAC changed, what other evidence would you check before calling it an ARP spoofing incident?
