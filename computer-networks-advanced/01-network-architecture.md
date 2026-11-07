# 01 — Advanced Network Architecture

## 1. What is network architecture?
Network architecture is the planned structure of a network: its devices, connections, addressing, routing, security boundaries, services and management. A good design is not simply one where computers can communicate. It must also be reliable, manageable, scalable and secure.

A cybersecurity professional studies architecture because security controls depend on where traffic enters, where it travels, which systems communicate and where trust boundaries exist.

## 2. Common enterprise layers
A traditional campus design often separates functions into:
- **Access layer:** connects end-user devices, printers, phones and wireless access points. Controls may include port security, 802.1X, VLAN assignment and edge protections.
- **Distribution layer:** aggregates access switches, applies routing and policy, and creates boundaries between groups.
- **Core layer:** provides fast, resilient transport between major network blocks. In smaller networks, distribution and core may be combined.

This is a logical design model, not a requirement that every network must have three physical layers.

## 3. Physical vs logical topology
Physical topology describes cables, ports, radios and device placement. Logical topology describes VLANs, IP subnets, routes, overlays and security zones. Two devices may be physically connected to the same switch but logically separated into different VLANs.

**Security example:** A finance laptop and a guest device may use the same access-switch hardware, but should not share the same trust zone or access policy.

## 4. Important design concepts
- **Availability:** redundant links/devices, power protection, tested backups and controlled change.
- **Confidentiality:** encryption, segmentation, restricted management access and secure wireless.
- **Integrity:** authenticated administration, configuration backups, monitoring and change control.
- **Scalability:** address plans, summarizable routes, consistent naming and capacity planning.
- **Least privilege:** allow only required communication, not broad access by default.
- **Defense in depth:** combine endpoint, network, identity, application and monitoring controls.

## 5. Trust boundaries and traffic flows
Draw the path from source to destination. Identify:
1. Source device and its VLAN/subnet
2. Default gateway
3. Routing/firewall points
4. Destination subnet and service
5. Identity and encryption controls
6. Logs available at each boundary

A firewall rule should be based on a business need: source, destination, protocol/port, direction and owner. “Allow any to any” hides risk and makes investigations harder.

## 6. North-south and east-west traffic
- **North-south:** traffic entering or leaving an environment, such as a user browsing an external website.
- **East-west:** traffic between internal systems, such as an application server connecting to a database.

Attackers who gain an initial foothold may move laterally using east-west paths. Internal traffic therefore deserves segmentation and monitoring too.

## 7. Network documentation
Maintain:
- Physical and logical diagrams
- IP address management (IPAM) records
- VLAN and subnet register
- Device inventory and owners
- Firewall/ACL rule register and business justification
- Network change log and configuration backups
- Critical service dependencies and recovery contacts

Do not put passwords or shared secrets in diagrams or ordinary documentation.

## Practical exercise: draw a small enterprise
Create four zones: Staff, Servers, Guest and Management. Give each zone a separate subnet. Draw gateways and a firewall boundary. Write down which flows are required (for example, Staff to approved application ports; Guest to internet only; Management to network-device admin interfaces from a dedicated admin host).

## Cybersecurity perspective
Ask these questions during a design review:
- Can a guest device reach internal servers?
- Can ordinary staff administer switches?
- Are management interfaces exposed to user networks?
- Can one compromised workstation reach every other workstation?
- Are DNS, DHCP and authentication services protected and monitored?
- Is there enough logging to reconstruct a security event?
