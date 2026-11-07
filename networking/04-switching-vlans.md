# 04 — Switching, VLANs and Trunking

## Ethernet switching
A switch learns source MAC addresses and associates them with ports in its MAC address table. It forwards known unicast frames toward the learned port, floods unknown unicast and broadcast frames within the VLAN, and filters frames where appropriate.

## VLAN
A Virtual LAN separates one physical switch into multiple logical Layer 2 broadcast domains. VLANs help segment departments, devices and security zones.

Example plan:
- VLAN 10 — Administration — 192.168.10.0/24
- VLAN 20 — Sales — 192.168.20.0/24
- VLAN 30 — IT — 192.168.30.0/24
- VLAN 99 — Management (example only)

## Access and trunk ports
- Access port: normally carries traffic for one assigned VLAN to an endpoint.
- Trunk port: carries multiple VLANs between network devices, commonly using IEEE 802.1Q tags.

## Example Cisco IOS-style configuration
Commands vary by device/model and simulator. In Packet Tracer switch CLI:

```text
enable
configure terminal
vlan 10
 name ADMIN
vlan 20
 name SALES
vlan 30
 name IT
interface fastEthernet 0/1
 switchport mode access
 switchport access vlan 10
interface fastEthernet 0/2
 switchport mode access
 switchport access vlan 20
interface gigabitEthernet 0/1
 switchport mode trunk
end
show vlan brief
show interfaces trunk
show mac address-table
```

Some switch models require additional trunk encapsulation or use different interface names. Check the platform syntax.

## Inter-VLAN routing
Devices in different VLANs need a Layer 3 device to communicate. Options include:
- Router-on-a-stick: router subinterfaces over an 802.1Q trunk.
- Layer 3 switch: switched virtual interfaces (SVIs) route between VLANs.

## Security considerations
- Put unused ports in an unused VLAN and administratively shut them down.
- Do not leave user ports as trunks.
- Restrict allowed VLANs on trunks.
- Use a dedicated management VLAN and secure management access.
- Consider DHCP snooping, Dynamic ARP Inspection and port security where supported.
- Avoid VLAN 1 for user and management traffic in a hardened design.

## Lab verification
Check VLAN membership, trunk state, MAC learning and reachability. Confirm hosts in separate VLANs cannot communicate until routing and policy permit it.
