# Privileged identities and access monitoring


### 9.1 What is a privileged account?

A privileged account has more access than a normal user account. It may administer servers, manage users, change security policy, access sensitive data or control identity infrastructure.

Examples include domain administrators, enterprise administrators, server administrators, backup operators and delegated service accounts.

### 9.2 Why privileged accounts are high risk

If an attacker gains control of a highly privileged identity, the attacker may be able to change permissions, create accounts, access sensitive systems or weaken security controls. The impact can extend across an organization.

### 9.3 Defensive controls

- Apply least privilege: give each identity only the access needed for its role.
- Use separate standard and administrative accounts.
- Require strong multifactor authentication where supported by the access path.
- Restrict where privileged accounts can sign in.
- Avoid routine email/web browsing from privileged sessions.
- Use dedicated, hardened administrative workstations where feasible.
- Review privileged group membership regularly.
- Prefer managed service accounts for supported services.
- Disable stale accounts and investigate unused privileged identities.
- Use time-limited or just-in-time privilege where the environment supports it.

### 9.4 Monitoring checklist

Alert or investigate when:

- A member is added to or removed from a sensitive group.
- A privileged account signs in from an unusual endpoint.
- A privileged account performs interactive logon where only service use is expected.
- A new service account receives powerful permissions.
- A privileged identity authenticates outside its normal schedule or location.
- Multiple failures are followed by a successful privileged logon.
- Security policy or audit configuration is weakened.

---
