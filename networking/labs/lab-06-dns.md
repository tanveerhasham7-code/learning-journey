# Lab 06 — DNS (Domain Name System)

**Status:** Completed — DNS A-record configured, hostname resolution verified with `nslookup`, hostname ping successful, and DNS events observed in Packet Tracer Simulation mode.  
**Date performed:** 16 November 2026  
**Tool:** Cisco Packet Tracer  
**Devices:** one PC-PT (displayed as PC2), one Cisco 2960-24TT switch (Switch1), and one Server-PT (Server1)

## 1. Objective

Configure a local DNS service in Packet Tracer, create an A record for a test hostname, and verify that a client can resolve the hostname to an IPv4 address. Observe DNS-related events in Simulation mode.

## 2. Topology

The lab uses a simple switched LAN:

- PC2 — client computer.
- Switch1 — Cisco 2960-24TT switch.
- Server1 — Server-PT providing DNS service.

PC2 and Server1 are connected to the switch using copper straight-through cables. The topology screenshot shows the links active.

![Lab 6 topology and PC IP configuration](screenshots/lab-06/Screenshot%202026-11-16%20105139.png)

## 3. IPv4 addressing

The lab network is `192.168.40.0/24`.

| Device | IPv4 address | Subnet mask | Default gateway | DNS server |
|---|---|---|---|---|
| PC2 | 192.168.40.10 | 255.255.255.0 | 192.168.40.1 | 192.168.40.2 |
| Server1 | 192.168.40.2 | 255.255.255.0 | 192.168.40.1 | 192.168.40.2 |

The gateway value was entered as part of the host configuration, but this topology has no router. Therefore, the gateway is not used for the local PC-to-server tests in this lab.

![Server1 static IPv4 configuration](screenshots/lab-06/Screenshot%202026-11-16%20105218.png)

## 4. DNS service configuration

On Server1, the DNS service was opened from **Services → DNS** and enabled.

The following DNS record was added:

| Field | Value |
|---|---|
| Record name | `www.lab.local` |
| Record type | A Record |
| IPv4 address | `192.168.40.2` |

An A record maps a hostname to an IPv4 address.

![Server1 DNS service with www.lab.local A record](screenshots/lab-06/Screenshot%202026-11-16%20105242.png)

## 5. DNS client verification

On PC2, Command Prompt was used to run:

```text
nslookup www.lab.local
```

Observed result:
- DNS server: `192.168.40.2`
- Resolved name: `www.lab.local`
- Resolved address: `192.168.40.2`

The following command was then run:

```text
ping www.lab.local
```

Observed result: four replies received, zero packet loss. This confirms that the hostname resolved to the server's IPv4 address and that the client could reach that address on the local LAN.

![Successful nslookup and ping of www.lab.local](screenshots/lab-06/Screenshot%202026-11-16%20105452.png)

## 6. DNS events in Simulation mode

Packet Tracer was switched to Simulation mode and the DNS event filter was selected. The event list shows DNS-related activity while the client ran the hostname lookup and ping tests.

![DNS filter and DNS-related Simulation event list](screenshots/lab-06/Screenshot%202026-11-16%20110155.png)

## 7. What this lab demonstrates

- DNS translates a hostname into an IP address.
- An A record maps a hostname to an IPv4 address.
- A client uses its configured DNS server to resolve a hostname.
- `nslookup` can be used to test DNS resolution.
- A hostname can be used with `ping` after it resolves successfully.
- Packet Tracer Simulation mode can display DNS-related network events.

## 8. Completion checklist

- [x] Add PC, switch, and Server-PT.
- [x] Connect the devices with copper straight-through cables.
- [x] Configure the PC and server IPv4 settings.
- [x] Enable DNS service on Server1.
- [x] Add the `www.lab.local` A record pointing to `192.168.40.2`.
- [x] Verify hostname resolution with `nslookup`.
- [x] Verify hostname reachability with `ping`.
- [x] Observe DNS-related events in Simulation mode.
- [x] Save and link screenshot evidence.

**Overall result:** Lab 6 DNS configuration and verification completed successfully.

## 9. Evidence screenshots

All five screenshots are stored in the [Lab 6 screenshots folder](screenshots/lab-06/):

1. [Screenshot 2026-11-16 105139.png](screenshots/lab-06/Screenshot%202026-11-16%20105139.png) — topology and PC2 IP configuration.
2. [Screenshot 2026-11-16 105218.png](screenshots/lab-06/Screenshot%202026-11-16%20105218.png) — Server1 static IP configuration.
3. [Screenshot 2026-11-16 105242.png](screenshots/lab-06/Screenshot%202026-11-16%20105242.png) — DNS service and `www.lab.local` A record.
4. [Screenshot 2026-11-16 105452.png](screenshots/lab-06/Screenshot%202026-11-16%20105452.png) — successful `nslookup` and hostname ping.
5. [Screenshot 2026-11-16 110155.png](screenshots/lab-06/Screenshot%202026-11-16%20110155.png) — DNS-filtered Simulation event list.
