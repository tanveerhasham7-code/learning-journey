# 06 — Windows Networking for Security Analysts

## Core concepts
Windows networking uses adapters, TCP/IP, DNS, DHCP, routing and firewall rules. Understand IPv4 addresses, subnet masks, default gateways, DNS servers, TCP/UDP ports and connection states.

## Useful inspection commands
~~~powershell
ipconfig /all
Get-NetIPConfiguration
Get-NetIPAddress
Get-DnsClientServerAddress
Get-NetRoute
Get-NetTCPConnection
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
~~~

Use only domains and systems you are authorized to test.

## TCP and UDP
TCP is connection-oriented and provides sequencing and retransmission. UDP sends datagrams without TCP's connection and retransmission behavior. A listening port is not automatically vulnerable; identify the owning process and determine whether the service is expected.

## DNS and DHCP
DNS translates names to records such as IP addresses. DHCP provides configuration such as IP address, gateway and DNS server. Incorrect DNS can cause outages or direct users to malicious infrastructure.

## Network profiles
Windows commonly uses Domain, Private and Public profiles. Different firewall rules can apply to each profile. Public networks should normally have restrictive inbound access.

~~~powershell
Get-NetConnectionProfile
Get-NetAdapter
~~~

## Practical lab
Run ipconfig /all and Get-NetIPConfiguration. Identify the active adapter, address, gateway and DNS server. Resolve a known domain and test HTTPS connectivity with Test-NetConnection. Explain each result. Sanitize network identifiers before publishing.

## Check yourself
What does DNS do? What is the default gateway? Why should inbound access be restricted on a Public profile?
