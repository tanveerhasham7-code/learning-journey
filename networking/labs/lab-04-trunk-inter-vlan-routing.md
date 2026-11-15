# Lab 04 — Trunk and Inter-VLAN Routing

**Status:** Inter-VLAN routing configured and tested; ACL restriction task is pending.  
**Date performed:** 15 November 2026  
**Tool:** Cisco Packet Tracer  
**Devices:** Cisco 2911 router, Cisco Catalyst 2960 switch, and two PCs  
**Method:** Router-on-a-Stick using 802.1Q subinterfaces

## 1. Objective

Configure a trunk link between a Cisco 2960 switch and a Cisco 2911 router, create router subinterfaces for VLAN 10 (Admin) and VLAN 20 (Sales), and verify communication between the two VLANs.

The final exercise also calls for an ACL to restrict traffic from Sales to Admin. That ACL task has **not yet been completed**, so this report does not mark the entire lab as finished.

## 2. Topology

The Packet Tracer topology contains one router connected to one switch. Two end devices connect to the switch on separate access ports.

- PC2 — Admin, VLAN 10, switch port Fa0/1
- PC3 — Sales, VLAN 20, switch port Fa0/2
- Router1 — Cisco 2911, connected to the switch using GigabitEthernet0/0
- Switch1 — Cisco 2960, router-facing trunk port GigabitEthernet0/1

![Lab 4 topology and switch trunk configuration](screenshots/lab-04/Screenshot%202026-11-15%20230935.png)

The screenshot shows the router-switch-PC topology and the switch CLI accepting `switchport mode trunk` and `no shutdown` on GigabitEthernet0/1.

## 3. VLAN and IP addressing plan

The two VLANs were created on the switch and the PC-facing ports were assigned as access ports.

| Device / VLAN | Role | IPv4 address | Subnet mask | Default gateway |
|---|---|---|---|---|
| PC2 — VLAN 10 | Admin | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| PC3 — VLAN 20 | Sales | 192.168.20.10 | 255.255.255.0 | 192.168.20.1 |
| Router subinterface G0/0.10 | VLAN 10 gateway | 192.168.10.1 | 255.255.255.0 | — |
| Router subinterface G0/0.20 | VLAN 20 gateway | 192.168.20.1 | 255.255.255.0 | — |

VLAN names used on the switch:
- VLAN 10 — `admin`
- VLAN 20 — `sale`

## 4. Switch access-port and trunk configuration

The PC-facing switch ports were configured as access ports:

```text
enable
configure terminal

vlan 10
name admin
exit

vlan 20
name sale
exit

interface fastEthernet 0/1
switchport mode access
switchport access vlan 10
exit

interface fastEthernet 0/2
switchport mode access
switchport access vlan 20
exit
```

The router-facing switch port was configured as a trunk:

```text
interface gigabitEthernet 0/1
switchport mode trunk
no shutdown
end
```

The switch CLI screenshot shows the trunk-mode command accepted on GigabitEthernet0/1. A separate `show interfaces trunk` output was not captured; the Packet Tracer command was not working in this session.

![Switch GigabitEthernet0/1 trunk command entered successfully](screenshots/lab-04/Screenshot%202026-11-15%20230935.png)

## 5. Router physical interface

The router's GigabitEthernet0/0 interface was enabled:

```text
enable
configure terminal
interface gigabitEthernet 0/0
no shutdown
exit
```

The router CLI confirms that GigabitEthernet0/0 and its line protocol changed to the up state. The screenshot also shows an initial mistyped `exir` command returning an error; it was corrected by entering `exit`.

![Router GigabitEthernet0/0 enabled and link state changed to up](screenshots/lab-04/Screenshot%202026-11-15%20231344.png)

## 6. Router-on-a-Stick subinterfaces

Two 802.1Q subinterfaces were configured on the router.

### VLAN 10 — Admin

```text
interface gigabitEthernet 0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
```

### VLAN 20 — Sales

```text
interface gigabitEthernet 0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0
no shutdown
exit
end
```

The screenshot shows both subinterfaces being created with the correct VLAN tags and gateway addresses.

![Router subinterfaces G0/0.10 and G0/0.20 configured with 802.1Q encapsulation](screenshots/lab-04/Screenshot%202026-11-15%20231747.png)

## 7. Router interface verification

