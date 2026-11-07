# 02 — Switching, VLANs, Trunks, STP and EtherChannel

## 1. How an Ethernet switch forwards frames
A Layer 2 switch learns source MAC addresses and associates them with ingress ports in a MAC/CAM table. When a frame arrives, the switch:
1. Learns or refreshes the source MAC-to-port mapping.
2. Looks up the destination MAC.
3. Forwards a known unicast frame to the matching port.
4. Floods an unknown unicast or broadcast within the same VLAN (subject to protocol behavior).
5. Does not normally forward a Layer 2 frame between VLANs.

A MAC table is dynamic and entries age out. Attackers may attempt MAC-table exhaustion or spoofing; mitigations include port security, sensible port limits, 802.1X and monitoring.

## 2. VLANs
A Virtual LAN creates a logical Layer 2 broadcast domain. VLANs separate groups even when they share physical switching hardware.

Example plan:
| VLAN | Purpose | Example subnet |
|---|---|---|
| 10 | Staff | 192.168.10.0/24 |
| 20 | Servers | 192.168.20.0/24 |
| 30 | Guest | 192.168.30.0/24 |
| 99 | Network management | 192.168.99.0/24 |

A VLAN is not automatically a complete security boundary. Inter-VLAN routing, firewall policy, switch configuration and endpoint controls determine what can communicate.

## 3. Access ports and trunk ports
- **Access port:** normally carries traffic for one assigned VLAN to an endpoint.
- **Trunk port:** carries multiple VLANs between network devices using VLAN tagging, commonly IEEE 802.1Q.
- **Native VLAN:** on an 802.1Q trunk, frames for the native VLAN are transmitted untagged by default on many platforms. Configure it deliberately and consistently.

Security practices: disable unused ports, place them in an unused isolated VLAN, restrict allowed VLANs on trunks, avoid using the default VLAN for user traffic, and disable automatic trunk negotiation where supported.

## 4. Inter-VLAN routing
Devices in different IPv4 subnets need a Layer 3 device to route between them. Common designs:
- Separate router interface per VLAN
- Router-on-a-stick using a trunk and router subinterfaces
- Layer 3 switch with switched virtual interfaces (SVIs)

Routing creates an opportunity to enforce policy. Put ACLs or firewall rules at the boundary and permit only documented flows.

## 5. Spanning Tree Protocol (STP)
Redundant Layer 2 links can create loops. Loops may cause broadcast storms, duplicate frames and MAC-table instability. STP builds a loop-free logical topology by selecting a root bridge and placing some redundant paths into a non-forwarding state.

Important ideas: bridge ID, root bridge, root port, designated port, path cost and topology changes. RSTP (802.1w) improves convergence compared with classic STP.

Edge protections on supported switches:
- **PortFast/edge mode:** lets an endpoint-facing port transition quickly; use only on true edge ports.
- **BPDU Guard:** disables/protects an edge port if it receives a BPDU, helping prevent an unauthorized switch from joining.
- **Root Guard:** helps prevent an unexpected switch from becoming root.
- **Loop Guard:** helps protect against certain unidirectional-link/STP failures.

Exact commands vary by vendor and model. Verify the platform documentation before applying configuration.

## 6. Link aggregation / EtherChannel
Combines multiple physical links into one logical link for capacity and redundancy. LACP (IEEE 802.1AX, historically 802.3ad) negotiates aggregation. Both ends need compatible speed, duplex, VLAN and trunk settings. Aggregation does not mean one single flow always uses all links; hashing distributes flows.

## 7. Verification (simulator or owned switch)
Typical Cisco-like read-only checks:
```text
show mac address-table
show vlan brief
show interfaces trunk
show spanning-tree
show etherchannel summary
show interfaces status
```
Do not paste vendor-specific commands into production without checking syntax and change approval.

## Lab tasks
1. Create VLANs 10, 20, 30 and 99.
2. Assign endpoint ports to access VLANs.
3. Configure a trunk between two switches and allow only required VLANs.
4. Verify VLAN membership and trunk status.
5. Add a redundant link in the simulator and observe STP behavior.
6. Enable edge protections on simulated access ports and document the effect.
7. Build an LACP bundle in a simulator and verify its state.

## Security review
Explain how VLAN hopping, rogue switches, unauthorized trunking, STP manipulation and unmanaged access ports could create risk. For each, identify a prevention control and a monitoring clue. Keep demonstrations inside a simulator; do not attempt disruptive Layer 2 attacks on a live network.
