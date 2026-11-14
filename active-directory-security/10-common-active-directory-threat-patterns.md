# Common Active Directory threat patterns


This section describes defensive concepts and indicators. It is not an attack guide.

### 10.1 Password spraying

An actor tries a small number of common passwords against many accounts to avoid triggering account lockout thresholds.

Possible indicators:

- Many accounts failing authentication from one source.
- Similar failure patterns over a short period.
- Failures followed by success for one or more accounts.
- Attempts against accounts that do not normally authenticate from that source.

Differentiate spraying from a misconfigured application, stale saved credentials or a legitimate identity rollout.

### 10.2 Brute-force attempts

Repeated password guesses against one or more accounts may create clusters of failed logons. Investigate source, target, timing, logon type and whether any attempt succeeded.

### 10.3 Kerberoasting (defensive overview)

This attack pattern abuses the way service tickets are issued for accounts associated with service principal names. Offline password guessing may then be attempted against ticket material.

Defensive focus:

- Use long, unique, managed service-account passwords.
- Prefer Group Managed Service Accounts where appropriate.
- Inventory SPNs and remove stale or unnecessary ones.
- Avoid unnecessary privileged rights on service accounts.
- Monitor unusual service-ticket request patterns and correlate them with the requesting identity and host.

### 10.4 AS-REP roasting (defensive overview)

This pattern targets accounts configured without Kerberos pre-authentication. Review whether any such configuration is genuinely required, minimize exceptions and monitor unusual authentication activity involving affected accounts.

### 10.5 Pass-the-Hash and credential replay

Credential material may be abused to authenticate without knowing the original plaintext password. Reduce exposure by limiting privileged logons, protecting credential stores, using supported credential protections and monitoring unusual NTLM activity.

### 10.6 DCSync-style directory replication abuse

An identity with replication-related privileges may be able to request directory replication data. Review who has replication permissions and alert on unexpected use of directory replication rights. Investigations should include the actor, source host, target domain controller and relevant directory-service events/telemetry.

### 10.7 Golden Ticket and forged-ticket concepts

If an attacker obtains highly sensitive Kerberos key material, forged-ticket abuse may be possible. Protect domain controllers and directory database backups, minimize privileged access, monitor unusual Kerberos behavior and follow Microsoft's forest recovery guidance after a confirmed domain compromise.

### 10.8 Group Policy abuse

An unauthorized change to a GPO or its scripts can distribute insecure settings or execute code across many computers. Monitor policy modifications, SYSVOL changes, administrator identity and endpoint effects.

### 10.9 Lateral movement

An intruder may use one compromised host or account to access other systems. Look for unusual remote logons, administrative shares, service creation, remote management activity and a chain of logons across endpoints.

---
