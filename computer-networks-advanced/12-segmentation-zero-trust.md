# 12 — Network Segmentation and Zero Trust

## 1. Segmentation
Segmentation divides a network into smaller zones to limit unnecessary communication. It can be implemented with VLANs, subnets, routers, firewalls, host firewalls, private virtual networks and software-defined controls.

Segmentation reduces blast radius. If a guest device is compromised, it should not automatically be able to reach domain controllers, databases or management interfaces.

## 2. Macro and micro segmentation
- **Macro segmentation:** separates broad zones such as users, servers, guests and management.
- **Microsegmentation:** applies more granular controls between workloads, applications or individual systems.

## 3. Zero Trust principles
Zero Trust is an approach, not a single product. It avoids granting trust solely because a device is inside a corporate network. Access decisions consider identity, device health, resource sensitivity, context and policy. Access should be explicit, least-privileged and continuously evaluated where practical.

## 4. Example zone policy
| Zone | May initiate to | Should not initiate to |
|---|---|---|
| Guest | Approved internet services | Staff, server and management zones |
| Staff | Required business applications | Network management and database admin |
| App servers | Required database/service ports | User workstation ranges without reason |
| Management | Network device admin interfaces | General browsing from device management plane |

Actual policy must reflect application dependencies and business needs.

## 5. Common mistakes
- VLANs created but unrestricted routing remains
- Management interfaces reachable from user networks
- Flat server networks
- Broad firewall rules left indefinitely
- No asset owner or rule review date
- IPv6 path ignored
- Monitoring not updated after segmentation

## Practical lab
Create Staff, Guest, Application, Database and Management segments in a simulator. Write a flow matrix first, implement only required flows, and test both permitted and denied connections. Document any application dependency that required a rule change.

## Security validation
Use an approved test matrix and confirm controls from both sides of a boundary. A denied ping does not prove all traffic is blocked; test the specific required protocols and inspect firewall logs. Avoid disruptive testing outside the lab.
