# Lab 07 — Static Routing Between Two LANs

**Date performed:** 16 November 2026  
**Tool:** Cisco Packet Tracer  
**Status:** Completed — static routes installed and cross-LAN connectivity demonstrated.

## Objective

Connect two separate LANs using two Cisco routers, configure reciprocal static routes, inspect routing tables, and trace the path between end devices.

## Topology

PC0 — Switch0 — Router1 — Router0 — Switch1 — PC1

- Router1 connects LAN A to the inter-router network.
- Router0 connects LAN B to the inter-router network.
- Both router-to-router and LAN links are shown active in the final topology screenshots.

## IP addressing plan

| Device | Interface | IP address | Subnet mask | Default gateway |
|---|---|---:|---:|---:|
| PC0 | FastEthernet0 | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| Router1 | G0/0 (LAN A) | 192.168.10.1 | 255.255.255.0 | — |
| Router1 | G0/1 (WAN link) | 10.0.0.1 | 255.255.255.252 | — |
| Router0 | G0/1 (WAN link) | 10.0.0.2 | 255.255.255.252 | — |
| Router0 | G0/0 (LAN B) | 192.168.20.1 | 255.255.255.0 | — |
| PC1 | FastEthernet0 | 192.168.20.10 | 255.255.255.0 | 192.168.20.1 |

**Inter-router network:** 10.0.0.0/30  
**LAN A:** 192.168.10.0/24  
**LAN B:** 192.168.20.0/24

## Static route configuration

On Router1, a route was added for LAN B through Router0:

```text
enable
configure terminal
ip route 192.168.20.0 255.255.255.0 10.0.0.2
end
```

On Router0, a route was added for LAN A through Router1:

```text
enable
configure terminal
ip route 192.168.10.0 255.255.255.0 10.0.0.1
end
```

## Verification and results

- Router interface status was checked; the screenshots show the configured GigabitEthernet interfaces up/up.
- The routing tables show the expected static route entries:
  - Router1: `S 192.168.20.0/24 via 10.0.0.2`
  - Router0: `S 192.168.10.0/24 via 10.0.0.1`
- PC0 pinged PC1 at 192.168.20.10. The captured first test shows two initial timeouts followed by two successful replies (2 received, 2 lost).
- PC1 pinged PC0 at 192.168.10.10. The captured test shows four successful replies (0% loss).
- PC0 traceroute to 192.168.20.10 completed and displayed the path through router hops before reaching the destination.

The first ping's initial timeouts can occur while devices are resolving Layer 2 addresses (ARP). The evidence confirms successful replies and a completed trace, but the first captured PC0 ping is not a zero-loss test.

## Screenshots

All evidence is stored in [the Lab 7 screenshots folder](screenshots/lab-07/).

1. [Router1 LAN and WAN interface configuration](screenshots/lab-07/Screenshot%202026-11-16%20192432.png)
2. [PC0 IPv4 configuration](screenshots/lab-07/Screenshot%202026-11-16%20192527.png)
3. [PC1 IPv4 configuration](screenshots/lab-07/Screenshot%202026-11-16%20192552.png)
4. [Router0 LAN and WAN interface configuration](screenshots/lab-07/Screenshot%202026-11-16%20192901.png)
5. [Router1 initial CLI/startup screen](screenshots/lab-07/Screenshot%202026-11-16%20193048.png)
6. [Router0 interface status — up/up](screenshots/lab-07/Screenshot%202026-11-16%20193109.png)
7. [Router1 static route configuration](screenshots/lab-07/Screenshot%202026-11-16%20193445.png)
8. [Router0 static route configuration](screenshots/lab-07/Screenshot%202026-11-16%20193636.png)
9. [Router1 routing table with static route](screenshots/lab-07/Screenshot%202026-11-16%20193653.png)
10. [Router0 routing table with static route](screenshots/lab-07/Screenshot%202026-11-16%20193724.png)
11. [PC0 to PC1 ping test — initial timeouts then replies](screenshots/lab-07/Screenshot%202026-11-16%20193849.png)
12. [PC1 to PC0 ping test — 4/4 replies](screenshots/lab-07/Screenshot%202026-11-16%20194001.png)
13. [PC0 traceroute to PC1 — trace complete](screenshots/lab-07/Screenshot%202026-11-16%20194146.png)

## What I learned

- How routers connect separate IP networks.
- How to configure a /30 point-to-point network between routers.
- How to add reciprocal static routes using `ip route`.
- How to read connected (`C`) and static (`S`) entries in `show ip route`.
- How ping and traceroute help verify end-to-end connectivity and the forwarding path.

## Conclusion

The two LANs were connected through Router1 and Router0. Reciprocal static routes appeared in the routing tables, PC-to-PC communication produced successful replies in both directions, and traceroute completed to the remote PC. Lab 7 is documented as completed based on the captured evidence.
