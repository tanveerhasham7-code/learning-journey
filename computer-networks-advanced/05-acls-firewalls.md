# 05 — ACLs, Firewalls and Traffic Filtering

## 1. Why filtering matters
Routing answers “where can this packet go?” Filtering answers “should this traffic be allowed?” An ACL or firewall policy compares traffic against ordered rules and takes an action such as permit, deny, reject or log.

## 2. ACL building blocks
A rule may match:
- Source and destination IP/prefix
- Protocol (TCP, UDP, ICMP, etc.)
- Source/destination port
- Interface and direction
- Connection state or application identity (on advanced firewalls)

Rules are evaluated according to platform behavior, often top-to-bottom with first match. Many ACL systems have an implicit deny at the end. Always verify the exact platform semantics.

## 3. Stateless ACL vs stateful firewall
A stateless filter evaluates each packet independently. A stateful firewall tracks connection state and can allow return traffic for an established permitted session. Next-generation firewalls may add application, user, URL and threat inspection, but encrypted traffic and false positives create limits.

## 4. Build policy from business requirements
Example policy:
- Staff may reach the internal application on its documented HTTPS port.
- Guest devices may reach approved internet services but not internal subnets.
- Only an admin workstation may access network-device management.
- Application servers may reach the database on its required database port.
- All other inter-zone traffic is denied and appropriately logged.

Avoid writing “allow all” as a shortcut. Document the owner, purpose, source, destination, service, expiry/review date and logging requirement for each rule.

## 5. Inbound, outbound and inter-zone controls
- Inbound: traffic entering a zone/device.
- Outbound: traffic leaving a zone/device.
- Inter-zone: traffic moving between security zones.
- Egress filtering: restricts what internal systems can send out, reducing command-and-control and data-exfiltration paths.

## 6. Rule hygiene
Use least privilege, specific objects, meaningful names, comments, change approval, periodic recertification and hit-count review. Remove obsolete rules after confirming they are unused. Logging every packet can overwhelm storage; log meaningful denies and high-risk allows according to policy.

## 7. Example policy matrix
| Source | Destination | Service | Decision |
|---|---|---|---|
| Staff | Application server | TCP 443 | Allow |
| Staff | Database subnet | Any | Deny |
| Application server | Database | Required DB port | Allow |
| Guest | Internal subnets | Any | Deny |
| Admin workstation | Network management | Approved admin protocols | Allow |
| Any other inter-zone flow | Any | Any | Deny and log as appropriate |

Ports must be selected for the actual application and environment; the table is a design example, not a universal production configuration.

## Practical lab
In Packet Tracer or a firewall simulator, create Staff, Server, Guest and Management zones. Implement the policy matrix. Test both allowed and denied flows. Capture screenshots of rule order and test results. Then intentionally create a too-broad rule in the simulator, observe why it violates least privilege, and correct it.

## Cybersecurity investigation
When a connection fails, check source/destination, route, DNS, host firewall, network firewall, NAT and application listener. A firewall deny log is evidence of a policy decision, not automatically evidence of an attack.
