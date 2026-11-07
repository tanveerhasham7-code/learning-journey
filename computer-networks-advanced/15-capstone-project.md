# 15 — Capstone: Design and Defend a Small Enterprise Network

## Scenario
A fictional organization has four teams: Administration, Sales, IT and Guest users. It runs an internal application and a database. Network administrators need a dedicated management path. Your task is to design a network that is usable, segmented, observable and resilient.

## Required deliverables
1. **Requirements:** list users, applications, services, availability needs and constraints.
2. **Topology:** logical and physical diagrams showing switches, router/firewall, APs, servers and zones.
3. **Address plan:** IPv4 subnet table and an IPv6 strategy. Use documentation/private ranges in the lab.
4. **VLAN plan:** separate user, server, guest and management segments.
5. **Routing:** explain gateways, static/dynamic routing choice and default route.
6. **Security policy:** flow matrix with source, destination, service, action, reason and owner.
7. **Infrastructure services:** DNS, DHCP, NTP and centralized logging plan.
8. **Wireless:** staff and guest design, authentication and isolation.
9. **Monitoring:** events and metrics that would help detect misuse or outages.
10. **Validation:** test cases for allowed and denied communication.
11. **Risk register:** identify at least eight risks, likelihood, impact and mitigation.
12. **Operations:** backup, change control, patching and incident escalation notes.

## Suggested address plan
Use a private lab block such as 10.20.0.0/16 and divide it into appropriate subnets. Example only:
| Zone | Example subnet |
|---|---|
| Administration | 10.20.10.0/24 |
| Sales | 10.20.20.0/24 |
| IT | 10.20.30.0/24 |
| Servers | 10.20.40.0/24 |
| Guest | 10.20.50.0/24 |
| Management | 10.20.99.0/24 |

Change the plan if your simulator requires different addressing. Do not use these sample ranges on a real network without checking for conflicts.

## Minimum security requirements
- Guest devices cannot initiate connections to internal business zones.
- User devices cannot directly administer network infrastructure.
- Only the required application-to-database flow is allowed.
- Management interfaces are reachable only from a dedicated admin path.
- DNS and time services are defined and monitored.
- Network device configurations are backed up securely.
- IPv4 and IPv6 policy are both considered.
- Denied and high-risk traffic is logged without creating unmanageable noise.

## Validation matrix
For each required flow, test:
- Expected allowed case
- Expected denied case
- Correct source/destination and port
- Relevant firewall/ACL log
- Whether the application actually works

A successful ping is not sufficient to validate an application policy. Test the actual required service.

## Final report structure
1. Executive summary
2. Requirements and assumptions
3. Topology and address plan
4. Routing and switching design
5. Security zones and policy matrix
6. Monitoring and incident visibility
7. Test results and evidence
8. Risk register and remediation priorities
9. Limitations and future improvements
10. Lessons learned

## Portfolio honesty
This repository provides the project brief and design framework. Add your own topology, configurations, screenshots and test results after completing the work. Clearly label simulated results as simulated. Do not claim a production deployment.
