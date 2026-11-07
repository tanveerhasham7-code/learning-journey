# 08 — Network Security Fundamentals

## Security goals
- Confidentiality: only authorized parties can read information.
- Integrity: information is not changed without authorization.
- Availability: systems and services remain accessible when needed.

## Network security controls
- Firewall: filters traffic based on policy.
- IDS: detects suspicious activity and raises alerts.
- IPS: can block detected malicious traffic inline.
- VPN: creates a protected tunnel across an untrusted network.
- NAC: controls which devices may join a network.
- Segmentation: limits unnecessary communication between zones.
- Proxy/Secure Web Gateway: mediates web access.
- WAF: protects web applications from certain application-layer attacks.

## Common threats
- Phishing and credential theft
- Malware and command-and-control traffic
- DoS/DDoS
- Man-in-the-middle attacks
- ARP spoofing
- DNS abuse
- Rogue access points and weak Wi-Fi security
- Misconfigured firewall rules and exposed services
- Lateral movement after an initial compromise

## Defensive design principles
1. Least privilege: permit only required access.
2. Defense in depth: use multiple complementary controls.
3. Network segmentation: separate users, servers, guests and management.
4. Secure administration: SSH/HTTPS, MFA, restricted admin sources.
5. Patch and configuration management.
6. Centralized logging and accurate time synchronization.
7. Backups and tested recovery plans.
8. Continuous monitoring and incident response.

## Firewall policy example (conceptual)
- Allow approved users to reach the organization's HTTPS service.
- Allow administrators to manage servers only from a dedicated admin subnet.
- Deny unsolicited inbound traffic by default.
- Log important denied or unusual traffic.
Actual rules depend on the platform and business requirements.

## Wireless security
Use WPA2-AES or WPA3 where supported, strong unique passphrases, updated firmware, guest isolation and disable obsolete WEP/WPA/TKIP. Use enterprise authentication for managed environments where appropriate.

## SOC analyst perspective
When investigating an alert, record source/destination IP, source/destination port, protocol, timestamp/time zone, hostname, user, process (if available), action, asset criticality and related logs. An IP address alone rarely proves malicious activity.
