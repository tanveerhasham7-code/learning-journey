# NTLM authentication


### 7.1 What is NTLM?

NT LAN Manager (NTLM) is an older Microsoft authentication protocol that may still appear in environments for compatibility. It uses a challenge-response process.

A simplified description:

1. A client requests authentication.
2. The server sends a challenge.
3. The client computes a response using secret-derived material.
4. The server or a domain controller validates the response.

The user's plaintext password is not normally sent as part of this challenge-response exchange.

### 7.2 Why NTLM matters

NTLM has known security limitations compared with modern Kerberos-based domain authentication. Depending on configuration and protocol use, it can be exposed to relay and credential-related attack patterns.

Defensive recommendations:

- Inventory where NTLM is still required.
- Prefer Kerberos where compatible.
- Apply Microsoft's guidance for restricting NTLM in stages.
- Use SMB signing and other protocol protections where appropriate.
- Monitor NTLM use, especially from systems or accounts where it is unexpected.
- Test compatibility before disabling legacy authentication.

A SOC analyst should not recommend abruptly disabling NTLM without understanding business dependencies.

---
