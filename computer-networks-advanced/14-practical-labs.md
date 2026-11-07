# 14 — Practical Lab Workbook (16 Labs)

## Before every lab
- Use Packet Tracer, a local simulator or isolated VMs you own.
- Snapshot VMs before changes.
- Record the lab scope and addresses.
- Never scan or capture third-party networks.
- Save sanitized screenshots and actual outputs.
- Use the [lab report template](LAB-REPORT-TEMPLATE.md).

## Lab 01 — Build a segmented office network
**Goal:** create Staff, Servers, Guest and Management zones.
**Tasks:** draw topology; assign VLANs/subnets; configure access ports and gateways; test required flows.
**Evidence:** topology, VLAN table, successful and blocked test results.
**Security question:** why should guest devices not reach server management?

## Lab 02 — Configure 802.1Q trunking
**Goal:** carry multiple VLANs between two simulated switches.
**Tasks:** create VLANs; configure trunk; restrict allowed VLAN list; verify trunk and endpoint connectivity.
**Evidence:** sanitized configuration and trunk output.
**Security question:** what can go wrong if every VLAN is allowed unnecessarily?

## Lab 03 — Observe STP
**Goal:** understand loop prevention.
**Tasks:** create redundant Layer 2 links in a simulator; inspect root bridge and port states; change root preference; observe topology.
**Evidence:** STP output before/after.
**Safety:** do not create loops on a live network.

## Lab 04 — Inter-VLAN routing and ACL policy
**Goal:** route between zones while limiting access.
**Tasks:** configure SVIs or router-on-a-stick; allow only required application traffic; test denied traffic.
**Evidence:** route table, policy matrix and test results.

## Lab 05 — Static routing
**Goal:** connect multiple routed networks.
**Tasks:** build two or three routers; configure static/default routes; test end-to-end reachability; remove one route and diagnose.
**Evidence:** route tables and traceroute.

## Lab 06 — OSPF neighbor and route learning
**Goal:** understand dynamic routing.
**Tasks:** configure OSPF in a simulator; verify neighbors; inspect learned routes; simulate a link failure.
**Evidence:** neighbor state and route changes.
**Security question:** how would an unexpected neighbor be investigated?

## Lab 07 — IPv6 addressing and NDP
**Goal:** configure IPv6 on two LANs.
**Tasks:** assign documentation prefixes; configure gateway; inspect neighbor cache and ICMPv6; verify routing.
**Evidence:** IPv6 addresses, routes and packet capture.

## Lab 08 — DHCP DORA capture
**Goal:** observe address assignment.
**Tasks:** use a lab DHCP server/client; capture Discover, Offer, Request and Acknowledge; identify lease options.
**Evidence:** sanitized packet list and explanation.
**Security question:** what is a rogue DHCP server and how can a switch help prevent it?

## Lab 09 — DNS resolution investigation
**Goal:** understand recursive resolution and DNS records.
**Tasks:** query A, AAAA, MX and PTR records using a test domain; capture DNS traffic; compare successful and failed lookup.
**Evidence:** command output and packet details.
**Security question:** what DNS telemetry may help detect suspicious activity?

## Lab 10 — Wireshark TCP and TLS analysis
**Goal:** identify a TCP handshake and TLS metadata.
**Tasks:** generate an HTTPS request to a service you are allowed to use; capture only your own lab traffic; filter SYN/SYN-ACK/ACK and TLS handshake.
**Evidence:** annotated screenshots; do not publish session cookies or private data.

## Lab 11 — Authorized Nmap asset inventory
**Goal:** identify services on one lab VM.
**Tasks:** write scope; scan one host-only VM; identify open/closed/filtered ports; validate service with VM configuration.
**Evidence:** sanitized output and inventory table.
**Safety:** never scan a public or third-party target.

## Lab 12 — Firewall rule validation
**Goal:** implement least privilege.
**Tasks:** create Staff, App, DB and Guest zones; permit only documented service flows; test allowed/denied cases; inspect logs.
**Evidence:** flow matrix, rules and results.

## Lab 13 — VPN route and access review
**Goal:** understand a private tunnel.
**Tasks:** in a private lab, establish a supported VPN between systems you control or use a simulator; inspect routes and allowed subnets; test access boundaries.
**Evidence:** sanitized route table and design diagram. Never publish keys or credentials.

## Lab 14 — Network monitoring mini-SOC
**Goal:** build a simple event timeline.
**Tasks:** use synthetic DNS, DHCP, firewall and endpoint events; normalize timestamps; correlate source IP and device; write observations.
**Evidence:** sanitized timeline and analyst notes.
**Security question:** why is one suspicious DNS event not enough to confirm compromise?

## Lab 15 — Troubleshooting challenge
**Goal:** isolate network faults systematically.
**Tasks:** introduce one fault in a simulator (wrong VLAN, gateway, route or DNS); use layered tests; fix and verify.
**Evidence:** symptom, hypothesis, commands, root cause and resolution.

## Lab 16 — Secure network design review
**Goal:** assess an office network as a defender.
**Tasks:** review a simulated diagram; identify flat segments, exposed management, weak wireless, broad rules and missing telemetry; prioritize remediation.
**Evidence:** risk register with severity, impact, recommendation and owner.

## Lab completion record
For each lab, record status as **Not started**, **In progress** or **Completed with evidence**. Do not claim completion until you have performed the exercise and retained evidence.
