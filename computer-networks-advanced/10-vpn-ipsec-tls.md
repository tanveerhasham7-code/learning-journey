# 10 — VPN, IPsec and TLS

## 1. Why encryption in transit?
Networks may pass through shared or untrusted infrastructure. Encryption in transit protects data from passive observation and helps detect modification. It does not protect a compromised endpoint or make an unsafe application secure.

## 2. VPN concepts
A Virtual Private Network creates a protected logical connection across another network. Common uses include remote-access VPNs for individual users and site-to-site VPNs connecting offices.

Evaluate:
- Identity and MFA
- Device posture and patch state
- Tunnel encryption and key exchange
- Allowed routes and split-tunnel policy
- DNS behavior while connected
- Logging, revocation and key rotation

## 3. IPsec overview
IPsec is a suite for protecting IP traffic. Important concepts:
- **AH:** integrity/authentication without confidentiality; uncommon in many modern deployments.
- **ESP:** can provide confidentiality, integrity and authentication.
- **Transport mode:** protects the IP payload between hosts.
- **Tunnel mode:** encapsulates and protects an entire original IP packet, common for site-to-site VPNs.
- **IKE/IKEv2:** negotiates security associations and keys.

Use modern, vendor-supported cryptographic suites and strong authentication. Avoid obsolete algorithms and pre-shared secrets reused across many users or sites.

## 4. TLS overview
TLS protects application connections such as HTTPS. A handshake negotiates protocol parameters, authenticates the server with a certificate, and establishes session keys. Certificate validation matters: users and applications should verify hostname, trust chain, validity and revocation policy as applicable.

## 5. VPN is not a security boundary by itself
A VPN user may still be compromised. Apply least privilege after connection, segment remote users, require MFA, monitor unusual access and revoke lost devices promptly.

## Practical lab
Use a simulator or a private lab VPN product between two VMs you control. Document tunnel endpoints, routes, authentication method and allowed subnets. Verify that only intended networks are reachable. Separately inspect a normal HTTPS TLS handshake in Wireshark and identify certificate/handshake metadata.

## Incident clues
Unexpected VPN logins, impossible travel, repeated authentication failures, new source devices, unusual data transfer and access outside a user's role deserve investigation. Correlate identity, endpoint and network telemetry before concluding compromise.
