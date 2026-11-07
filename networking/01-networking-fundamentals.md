# 01 — Networking Fundamentals

## What is a computer network?
A network is a group of connected devices that exchange data and share resources. Devices communicate using agreed rules called protocols.

## Why networking matters in cybersecurity
Security analysts investigate how devices communicate, identify unusual connections, understand where traffic should travel, and help protect network boundaries. A strong network foundation makes firewall rules, packet analysis, incident response and vulnerability assessment easier to understand.

## Basic components
- **End device/host:** PC, laptop, phone, server, printer or IoT device.
- **NIC:** Network Interface Card; connects a device to a network.
- **Switch:** Connects devices in a LAN and forwards Ethernet frames using MAC addresses.
- **Router:** Connects different IP networks and forwards packets using IP addresses.
- **Access point:** Connects wireless clients to a network.
- **Firewall:** Allows or blocks traffic according to security rules.
- **Modem/ONT:** Connects a local network to an ISP access service.
- **Cabling/media:** Copper, fiber or wireless radio.

## Network types
- **PAN:** Personal-area network, such as Bluetooth devices.
- **LAN:** Local-area network in a home, office or lab.
- **WLAN:** Wireless LAN using Wi-Fi.
- **MAN:** Metropolitan-area network across a city or campus.
- **WAN:** Wide-area network connecting distant locations; the Internet is the largest public example.

## Common topologies
- **Star:** Devices connect to a central switch. Easy to manage; central device is important.
- **Bus:** Devices share one backbone cable. Mostly historical.
- **Ring:** Devices form a logical or physical ring.
- **Mesh:** Multiple paths connect devices; improves resilience but costs more.
- **Hybrid:** Combines topologies.

## Communication terms
- **Bandwidth:** Maximum theoretical capacity of a link.
- **Throughput:** Actual successful data rate.
- **Latency:** Time taken for data to travel.
- **Jitter:** Variation in packet delay.
- **Packet loss:** Packets that fail to reach the destination.
- **Full duplex:** Send and receive at the same time.
- **Half duplex:** Send or receive at a time.

## Encapsulation
Application data is wrapped with protocol information as it moves down the network stack. At the receiver, headers are interpreted and removed in reverse order. Common units:
- Application data
- TCP segment or UDP datagram
- IP packet
- Ethernet frame
- Bits/signals on the medium

## Client-server and peer-to-peer
In client-server communication, clients request services from servers. In peer-to-peer (P2P), devices can act as both clients and providers. A network can use both models.

## First practical exercise
In Packet Tracer, place two PCs and one switch. Connect each PC to the switch with copper straight-through cables. Assign:
- PC-A: 192.168.10.10 /24
- PC-B: 192.168.10.20 /24
No default gateway is needed for communication within this same subnet. Open the PC command prompt and ping the other PC. A successful reply confirms basic Layer 2/Layer 3 connectivity.

## Check your understanding
1. What is the difference between a switch and a router?
2. Why does a host need a default gateway to reach a different subnet?
3. Explain bandwidth versus throughput.
4. Give one cybersecurity use of a network diagram.
