# 10 — DHCP Traffic Analysis

## 1. DHCP purpose
DHCPv4 automatically provides network settings such as IP address, subnet mask, default gateway, DNS server and lease duration.

## 2. DORA sequence
1. Discover: client broadcasts to find a DHCP server.
2. Offer: server offers an address and options.
3. Request: client requests the offered configuration.
4. Acknowledge: server confirms the lease.

Some renewals and special cases use a shorter exchange.

## 3. What to inspect
In Wireshark filter `dhcp` (some versions/protocol decoders may also expose `bootp`). Inspect client MAC, transaction ID, offered/requested IP, server identifier, lease time, subnet mask, router and DNS options.

## 4. Why DHCP records matter to incident response
An IP address may be reassigned. DHCP lease records help map an address to a client identifier or MAC during a specific time interval. Combine with time synchronization, wireless association logs, switch port records and identity logs. A MAC address is not a permanent human identity.

## 5. Security risks
- Rogue DHCP server supplies malicious gateway or DNS settings.
- DHCP starvation attempts to exhaust available leases.
- Incorrect scope/options cause outages or traffic redirection.

Defenses include DHCP snooping, trusted server-facing switch ports, rate limits, monitoring and appropriate network access control.

## 6. Filters
```text
dhcp
bootp
dhcp.option.dhcp == 1
dhcp.option.dhcp == 2
dhcp.option.dhcp == 3
dhcp.option.dhcp == 5
```
Message-type field names can vary by Wireshark version; inspect the decoded packet tree if a filter does not work.

## Practical lab
In an isolated VM network, renew a test client's DHCP lease and capture the exchange. Identify DORA messages, transaction ID, server identifier, assigned address, gateway and DNS server. Use a lab DHCP server only.

## Analyst question
A firewall log shows an IP address at 10:05. What DHCP and clock information is needed to associate that IP with the correct device at that time?