The command `show ip interface brief` was used to verify the router interfaces.

Observed output in the screenshot:

| Interface | IP address | Status | Protocol |
|---|---|---|---|
| GigabitEthernet0/0 | Unassigned | up | up |
| GigabitEthernet0/0.10 | 192.168.10.1 | up | up |
| GigabitEthernet0/0.20 | 192.168.20.1 | up | up |

This confirms that the physical interface and both VLAN subinterfaces were up/up at the time of verification.

![show ip interface brief showing the physical interface and both VLAN subinterfaces up/up](screenshots/lab-04/Screenshot%202026-11-15%20231802.png)

## 8. Connectivity testing

### Test A — Admin (PC2) to Sales (PC3)

Command run on PC2:

```text
ping 192.168.20.10
```

Observed result:
- Packets sent: 4
- Packets received: 3
- Packets lost: 1
- Packet loss: 25%

The first request timed out and the next three received replies. This can occur during the first test while ARP address resolution is taking place. The three successful replies show that traffic reached the Sales PC.

![PC2 ping to 192.168.20.10: three replies and one initial timeout](screenshots/lab-04/Screenshot%202026-11-15%20232217.png)

### Test B — Sales (PC3) to Admin (PC2)

Command run on PC3:

```text
ping 192.168.10.10
```

Observed result:
- Packets sent: 4
- Packets received: 4
- Packets lost: 0
- Packet loss: 0%

All four replies were successful.

![PC3 ping to 192.168.10.10: four successful replies and 0 percent packet loss](screenshots/lab-04/Screenshot%202026-11-15%20232345.png)

**Connectivity result:** Inter-VLAN communication was demonstrated in both directions. The first test had one initial timeout (25% loss), followed by three successful replies; the reverse test completed with 0% packet loss.

## 9. What this lab demonstrates

- A switch trunk carries traffic for multiple VLANs over one physical link.
- 802.1Q tags identify the VLAN associated with each Ethernet frame on the trunk.
- Router subinterfaces provide Layer 3 gateways for separate VLANs.
- Router-on-a-Stick allows a single physical router interface to route between multiple VLANs.
- The router's subinterfaces must be up and correctly addressed for inter-VLAN communication.

## 10. Security relevance

VLANs provide logical network separation, but they do not by themselves enforce a complete security boundary. Inter-VLAN traffic should be restricted according to business requirements using ACLs or a firewall, and important traffic should be monitored.

## 11. Pending work

The original lab also requires restricting traffic initiated from Sales (VLAN 20) toward Admin (VLAN 10) with an extended ACL, while allowing other traffic as intended.

- [x] Create VLAN 10 (admin) and VLAN 20 (sale).
- [x] Assign PC-facing access ports to the correct VLANs.
- [x] Configure the switch router-facing port as a trunk.
- [x] Enable router GigabitEthernet0/0.
- [x] Configure VLAN 10 and VLAN 20 router subinterfaces.
- [x] Verify router interfaces with `show ip interface brief`.
- [x] Test Admin-to-Sales connectivity.
- [x] Test Sales-to-Admin connectivity before applying an ACL.
- [ ] Configure the extended ACL to restrict Sales-to-Admin traffic.
- [ ] Verify that Sales-to-Admin traffic is blocked and Admin-to-Sales traffic remains allowed.

**Overall status:** Inter-VLAN routing portion verified; ACL portion remains pending. The lab should be marked fully completed only after the ACL is configured and tested.

## 12. Evidence screenshots

All six screenshots are stored in the [Lab 4 screenshots folder](screenshots/lab-04/), and each is embedded beside the matching explanation above:

1. `Screenshot 2026-11-15 230935.png` — topology and switch trunk configuration.
2. `Screenshot 2026-11-15 231344.png` — router physical interface enabled.
3. `Screenshot 2026-11-15 231747.png` — VLAN 10 and VLAN 20 router subinterfaces configured.
4. `Screenshot 2026-11-15 231802.png` — router interface status verification.
5. `Screenshot 2026-11-15 232217.png` — Admin-to-Sales ping; one initial timeout and three replies.
6. `Screenshot 2026-11-15 232345.png` — Sales-to-Admin ping; four successful replies.

*Descriptions and test results are based on the screenshots reviewed from the repository and the configuration steps completed during this lab session.*
