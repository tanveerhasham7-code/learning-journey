# 03 — Routing, Route Selection and OSPF

## 1. What routing does
A router forwards IP packets between networks. It examines the destination IP address, consults its routing table and selects the most specific matching route (longest-prefix match). If no route matches, it may use a default route or drop the packet.

A routing table commonly contains destination prefix, next hop, outgoing interface, metric and route source.

## 2. Static and dynamic routing
**Static route:** manually configured by an administrator. It is predictable and useful for small/stub networks, but changes must be managed manually.

**Dynamic routing:** routers exchange reachability information using a routing protocol. It can adapt to topology changes, but requires secure design, correct configuration and monitoring.

A default route (0.0.0.0/0 for IPv4) is used when no more-specific route exists. IPv6 default route is ::/0.

## 3. Metrics and route selection
Routing protocols use metrics to compare paths. Do not confuse:
- **Administrative distance / route preference:** which route source is trusted when multiple sources advertise the same prefix (vendor terminology differs).
- **Metric:** which path is preferred within a routing protocol.
- **Longest-prefix match:** which destination prefix best matches the packet.

## 4. OSPF overview
Open Shortest Path First is a link-state interior gateway protocol. Routers discover neighbors, exchange link-state information, build a link-state database (LSDB) and run the Shortest Path First algorithm to calculate paths.

Key terms:
- Router ID: unique 32-bit identifier in dotted-decimal form.
- Neighbor adjacency: relationship formed between OSPF routers under compatible settings.
- Hello packets: discover and maintain neighbors.
- Area: logical OSPF grouping; Area 0 is the backbone in a multi-area design.
- LSA: Link-State Advertisement describing topology information.
- Cost: OSPF path metric, commonly derived from interface bandwidth.
- DR/BDR: designated and backup designated routers on applicable multi-access networks.

Neighbors must agree on relevant parameters such as area, timers, authentication settings (where used), network type and compatible subnet information. Mismatches can prevent adjacency.

## 5. OSPF security and reliability
- Use supported OSPF authentication where available and designed.
- Do not form adjacencies on untrusted user-facing interfaces.
- Make endpoint-facing interfaces passive where appropriate.
- Filter and summarize routes carefully at design boundaries.
- Monitor unexpected neighbor changes, new LSAs and route changes.
- Protect router management planes with restricted admin access and secure protocols.
- Keep configurations backed up and changes reviewed.

Authentication protects protocol exchanges but does not replace segmentation or device security.

## 6. Verification concepts
On a Cisco-like simulator, common checks include:
```text
show ip route
show ip ospf neighbor
show ip ospf interface
show ip protocols
traceroute <destination>
ping <destination>
```
Use only in your own simulator or authorized devices.

## Practical lab
Build three routers in a triangle with three LANs. Configure addressing, then static routes. Verify end-to-end reachability and inspect the routing table. Replace static routes with OSPF area 0, confirm neighbor relationships and learned routes, then simulate one link failure and observe reconvergence.

## Troubleshooting OSPF
Check physical/link state, IP/mask, interface enablement, area, timers, authentication, network type, router ID uniqueness and passive-interface settings. A ping failure alone does not prove OSPF is broken; test each hop and inspect the route table.

## Cybersecurity analyst view
A route change can redirect or black-hole traffic. During an incident, compare current routes and neighbor state with approved baselines. Investigate unexpected routing peers, default-route changes and unexplained path changes.
