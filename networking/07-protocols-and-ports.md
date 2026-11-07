# 07 — Common Protocols and Ports

Ports identify transport-layer application endpoints. A port number alone does not prove which application is running; verify service behavior.

| Protocol/service | Common port | Transport | Purpose |
|---|---:|---|---|
| FTP control | 21 | TCP | Legacy file transfer; avoid clear-text use |
| SSH | 22 | TCP | Secure remote shell |
| Telnet | 23 | TCP | Unencrypted remote terminal; avoid |
| SMTP | 25 | TCP | Mail transfer |
| DNS | 53 | UDP/TCP | Name resolution |
| DHCP server/client | 67/68 | UDP | Dynamic host configuration |
| HTTP | 80 | TCP | Web traffic |
| POP3 | 110 | TCP | Mail retrieval |
| NTP | 123 | UDP | Time synchronization |
| IMAP | 143 | TCP | Mail access |
| SNMP | 161/162 | UDP | Monitoring/traps |
| LDAP | 389 | TCP/UDP | Directory access |
| HTTPS | 443 | TCP (commonly); QUIC uses UDP 443 | Secure web / HTTP over TLS or QUIC |
| SMB | 445 | TCP | Windows file sharing |
| SMTPS/submission | 465/587 | TCP | Secure mail submission |
| LDAPS | 636 | TCP | LDAP over TLS |
| RDP | 3389 | TCP/UDP | Remote Desktop |

## Cybersecurity relevance
- Exposed services increase attack surface.
- Disable unnecessary services.
- Restrict management ports to trusted admin networks.
- Prefer encrypted protocols.
- Monitor unexpected listening ports and outbound connections.
- Use firewall rules based on business need and least privilege.

## Lab
On your own Linux VM, run `ss -tulpen` to inspect listening sockets. Compare the results with the services you intentionally enabled. Do not expose services to the Internet just to practice.
