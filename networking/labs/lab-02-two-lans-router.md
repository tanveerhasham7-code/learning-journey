# Lab 02 — Connect Two LANs Through a Router

**Status:** Successfully tested — bidirectional communication demonstrated.  
**Date performed:** 15 November 2026  
**Tool:** Cisco Packet Tracer  
**Router:** Cisco 2911  
**Switches:** 2 × Cisco 2960-24TT  
**Topology:** Two PCs, two access switches, and one router.

## 1. Objective

Build two separate IPv4 LANs and use a router to forward traffic between them. Configure host addresses and default gateways, bring up the router interfaces, and verify connectivity in both directions with ICMP ping.

## 2. Topology

```text
PC0 ---- Switch0 ---- G0/0 [ Router0 ] G0/1 ---- Switch1 ---- PC1
        LAN-A: 192.168.10.0/24       LAN-B: 192.168.20.0/24
```

The first topology screenshot below records the initial setup stage: the left router link is up, while the right router link is still red/down because GigabitEthernet0/1 has not yet been configured and enabled. After both router interfaces were configured with `no shutdown`, the later screenshots show all four Ethernet links green.

![Initial Lab 2 topology and first router-interface setup; the right router link is still down at this stage](screenshots/lab-02/Screenshot%202026-11-15%20151610.png)

## 3. IP addressing plan

| Device | Interface | IPv4 address | Subnet mask | Default gateway |
|---|---|---|---|---|
| PC0 | FastEthernet0 | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| Router0 | GigabitEthernet0/0 | 192.168.10.1 | 255.255.255.0 | — |
| Router0 | GigabitEthernet0/1 | 192.168.20.1 | 255.255.255.0 | — |
| PC1 | FastEthernet0 | 192.168.20.10 | 255.255.255.0 | 192.168.20.1 |

- LAN-A network: **192.168.10.0/24**
- LAN-B network: **192.168.20.0/24**

## 4. Physical connections

Copper straight-through cables were used for these connections:

1. PC0 FastEthernet0 → Switch0 FastEthernet0/1
2. Switch0 FastEthernet0/24 → Router0 GigabitEthernet0/0
3. Router0 GigabitEthernet0/1 → Switch1 FastEthernet0/24
4. Switch1 FastEthernet0/1 → PC1 FastEthernet0

## 5. Router configuration

The following commands configured the two router interfaces:

```text
enable
configure terminal

interface gigabitEthernet 0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit

interface gigabitEthernet 0/1
ip address 192.168.20.1 255.255.255.0
no shutdown
exit

end
write memory
```

Verification command:

```text
show ip interface brief
```

The router configuration is shown in the following evidence screenshot:

![Router interface configuration for both LANs](screenshots/lab-02/Screenshot%202026-11-15%20151804.png)

The supplied router CLI verification screenshot shows:
- GigabitEthernet0/0 — 192.168.10.1 — up/up
- GigabitEthernet0/1 — 192.168.20.1 — up/up

![Router show ip interface brief output](screenshots/lab-02/Screenshot%202026-11-15%20151936.png)

## 6. Connectivity testing and observed results

### Test A — PC0 to PC1

Command:

```text
ping 192.168.20.10
```

The first captured run showed one initial timeout followed by three successful replies: 3 received, 1 lost (25% loss). This run demonstrates successful replies, but it was not a zero-loss result.

![PC0 to PC1 ping test with one initial timeout and three replies](screenshots/lab-02/Screenshot%202026-11-15%20152257.png)

### Test B — PC1 to PC0

Command:

```text
ping 192.168.10.10
```

The supplied screenshot shows:
- Packets sent: 4
- Packets received: 4
- Packets lost: 0 (0% loss)

![PC1 to PC0 ping test with four successful replies](screenshots/lab-02/Screenshot%202026-11-15%20152411.png)

**Result:** Communication from PC1 to PC0 was verified with 0% packet loss. The opposite direction also returned successful replies after one initial timeout.

## 7. What this lab demonstrates

- A router connects different IP networks.
- Each router interface acts as the default gateway for its directly connected LAN.
- Hosts use their default gateway when sending traffic to a different subnet.
- The router has directly connected routes for both configured networks.
- ICMP ping can test reachability between hosts on separate subnets.

## 8. Security and SOC relevance

Network segmentation separates devices into distinct IP networks. A SOC analyst should understand which gateway connects each segment and how traffic moves between them. This foundation is useful when investigating cross-subnet connections, unexpected communication paths, and access-control policies.

## 9. Completion checklist

- [x] Two separate LANs created.
- [x] Two PCs, two switches, and one Cisco 2911 router placed.
- [x] Host IP addresses and default gateways configured.
- [x] Router interfaces configured and verified up/up.
- [x] PC1 → PC0 ping verified (4/4, 0% loss).
- [x] PC0 → PC1 returned successful replies; first captured run had one initial timeout.
- [ ] Repeat PC0 → PC1 ping and capture a clean 4/4 result (optional stronger evidence).

## 10. Evidence screenshots

The five Packet Tracer screenshots embedded above provide evidence of:
1. The two-LAN topology and initial router setup.
2. Configuration of both router interfaces.
3. Router interface status using `show ip interface brief`.
4. PC0 → PC1 ping output (one initial timeout, then three replies).
5. PC1 → PC0 ping output (4/4 successful replies).

*The report records the results visible in the supplied screenshots and does not describe the first PC0 → PC1 ping as 0% loss.*
