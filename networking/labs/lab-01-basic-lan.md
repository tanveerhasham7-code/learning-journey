# Lab 01 — Build and Verify a Basic Switched LAN

**Status:** Partially verified — host-to-host connectivity and ARP evidence captured; switch MAC-table verification still needs to be repeated.

**Date performed:** 15 November 2026  
**Tool:** Cisco Packet Tracer  
**Device model:** Cisco 2960-24TT switch  
**Topology:** Two PCs connected to one Layer 2 switch

## 1. Objective

Build a small LAN, assign IPv4 addresses in the same subnet, test connectivity with ICMP ping, and inspect ARP and switch MAC-address learning.

## 2. Topology

```text
PC2 ---------------- Fa0/1
                         \
                          [Switch0 — Cisco 2960-24TT]
                         /
PC3 ---------------- Fa0/2
```

The Packet Tracer screenshot shows both access links up (green link indicators).

### Evidence screenshots

**1. Network topology and successful PC2-to-PC3 ping**

![Two-PC switched LAN topology and successful ping from PC2 to PC3 (4 replies, 0% loss)](screenshots/lab-01/Screenshot%202026-11-15%20132321.png)

This screenshot shows PC2 and PC3 connected to the Cisco 2960 switch, with both links up. The PC2 command prompt shows four successful replies from 192.168.10.20 (4/4 received, 0% loss).

**2. PC3 ARP cache output**

![PC3 ARP cache showing the dynamic entry for 192.168.10.10](screenshots/lab-01/Screenshot%202026-11-15%20133106.png)

This screenshot shows the output of `arp -a` on PC3. It contains a dynamic entry for 192.168.10.10 with physical address 0010.1114.232a.

**3. Switch MAC address table — verification pending**

![Switch0 CLI showing show mac address-table with no learned MAC rows in this capture](screenshots/lab-01/Screenshot%202026-11-15%20133350.png)

This screenshot shows the Cisco 2960 switch CLI after running `show mac address-table`. The table headings are visible, but no learned MAC-address rows appear. Therefore, switch MAC-table learning is not marked as verified yet.



## 3. IP addressing plan

| Device | IPv4 address | Subnet mask | Default gateway |
|---|---|---|---|
| PC2 | 192.168.10.10 | 255.255.255.0 (/24) | Not required for this same-subnet test |
| PC3 | 192.168.10.20 | 255.255.255.0 (/24) | Not required for this same-subnet test |

Both hosts are in network **192.168.10.0/24**. Since they communicate within the same subnet, a router/default gateway is not needed for this test.

## 4. Configuration and test procedure

1. Place two PCs and one Cisco 2960 switch in the Packet Tracer workspace.
2. Connect PC2 to switch port FastEthernet0/1 and PC3 to FastEthernet0/2 using copper straight-through links.
3. Configure PC2 as `192.168.10.10 / 255.255.255.0`.
4. Configure PC3 as `192.168.10.20 / 255.255.255.0`.
5. From PC2, open **Desktop → Command Prompt** and run:

   ```text
   ping 192.168.10.20
   ```

6. On a PC, inspect the ARP cache:

   ```text
   arp -a
   ```

7. On the switch CLI, inspect the learned MAC-address table:

   ```text
   enable
   show mac address-table
   ```

## 5. Observed results

### 5.1 ICMP connectivity — successful

The captured ping output shows four replies from **192.168.10.20**:

- Sent: 4
- Received: 4
- Lost: 0 (0% loss)
- Reported round-trip time: 0–1 ms

**Result:** The two hosts successfully communicated over the switched LAN.

### 5.2 ARP cache — neighbor entry observed

The captured `arp -a` output shows this dynamic entry:

| Internet address | Physical address | Type |
|---|---|---|
| 192.168.10.10 | 0010.1114.232a | dynamic |

This is evidence that the PC displaying the ARP output had learned a MAC address for **192.168.10.10**. ARP maps an IPv4 address to a local-link MAC address so an Ethernet frame can be delivered to the correct host.

### 5.3 Switch MAC-address table — pending recheck

The captured `show mac address-table` output displayed the table headings but no learned MAC-address rows.

**Do not treat this check as passed yet.** The screenshot does not prove that the switch table was populated at that moment. Repeat the ping, then run the command again:

```text
enable
show mac address-table
```

Expected after the switch has processed frames: dynamically learned MAC addresses should appear against the corresponding switch ports (expected access ports: **Fa0/1** and **Fa0/2**). The actual MAC values will depend on the Packet Tracer end devices.

## 6. Concepts demonstrated

- **LAN:** Devices connected within a local network.
- **Ethernet switching:** The switch forwards frames using learned MAC-address-to-port information.
- **IPv4 subnet:** Both hosts use addresses in the same /24 network.
- **ICMP:** The ping test uses ICMP Echo Request and Echo Reply messages to test reachability.
- **ARP:** A host discovers the MAC address associated with a local IPv4 address.
- **Default gateway:** Not needed for communication between these two hosts in the same subnet.

## 7. Security relevance

A SOC analyst may use ARP and switch MAC-address information during basic network investigation to understand which local devices are communicating and which switch ports have learned their MAC addresses. Unexpected IP-to-MAC changes, duplicate IP symptoms, or unfamiliar devices can warrant investigation; these observations alone do not prove malicious activity.

## 8. Evidence and completion checklist

- [x] Two-PC, one-switch topology created.
- [x] Both switch links shown as up in Packet Tracer.
- [x] PC-to-PC ping successful (4/4 replies, 0% loss).
- [x] ARP cache contains a dynamic neighbor entry for 192.168.10.10.
- [ ] Switch MAC-address table shows learned entries on the expected ports — repeat and capture output.

## 9. Next action

Repeat the ping from PC2 to PC3, then immediately run `show mac address-table` on Switch0. Save a screenshot showing the learned MAC entries and ports. Once that evidence is captured, mark the final checklist item complete.

---
*This report records only the results visible in the supplied Packet Tracer screenshots. The switch MAC-table verification is intentionally left pending.*
