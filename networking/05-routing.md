# 05 — Routing

## What is routing?
Routing moves IP packets between different networks. A router or Layer 3 switch checks the destination IP and selects a next hop or outgoing interface using its routing table.

## Routing table concepts
- Destination prefix
- Next-hop address or outgoing interface
- Metric/administrative preference
- Route source (connected, static, dynamic, default)

Routers use longest-prefix match: the most specific matching route is selected.

## Static routing
A network administrator manually configures routes. It is predictable and useful in small or stable networks, but does not automatically adapt to topology changes.

Cisco IOS-style example:
```text
ip route 192.168.20.0 255.255.255.0 10.0.0.2
show ip route
```
This says to reach 192.168.20.0/24 via next hop 10.0.0.2.

## Default route
A default route is used when no more specific route matches:
```text
ip route 0.0.0.0 0.0.0.0 10.0.0.1
```

## Dynamic routing overview
Dynamic routing protocols exchange route information:
- RIP: distance-vector, mainly educational/legacy.
- OSPF: link-state, widely used within an organization.
- BGP: path-vector, used between autonomous systems and by Internet routing.
Understand the purpose and concepts before attempting advanced configuration.

## Router-on-a-stick example
```text
interface gigabitEthernet 0/0
 no shutdown
interface gigabitEthernet 0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
interface gigabitEthernet 0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
```
The switch port connected to the router must be a trunk. Use interface names supported by your device.

## Lab
Create two LANs connected by two routers. Configure interface addresses, add static routes in both directions, set host gateways and verify with ping and traceroute. Inspect `show ip route`.
