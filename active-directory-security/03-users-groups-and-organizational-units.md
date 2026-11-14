# Users, groups, computers and organizational units


### 3.1 User accounts

A user object represents an identity. Common attributes include display name, UPN, account status, department, manager and group memberships.

Security-relevant account states include:

- Enabled or disabled.
- Locked or unlocked.
- Password expired or password change required.
- Password never expires (often a risk if used without a strong documented reason).
- Account expiration date.
- Whether the account is marked as sensitive or delegated in particular ways.

Do not assume that a familiar display name proves who used an account. Correlate the account identifier, logon session, endpoint, source address and surrounding events.

### 3.2 Computer accounts

Domain-joined computers have their own directory identities. They authenticate to the domain and have passwords that are normally rotated automatically by Windows.

Unexpected computer-account creation, unusual changes, or authentication from an unexpected system can be useful investigation clues.

### 3.3 Security groups

Groups simplify permission management. Instead of granting access separately to many users, administrators can assign permissions to a group and manage its membership.

- **Security group:** Can be used to assign permissions.
- **Distribution group:** Primarily used for email distribution and is not used to assign Windows access permissions.
- **Global, Domain Local and Universal:** Group scopes that determine where membership and permissions can be used. Understand the organization's group design before recommending a change.

Examples of sensitive built-in groups include Domain Admins, Enterprise Admins, Administrators and Backup Operators. The exact risk depends on the group's permissions and the environment.

### 3.4 Organizational Units (OUs)

An OU is a container used to organize directory objects and delegate administration. Group Policy can be linked to OUs.

Example:

```text
corp.example.test
├── OU=Workstations
│   ├── PC-FIN-01
│   └── PC-HR-01
├── OU=Servers
│   └── FILE-SRV-01
└── OU=Users
    ├── OU=Finance
    └── OU=Human-Resources
```

An OU is not the same as a security group. OUs organize objects and help apply policy or delegate administration; groups are commonly used to grant access.

### 3.5 SOC use cases

Investigate:

- A user added to a privileged group.
- A disabled account becoming enabled unexpectedly.
- A new account created outside the normal provisioning process.
- A service account used for interactive logon.
- A computer account created or modified by an unexpected actor.
- A user added to a group that grants access to sensitive data.

Always confirm the business reason and approved change record before treating an administrative change as malicious.

---
