# 09 — Build a Safe Networking Lab

## Option A: Cisco Packet Tracer (best first step)
1. Install Packet Tracer from Cisco Networking Academy after creating an account.
2. Create a new project.
3. Add two PCs and one 2960-style switch.
4. Connect PCs to switch using copper straight-through links.
5. Assign IPs in the same subnet and test ping.
6. Save the .pkt file and take screenshots of topology and successful tests.

Use Packet Tracer for VLANs, trunks, router-on-a-stick, static routing, DHCP, ACL concepts and basic troubleshooting. It simulates network devices; it is not a full production router OS.

## Option B: VirtualBox host-only lab
Suggested isolated design:
- Kali or Ubuntu analyst VM: 192.168.56.10/24
- Ubuntu server VM: 192.168.56.20/24
- Optional Windows evaluation VM: 192.168.56.30/24

Use a Host-only network or Internal Network for isolated practice. Give the VMs unique addresses or use a lab DHCP server. Do not attach intentionally vulnerable machines to a bridged campus/home network. NAT networking may provide Internet access, but keep vulnerable targets isolated from it.

## Option C: GNS3 / EVE-NG
Use these after understanding Packet Tracer basics. They can emulate or virtualize more realistic network topologies. Router/switch operating-system images may require a license; obtain images only from authorized sources.

## How to connect a basic lab
- Physical/virtual link: connect VM NICs to the same virtual switch/network.
- IP layer: assign addresses in the same subnet.
- Gateway: configure only when the host needs to reach another subnet.
- DNS: configure a resolver if name resolution is needed.
- Firewall: allow only the test traffic needed.
- Verification: check interface status, IP settings, ARP/neighbor table, ping, traceroute and packet capture.

## Troubleshooting checklist
1. Is the interface/link up?
2. Are both devices on the intended virtual/physical network?
3. Are IP addresses unique and in the correct subnet?
4. Is the subnet mask correct?
5. Is a gateway required and configured correctly?
6. Is a host firewall blocking the test?
7. Can you see ARP/neighbor discovery?
8. Does a packet capture show requests and replies?

## Lab notebook template
Copy this for every exercise:
- Date:
- Objective:
- Tool and version:
- Topology:
- IP addressing table:
- Configuration:
- Tests and expected results:
- Actual results:
- Screenshots (remove passwords, tokens and public IP details):
- Problem and fix:
- Security lesson:
- Next step:
