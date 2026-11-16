# Lab 05 — DHCP (Dynamic Host Configuration Protocol)

**Status:** In progress — DHCP service and client address assignment were observed, but the clients received addresses from an unintended/default pool and their IPv4 default gateway remained 0.0.0.0. The configured LAN_POOL still needs to be verified and corrected.  
**Date performed:** 16 November 2026  
**Tool:** Cisco Packet Tracer  
**Devices:** Cisco 2911 router, Cisco Catalyst 2960 switch, one Server-PT, and two PCs

## 1. Objective

Build a small LAN with a router, switch, DHCP server, and two client PCs. Configure the router and server with static IPv4 addresses, create a DHCP pool, obtain addresses automatically on both PCs, test connectivity, and observe DHCP messages in Simulation mode.

The lab demonstrates the purpose of DHCP and the client/server exchange. The final configuration is **not yet fully correct**, because the observed client leases do not match the intended pool and the default gateway is missing.

## 2. Topology

The Packet Tracer topology contains:
- Router0 — Cisco 2911, connected to Switch0.
- Switch0 — Cisco 2960, connecting the router, server, PC0, and PC1.
- Server0 — Server-PT, intended to provide DHCP.
- PC0 and PC1 — DHCP clients.

The four links are shown connected in the topology screenshot. The router uses GigabitEthernet0/0 toward the switch. The server and PCs connect to separate switch access ports.

![Lab 5 topology and router GigabitEthernet0/0 configuration](screenshots/lab-05/Screenshot%202026-11-16%20085302.png)

## 3. IPv4 addressing plan

The intended network is 192.168.30.0/24.

| Device | Intended IPv4 address | Subnet mask | Default gateway |
|---|---|---|---|
| Router G0/0 | 192.168.30.1 | 255.255.255.0 | — |
| Server0 | 192.168.30.2 | 255.255.255.0 | 192.168.30.1 |
| PC0 | DHCP pool address | 255.255.255.0 | 192.168.30.1 |
| PC1 | DHCP pool address | 255.255.255.0 | 192.168.30.1 |

The intended DHCP pool was configured with:
- Pool name: LAN_POOL
- Default gateway: 192.168.30.1
- DNS server: 8.8.8.8
- Start address: 192.168.30.100
- Subnet mask: 255.255.255.0
- Maximum users: 101

The expected client range is 192.168.30.100 through 192.168.30.200.

## 4. Router configuration

The router's GigabitEthernet0/0 interface was assigned 192.168.30.1/24 and enabled.

    enable
    configure terminal
    interface gigabitEthernet 0/0
    ip address 192.168.30.1 255.255.255.0
    no shutdown
    exit
    end
    show ip interface brief

The screenshot shows the command accepted and the interface reported as up/up with address 192.168.30.1.

![Router G0/0 configured with 192.168.30.1 and verified up/up](screenshots/lab-05/Screenshot%202026-11-16%20085302.png)

## 5. Server static IP configuration

Server0 was configured manually from **Desktop → IP Configuration**:

| Setting | Configured value |
|---|---|
| IPv4 mode | Static |
| IP address | 192.168.30.2 |
| Subnet mask | 255.255.255.0 |
| Default gateway | 192.168.30.1 |
| DNS server | 8.8.8.8 |

![Server0 static IPv4 configuration](screenshots/lab-05/Screenshot%202026-11-16%20094657.png)

## 6. DHCP service and pool

The DHCP service was opened from **Server0 → Services → DHCP**. A pool named LAN_POOL was entered with the intended gateway, DNS server, starting IP address, subnet mask, and maximum-user count.

The saved DHCP screen also shows an additional default serverPool entry. This is important: the client lease screenshots later show that the clients did not receive the intended 192.168.30.100+ addresses. The extra pool and the active pool selection need to be checked before the lab can be marked complete.

![DHCP service showing LAN_POOL settings and an additional default serverPool entry](screenshots/lab-05/Screenshot%202026-11-16%20095219.png)

## 7. DHCP client configuration and observed leases

Both PCs were set to **Desktop → IP Configuration → DHCP**.

The screenshots show these actual IPv4 settings:

| Client | Observed IPv4 address | Subnet mask | Observed default gateway | DNS |
|---|---|---|---|---|
| PC0 | 192.168.30.3 | 255.255.255.0 | 0.0.0.0 | 8.8.8.8 |
| PC1 | 192.168.30.4 | 255.255.255.0 | 0.0.0.0 | 8.8.8.8 |

The PCs did receive IPv4 addresses automatically, but these addresses are outside the intended LAN_POOL range and the default gateway is not correct. This suggests that the default pool or another pool entry is being used instead of the intended configuration.

![PC0 receiving 192.168.30.3 through DHCP; default gateway shown as 0.0.0.0](screenshots/lab-05/Screenshot%202026-11-16%20100314.png)

![PC1 receiving 192.168.30.4 through DHCP; default gateway shown as 0.0.0.0](screenshots/lab-05/Screenshot%202026-11-16%20100338.png)

## 8. Connectivity tests

The following tests are visible in the PC0 Command Prompt screenshots.

### Test A — PC0 to router

Command:

    ping 192.168.30.1

Observed result: 4 replies received, 0% packet loss.

### Test B — PC0 to DHCP server

Command:

    ping 192.168.30.2

Observed result: 4 replies received, 0% packet loss.

### Test C — PC0 to the intended next pool address

Command:

    ping 192.168.30.101

Observed result: 4 requests timed out, 100% packet loss. This address was not assigned to PC1 in the captured configuration.

### Test D — PC0 to PC1's actual observed address

Command:

    ping 192.168.30.4

Observed result: 4 replies received, 0% packet loss.

![PC0 ipconfig and successful ping to the router](screenshots/lab-05/Screenshot%202026-11-16%20100550.png)

![PC0 ping results for the server, intended address 192.168.30.101, and PC1 actual address 192.168.30.4](screenshots/lab-05/Screenshot%202026-11-16%20100914.png)

**Connectivity result:** PC0 can reach the router, server, and PC1 at its actual observed address. However, the intended pool address test failed, and both clients show an incorrect default gateway. Therefore, basic local connectivity works, but the DHCP configuration needs correction.

## 9. DHCP Simulation observation

Packet Tracer was switched to **Simulation** mode and the DHCP event filter was enabled. The screenshot shows DHCP-related events moving through Server0, Switch0, and the client devices. This provides evidence of DHCP message exchange in the simulated network.

![DHCP-filtered Simulation mode showing DHCP events and client configuration](screenshots/lab-05/Screenshot%202026-11-16%20102954.png)

DHCP uses the DORA sequence:
1. **Discover** — client broadcasts to find a DHCP server.
2. **Offer** — server offers an available address and configuration.
3. **Request** — client requests the offered address.
4. **Acknowledge** — server confirms the lease.

## 10. What this lab demonstrates

- A router interface can act as the LAN's default gateway.
- A server can provide DHCP service to client devices.
- DHCP clients can obtain IPv4 addresses without manually entering them.
- Packet Tracer Simulation mode can be used to observe DHCP-related events.
- Successful IP assignment alone does not prove that every DHCP option is correct; the gateway, DNS, subnet mask, and address range must also be checked.

## 11. Pending correction

Before marking Lab 5 fully complete, correct and retest the DHCP pool:

- [x] Build the router-switch-server-two-PC topology.
- [x] Configure Router G0/0 as 192.168.30.1/24.
- [x] Configure Server0 as 192.168.30.2/24 with gateway 192.168.30.1.
- [x] Create the intended LAN_POOL with start IP 192.168.30.100, gateway 192.168.30.1, DNS 8.8.8.8, and maximum users 101.
- [x] Set PC0 and PC1 to DHCP and observe automatic address assignment.
- [x] Observe DHCP events in Simulation mode.
- [x] Verify PC0 can ping the router and server.
- [ ] Investigate the additional default serverPool entry and ensure clients use LAN_POOL.
- [ ] Renew both client leases and confirm addresses in the intended range.
- [ ] Confirm both clients receive default gateway 192.168.30.1.
- [ ] Retest PC0-to-PC1 connectivity using the actual new DHCP lease.
- [ ] Capture final screenshots showing corrected client leases and successful tests.

**Overall status:** DHCP service and message exchange were observed, and basic LAN pings succeeded. The intended DHCP pool and default-gateway options are not yet verified on the clients, so Lab 5 remains **in progress**.

## 12. Evidence screenshots

All eight screenshots are stored in the [Lab 5 screenshots folder](screenshots/lab-05/):

1. Screenshot 2026-11-16 085302.png — topology, router G0/0 configuration, and interface status.
2. Screenshot 2026-11-16 094657.png — Server0 static IP configuration.
3. Screenshot 2026-11-16 095219.png — DHCP LAN_POOL settings and the additional default serverPool entry.
4. Screenshot 2026-11-16 100314.png — PC0 DHCP lease and current IPv4 configuration.
5. Screenshot 2026-11-16 100338.png — PC1 DHCP lease and current IPv4 configuration.
6. Screenshot 2026-11-16 100550.png — PC0 ipconfig and successful router ping.
7. Screenshot 2026-11-16 100914.png — server ping success, failed ping to 192.168.30.101, and successful ping to PC1 at 192.168.30.4.
8. Screenshot 2026-11-16 102954.png — DHCP-filtered Simulation mode event list.

*This report records the actual configuration and results visible in the uploaded screenshots. The remaining DHCP corrections are deliberately listed as pending rather than reporting the lab as fully complete.*
