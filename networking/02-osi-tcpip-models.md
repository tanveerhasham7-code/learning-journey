# 02 — OSI and TCP/IP Models

## OSI model
The OSI model divides network communication into seven conceptual layers.

| Layer | Name | Main role | Examples |
|---|---|---|---|
| 7 | Application | Network services used by applications | HTTP, DNS, SMTP |
| 6 | Presentation | Data format, encoding, encryption | TLS-related presentation concepts, JPEG |
| 5 | Session | Starts, manages and ends sessions | Session control |
| 4 | Transport | End-to-end delivery, ports, reliability | TCP, UDP |
| 3 | Network | Logical addressing and routing | IPv4, IPv6, ICMP |
| 2 | Data Link | Local delivery, frames, MAC addresses | Ethernet, Wi-Fi MAC, VLAN |
| 1 | Physical | Signals and transmission media | Copper, fiber, radio |

Mnemonic from Layer 7 to 1: **All People Seem To Need Data Processing**.

## TCP/IP model
A common four-layer view:
1. Application — HTTP/S, DNS, SSH, SMTP
2. Transport — TCP, UDP
3. Internet — IP, ICMP
4. Network Access/Link — Ethernet, Wi-Fi

Some courses use a five-layer model by separating physical and data-link functions.

## Addressing at different layers
- Layer 2: MAC address, used for local-link delivery.
- Layer 3: IP address, used for communication between networks.
- Layer 4: TCP/UDP port, identifies an application endpoint on a host.

## Example: opening a secure website
1. The browser uses DNS to find the server's IP address.
2. The host determines whether the destination is local or remote.
3. If remote, it sends the frame to the default gateway's MAC address.
4. IP routes the packet toward the destination.
5. TCP establishes a connection when TCP is used.
6. TLS protects the application session; HTTP carries the web request.

## Troubleshooting by layer
- Layer 1: cable, link light, Wi-Fi signal, interface state.
- Layer 2: VLAN mismatch, MAC learning, switching loop.
- Layer 3: IP/mask/gateway, routing, duplicate IP.
- Layer 4: blocked port, service not listening, TCP reset.
- Layers 5–7: authentication, TLS certificate, DNS/application configuration.

## Lab
Capture a ping in Wireshark. Identify ICMP Echo Request and Echo Reply. Then capture a DNS lookup and identify the DNS query and response. Note the source/destination IPs and protocol.
