# Lab 03 — VLAN Segmentation (Admin and Sales)

**Status:** VLAN configuration and segmentation test completed.  
**Date performed:** 15 November 2026  
**Tool:** Cisco Packet Tracer  
**Switch:** Cisco Catalyst 2960  
**Topology:** Two PCs connected to one Layer 2 switch.

## 1. Objective

Create two separate VLANs on a Cisco 2960 switch, assign each PC's switch port to the correct VLAN, and test whether hosts in different VLANs can communicate without a Layer 3 device.

## 2. Topology

```text
                  Cisco 2960 Switch
                   /             \
                Fa0/1             Fa0/2
                 /                 \
        PC0 — Admin              PC1 — Sales
          VLAN 10                  VLAN 20
```

The Packet Tracer topology contains one switch and two PCs. Both physical links are shown as connected in the supplied screenshots.

![Lab 3 topology and initial VLAN creation on the switch](screenshots/lab-03/Screenshot%202026-11-15%20200354.png)

## 3. IP addressing plan

Both PCs were configured in the same IPv4 subnet for this Layer 2 VLAN demonstration.

| Device | Role | IPv4 address | Subnet mask | Default gateway |
|---|---|---|---|---|
| PC0 | Admin — VLAN 10 | 192.168.10.10 | 255.255.255.0 | Not configured |
| PC1 | Sales — VLAN 20 | 192.168.10.20 | 255.255.255.0 | Not configured |

No router or Layer 3 switch was included in this lab, so no default gateway was required for the intended test.

## 4. VLAN creation

The following commands created the two VLANs:

```text
enable
configure terminal

vlan 10
name admin
exit

vlan 20
name sale
exit

do show vlan brief
```

The initial VLAN verification screenshot shows VLAN 10 named `admin` and VLAN 20 named `sale`, both active. At this initial stage, the PC access ports had not yet been moved out of the default VLAN.

![Initial VLAN creation: VLAN 10 admin and VLAN 20 sale](screenshots/lab-03/Screenshot%202026-11-15%20200354.png)

## 5. Access-port assignment

PC0 was connected to switch port FastEthernet0/1 and assigned to VLAN 10. PC1 was connected to FastEthernet0/2 and assigned to VLAN 20.

Commands used:

```text
enable
configure terminal

interface fastEthernet 0/1
switchport mode access
switchport access vlan 10
exit

interface fastEthernet 0/2
switchport mode access
switchport access vlan 20
exit

do show vlan brief
```

The verification output shows:
- VLAN 10 — `admin` — active — Fa0/1
- VLAN 20 — `sale` — active — Fa0/2

![Access ports Fa0/1 and Fa0/2 assigned to VLAN 10 and VLAN 20](screenshots/lab-03/Screenshot%202026-11-15%20222333.png)

## 6. Connectivity testing

### Test A — PC0 to PC1

Command on PC0:

```text
ping 192.168.10.20
```

Observed result in the supplied screenshot:
- Packets sent: 4
- Packets received: 0
- Packets lost: 4 (100% loss)

![PC0 ping to PC1: four requests timed out](screenshots/lab-03/Screenshot%202026-11-15%20222636.png)

### Test B — PC1 to PC0

Command on PC1:

```text
ping 192.168.10.10
```

Observed result in the supplied screenshot:
- Packets sent: 4
- Packets received: 0
- Packets lost: 4 (100% loss)

![PC1 ping to PC0: four requests timed out](screenshots/lab-03/Screenshot%202026-11-15%20222905.png)

**Result:** Both ping tests failed, as expected for hosts placed in separate VLANs when no inter-VLAN routing is configured. VLANs create separate Layer 2 broadcast domains. Communication between VLAN 10 and VLAN 20 requires a router or Layer 3 switch with inter-VLAN routing configured.

## 7. Final VLAN verification

The final `show vlan brief` screenshot confirms the access-port assignments:

| VLAN ID | Name shown by switch | Status | Assigned port |
|---|---|---|---|
| 10 | admin | active | Fa0/1 |
| 20 | sale | active | Fa0/2 |

![Final show vlan brief output confirming VLAN 10 on Fa0/1 and VLAN 20 on Fa0/2](screenshots/lab-03/Screenshot%202026-11-15%20223248.png)

## 8. What this lab demonstrates

- A VLAN logically separates devices on the same physical switch.
- Each VLAN is a separate Layer 2 broadcast domain.
- Access ports are assigned to a specific VLAN.
- Hosts in different VLANs cannot communicate through a Layer 2 switch alone.
- Inter-VLAN communication requires Layer 3 routing.

## 9. Security and SOC relevance

VLANs help organize a network into separate logical segments, such as administration, sales, servers, and guest devices. Segmentation can reduce unnecessary Layer 2 exposure and support security boundaries. However, VLANs alone are not a complete security control: inter-VLAN traffic should also be controlled with appropriate Layer 3 access-control rules and monitoring.

## 10. Completion checklist

- [x] One Cisco 2960 switch and two PCs placed in Packet Tracer.
- [x] VLAN 10 created and named `admin`.
- [x] VLAN 20 created and named `sale`.
- [x] PC0 switch port Fa0/1 assigned to VLAN 10.
- [x] PC1 switch port Fa0/2 assigned to VLAN 20.
- [x] Final `show vlan brief` output verified.
- [x] PC0 → PC1 ping tested; 100% loss observed.
- [x] PC1 → PC0 ping tested; 100% loss observed.

## 11. Evidence screenshots

The five screenshots stored in [the Lab 3 screenshots folder](screenshots/lab-03/) are embedded in the relevant sections above:

1. `Screenshot 2026-11-15 200354.png` — topology and initial VLAN creation.
2. `Screenshot 2026-11-15 222333.png` — access-port assignment and VLAN verification.
3. `Screenshot 2026-11-15 222636.png` — PC0 → PC1 ping test (100% loss).
4. `Screenshot 2026-11-15 222905.png` — PC1 → PC0 ping test (100% loss).
5. `Screenshot 2026-11-15 223248.png` — final VLAN and port-assignment verification.

*The report uses the exact VLAN names and test results visible in the screenshots.*
