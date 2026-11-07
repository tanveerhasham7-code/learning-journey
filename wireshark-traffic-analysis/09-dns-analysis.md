# 09 — DNS Traffic Analysis

## 1. DNS purpose
DNS translates names into records. A client may ask a recursive resolver, which may use cached data or query authoritative infrastructure. A capture can show queries, answers, record types, response codes and timing.

## 2. Common record types
- A: IPv4 address
- AAAA: IPv6 address
- CNAME: canonical name alias
- MX: mail exchanger
- NS: authoritative name server
- TXT: text data, used by many legitimate services
- PTR: reverse lookup
- SOA: zone authority information

## 3. Query/response fields
In Wireshark expand Domain Name System. Inspect transaction ID, query name, query type, flags, response code, answer count, TTL and returned records. Match the response to the request using transaction ID and endpoints, while considering retries and transport behavior.

## 4. Response codes
- NOERROR: query completed without DNS error; answer may still be empty.
- NXDOMAIN: requested name does not exist according to the responding server.
- SERVFAIL: server could not complete the query.
- REFUSED: server refused the query.

A high NXDOMAIN rate may be caused by typos, broken applications, misconfiguration or suspicious algorithmic queries. Investigate context.

## 5. Useful filters
```text
dns
dns.flags.response == 0
dns.flags.response == 1
dns.qry.name
dns.qry.type == 1
dns.qry.type == 28
dns.flags.rcode != 0
udp.port == 53 || tcp.port == 53
```

## 6. DNS security signals
Investigate:
- Workstations using unexpected external resolvers
- Sudden query-volume increases
- Repeated random-looking subdomains
- Unusual TXT or other record patterns
- Many failed lookups
- Domains newly observed for a host
- DNS activity outside normal business patterns

DNS tunneling may encode data in query names or records, but long/random names alone are not enough to prove tunneling. Consider query length, entropy, volume, response patterns, process attribution and endpoint context.

## 7. Encrypted DNS
DoH and DoT protect the client-to-resolver channel. A packet capture may show encrypted sessions rather than readable query names. Use approved resolver logs, endpoint telemetry and network policy to retain visibility without bypassing user privacy.

## Practical lab
Use dig or nslookup to query a harmless test domain for A, AAAA and MX records. Capture the exchange, identify query and response, note TTL and response code. Generate a deliberately invalid test name and compare the response.

## SOC exercise
Given synthetic DNS events, identify one unusual pattern and write alternative benign explanations plus the additional evidence needed.
