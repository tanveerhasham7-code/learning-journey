# Active Directory Security for SOC Analysts

**Level:** Beginner to Intermediate  
**Track:** SOC Analyst / Blue Team  
**Purpose:** Understand how Windows domain identity works, what telemetry it produces, and how a SOC analyst detects and investigates suspicious activity.

> **Study rule:** This repository separates theory from practical evidence. Read and understand the material first. Perform labs only in an isolated domain that you own or are explicitly authorized to administer. Mark a lab complete only after you have performed it and saved sanitized evidence.

## Learning outcomes

After studying this module, you should be able to:

- Explain the purpose and main components of Active Directory Domain Services (AD DS).
- Describe domains, forests, trees, domain controllers, sites, OUs, users, groups and Group Policy.
- Explain the high-level purpose of LDAP, Kerberos and NTLM.
- Recognize important Windows security events related to logons, accounts, groups and Kerberos.
- Identify why privileged identities need stronger monitoring.
- Build a basic investigation timeline from domain authentication and directory-change events.
- Explain common identity attack patterns without performing attacks against real systems.
- Write a detection hypothesis and recommend proportionate defensive actions.

## Course map

1. [Active Directory fundamentals and architecture](#1-active-directory-fundamentals-and-architecture)
2. [Domain controllers and AD DS components](#2-domain-controllers-and-ad-ds-components)
3. [Users, groups, computers and organizational units](#3-users-groups-computers-and-organizational-units)
4. [Group Policy](#4-group-policy)
5. [LDAP and directory queries](#5-ldap-and-directory-queries)
6. [Kerberos authentication](#6-kerberos-authentication)
7. [NTLM authentication](#7-ntlm-authentication)
8. [Windows domain security events](#8-windows-domain-security-events)
9. [Privileged identities and access monitoring](#9-privileged-identities-and-access-monitoring)
10. [Common Active Directory threat patterns](#10-common-active-directory-threat-patterns)
11. [Detection engineering for Active Directory](#11-detection-engineering-for-active-directory)
12. [SOC investigation workflow and response](#12-soc-investigation-workflow-and-response)
13. [Practical lab plan](#13-practical-lab-plan)
14. [Knowledge check](#14-knowledge-check)
15. [Glossary and learning references](#15-glossary-and-learning-references)

---

## 1. Active Directory fundamentals and architecture

### 1.1 What is Active Directory?

Active Directory (AD) is Microsoft's directory service used by many organizations to centrally manage identities and resources in a Windows environment. It stores information about objects such as users, computers, groups and services. It also supports authentication and access-control decisions.

Imagine a university with hundreds of students, teachers, computers and shared folders. Without centralized identity management, each computer might need separate local accounts. Managing access and disabling a former employee's access would become difficult. A domain directory gives administrators a central place to manage identities and many security settings.

**Important distinction:** Active Directory is not the same thing as Microsoft Entra ID (formerly Azure Active Directory). Traditional AD DS is commonly deployed on Windows Server and uses domain controllers. Microsoft Entra ID is Microsoft's cloud identity service. Hybrid organizations may use both.

### 1.2 Why SOC analysts need to understand AD

A compromised identity can be used to access email, file shares, servers, business applications and administrative tools. Many serious incidents involve misuse of legitimate accounts rather than an obvious malware alert.

A SOC analyst therefore asks:

- Which identity authenticated?
- From which device and source address?
- At what time?
- Was the logon successful or unsuccessful?
- Which service or resource was accessed?
- Was the account privileged?
- Did the account's permissions or group memberships change?
- Does the activity match the user's normal role and behavior?

### 1.3 Logical structure

- **Object:** A directory entry, such as a user, computer, group or printer.
- **Domain:** An administrative and replication boundary containing directory objects.
- **Tree:** One or more domains in a contiguous DNS namespace.
- **Forest:** The top-level AD logical structure. A forest can contain one or more domain trees and shares a schema, configuration and global catalog.
- **Schema:** Defines the types of objects and attributes that can exist in the directory.
- **Global Catalog (GC):** Helps users and applications search for directory information across a forest. It holds a partial, searchable replica of objects from the forest.
- **Site:** Represents the physical network structure used to optimize replication and client access.

A small organization may use one domain in one forest. A large organization may use multiple domains and sites. More domains do not automatically mean better security; design should follow operational and security requirements.

### 1.4 Naming examples

A domain might be named `corp.example.test`. A user could have a User Principal Name (UPN) such as `alex@corp.example.test` and a distinguished name (DN) such as:

`CN=Alex Khan,OU=Finance,DC=corp,DC=example,DC=test`

The DN describes the object's path in the directory. The UPN is a logon-style name that resembles an email address, but it is not necessarily a working email address.

---

## 2. Domain controllers and AD DS components

### 2.1 Domain Controller (DC)

A Domain Controller is a Windows Server running AD DS. It stores a replica of the directory for its domain and performs important identity functions, including authentication and directory lookups.

A domain may have multiple domain controllers for availability, capacity and geographic reasons. Changes are generally replicated between writable domain controllers. Replication health matters: a delay or failure can cause inconsistent views of directory changes.

### 2.2 Important components

- **NTDS.dit:** The main AD database file on a domain controller. It contains directory data and must be protected as highly sensitive.
- **SYSVOL:** A shared folder replicated among domain controllers in a domain. It stores items such as Group Policy files and scripts.
- **DNS:** Domain clients rely heavily on DNS records to locate domain services and domain controllers.
- **AD replication:** Keeps directory changes synchronized between domain controllers.
- **FSMO roles:** Five specialized operations-master roles help coordinate particular forest-wide or domain-wide tasks. They are not five separate servers by definition; roles can be held by different DCs or concentrated on one DC in a small environment.

### 2.3 FSMO roles

Forest-wide roles:

1. **Schema Master:** Coordinates schema changes.
2. **Domain Naming Master:** Coordinates adding or removing domains in a forest.

Domain-wide roles:

3. **RID Master:** Allocates pools of Relative Identifiers used when creating security principals.
4. **PDC Emulator:** Handles several important compatibility and time-related functions, and is significant for password-change processing and account lockout behavior.
5. **Infrastructure Master:** Maintains certain cross-domain reference updates.

A SOC analyst should know that changes to directory infrastructure, replication behavior or privileged DC administration can have broad impact.

### 2.4 Defensive monitoring priorities

Monitor domain controllers closely because they are high-value identity infrastructure:

- Unexpected interactive or remote logons.
- New services, scheduled tasks or software installations.
- Changes to privileged groups and domain policies.
- Unusual PowerShell or administrative tool activity.
- Security log clearing or audit-policy changes.
- Replication or DNS anomalies.
- Unexpected changes to scripts or policies in SYSVOL.

---

## 3. Users, groups, computers and organizational units

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

## 4. Group Policy

### 4.1 What is Group Policy?

Group Policy is a Windows feature used to centrally configure user and computer settings in an AD domain. A Group Policy Object (GPO) contains policy settings and can be linked to a site, domain or OU.

Examples of security settings managed through policy:

- Password and account-lockout policy.
- Windows Defender Firewall configuration.
- Audit policy.
- Windows security options.
- Script and software deployment settings.
- Restrictions on removable storage or other device behavior.

### 4.2 Policy processing

A simplified processing order is commonly described as **Local, Site, Domain, OU** (LSDOU). Policies can be affected by inheritance, enforcement, filtering and other configuration. The effective policy should be checked on the endpoint rather than assumed from a GPO's name.

### 4.3 SOC monitoring

A suspicious policy change can weaken security across many machines. Monitor for:

- Changes to GPOs or their links.
- Unexpected modifications to scripts stored in SYSVOL.
- Changes to audit, firewall or Defender settings.
- New startup or logon scripts.
- Changes performed by an account that does not normally administer policy.

Correlate the directory-change event with the administrator's logon, endpoint activity, change ticket and the actual policy version.

---

## 5. LDAP and directory queries

### 5.1 What is LDAP?

Lightweight Directory Access Protocol (LDAP) is a protocol used by clients and applications to read and, when authorized, modify directory information.

LDAP helps applications search for users, groups, computers and other directory objects. It is not itself the same as an authentication protocol, although directory operations may be part of an authentication workflow.

Common ports:

- TCP/UDP 389: LDAP (UDP is used for limited functions; most directory queries use TCP).
- TCP 636: LDAP over TLS, commonly called LDAPS.
- Global Catalog: TCP 3268; secure Global Catalog: TCP 3269.

Port use depends on configuration and the application. Do not infer that traffic is safe merely because it uses a standard port.

### 5.2 Distinguished names and search filters

An LDAP distinguished name identifies an object's location in the directory. LDAP filters select objects based on attributes.

Conceptual example:

`(&(objectCategory=person)(objectClass=user)(sAMAccountName=alex))`

This example asks for user objects whose account name is alex. It is a directory search filter, not a password or an exploit.

### 5.3 Security considerations

- Prefer encrypted directory communication where supported.
- Restrict who can read sensitive attributes and who can modify objects.
- Monitor unusual query volume or access patterns where telemetry is available.
- Investigate anonymous or unauthenticated directory access if it is not expected.
- Avoid exposing directory services directly to untrusted networks.

---

## 6. Kerberos authentication

### 6.1 What is Kerberos?

Kerberos is a network authentication protocol commonly used by AD domains. It uses tickets and a trusted Key Distribution Center (KDC), usually hosted by a domain controller, so users can authenticate to services without sending their password to every service.

### 6.2 Simplified flow

1. A user signs in and requests authentication from the KDC.
2. The Authentication Service (AS) issues a Ticket-Granting Ticket (TGT) after successful authentication.
3. The client presents the TGT to request a service ticket from the Ticket-Granting Service (TGS).
4. The client presents the service ticket to the target service.
5. The service validates the ticket and grants access according to its own authorization rules.

A ticket proves an authentication step; it does not automatically grant permission to every resource.

### 6.3 Important terms

- **KDC:** Key Distribution Center.
- **TGT:** Ticket-Granting Ticket.
- **TGS:** Ticket-Granting Service.
- **SPN:** Service Principal Name, which identifies a service instance for Kerberos.
- **Clock synchronization:** Kerberos is sensitive to time differences. Domain time configuration is therefore important.

### 6.4 SOC-relevant patterns

- Unusual volume of service-ticket requests.
- Service tickets requested for unexpected accounts or services.
- Kerberos pre-authentication failures.
- Unusual encryption-type usage compared with the organization's baseline.
- Authentication activity from unexpected hosts or at unusual times.

These patterns are investigation leads, not proof of compromise. Service accounts, legacy systems and legitimate administrative tools can produce unusual-looking activity.

---

## 7. NTLM authentication

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

## 8. Windows domain security events

Windows Security logs provide important evidence for identity investigations. Event IDs are useful identifiers, but their availability and meaning depend on audit policy, Windows version, event source and configuration.

### 8.1 High-value event IDs

| Event ID | Meaning | SOC investigation value |
|---|---|---|
| 4624 | Successful logon | Identify account, logon type, source and target host |
| 4625 | Failed logon | Investigate repeated failures, source and target |
| 4634 | Logoff | Help establish session end |
| 4648 | Logon using explicit credentials | Identify use of supplied credentials |
| 4672 | Special privileges assigned to new logon | Review privileged logon context |
| 4688 | Process creation | Investigate process execution when auditing is enabled |
| 4720 | User account created | Validate provisioning and creator |
| 4722 | User account enabled | Check whether enablement was approved |
| 4723 | Attempt to change an account password | Correlate with user activity |
| 4724 | Attempt to reset an account password | Review administrator or reset workflow |
| 4725 | User account disabled | Confirm expected offboarding or containment |
| 4726 | User account deleted | Check authorization and change record |
| 4728 | Member added to a security-enabled global group | Investigate group privilege changes |
| 4729 | Member removed from a security-enabled global group | Validate access change |
| 4732 | Member added to a security-enabled local group | Investigate local group membership |
| 4733 | Member removed from a security-enabled local group | Validate removal |
| 4740 | User account locked out | Identify source and repeated failures |
| 4768 | Kerberos TGT requested | Review domain authentication |
| 4769 | Kerberos service ticket requested | Review service access patterns |
| 4771 | Kerberos pre-authentication failed | Investigate authentication failures |
| 4776 | NTLM credentials validated | Identify NTLM authentication activity |
| 1102 | Security audit log cleared | High-priority investigation clue |

**Important:** Some events are generated on domain controllers, some on member servers or workstations, and some may be present in multiple places depending on the action. For example, 4768 and 4769 are generally DC-side Kerberos events. Event 4624 is generated on the computer where the logon session is created. Confirm the event's source computer before interpreting it.

### 8.2 Logon types for Event 4624

Common logon types include:

- **2 — Interactive:** A local interactive sign-in, such as at a keyboard.
- **3 — Network:** Access to a computer or resource over the network.
- **4 — Batch:** A batch job.
- **5 — Service:** A service started under an account.
- **7 — Unlock:** A workstation was unlocked.
- **10 — RemoteInteractive:** Commonly a Remote Desktop logon.
- **11 — CachedInteractive:** A sign-in using cached domain credentials.

Logon type must be interpreted with the target system, account, authentication package and surrounding events.

### 8.3 Useful event fields

When available, preserve and compare:

- TimeCreated / timestamp (including timezone).
- Computer / event source.
- TargetUserName and TargetDomainName.
- SubjectUserName and SubjectDomainName (the actor performing an action).
- SubjectLogonId and TargetLogonId.
- IpAddress and WorkstationName.
- LogonType.
- Status and SubStatus for failures.
- ProcessName and AuthenticationPackageName.

Do not confuse the **Subject** (often the actor) with the **Target** (the account or object affected).

### 8.4 Logging prerequisites

Events are useful only if the right audit policies are enabled, logs are retained, clocks are synchronized and collection is working. Use Group Policy or an approved endpoint-management method to configure advanced audit policy. Forward logs to a protected central platform and alert on collection gaps.

---

## 9. Privileged identities and access monitoring

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

## 10. Common Active Directory threat patterns

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

## 11. Detection engineering for Active Directory

A useful detection is more than an event ID. It has a clear hypothesis, data requirements, logic, exclusions, severity, triage steps and a test plan.

### 11.1 Detection lifecycle

1. Define the threat behavior and business risk.
2. Identify the telemetry needed.
3. Confirm that logging is enabled and fields are populated.
4. Write a detection hypothesis.
5. Implement a query or correlation rule in the chosen SIEM.
6. Test with safe, authorized simulation or synthetic events.
7. Review false positives and tune thresholds.
8. Document investigation steps and response guidance.
9. Version-control the rule and review it periodically.

### 11.2 Example detection hypothesis: privileged group membership change

**Hypothesis:** A user is added to a highly privileged group outside an approved administrative change.

**Telemetry:** Windows Security events for group membership changes, especially 4728, 4732 and related events appropriate to the group type; include the actor, member, group, domain controller and timestamp.

**Logic outline:**

- Identify membership-addition events for a maintained list of sensitive groups.
- Enrich the actor and member with account and asset context.
- Check approved change windows or tickets.
- Raise severity when the actor is unexpected, the member is a normal user, or the event occurs outside approved activity.

**Triage questions:**

- Which account made the change?
- Which account was added?
- Which group was modified?
- Was the change approved?
- Did the actor recently authenticate from an unusual device?
- What did the new member do after the change?

### 11.3 Example detection hypothesis: repeated failures followed by success

**Hypothesis:** A sequence of failures followed by a successful authentication may indicate password guessing or a user entering an incorrect password and then succeeding.

**Telemetry:** 4625 and 4624, plus source address, target account, target host, logon type and timestamps.

**Logic outline:**

- Group failures by account and source over a defined time window.
- Identify a subsequent success for the same account or relevant source.
- Suppress known noisy systems only when there is a documented reason.
- Increase priority if the account is privileged or the source is unusual.

**Caution:** A fixed threshold should be based on local baseline and business context. A single universal threshold is rarely suitable for every organization.

### 11.4 Example detection hypothesis: suspicious account creation

**Hypothesis:** A new user account is created by an unexpected actor or outside the normal provisioning workflow.

**Telemetry:** Event 4720 and nearby events such as account enablement, password reset, group membership changes and first logon.

**Triage:** Identify creator, new account, timestamp, domain controller, initial group memberships, approval record and first authentication activity.

### 11.5 Detection quality checklist

- Does the rule detect a meaningful behavior rather than a noisy single event?
- Are the required audit policies enabled?
- Are event fields normalized consistently?
- Is there a clear severity rationale?
- Are legitimate admin workflows documented?
- Can the analyst explain why an alert fired?
- Does the runbook say what evidence to collect?
- Has the rule been tested with benign and suspicious examples?
- Is the detection version-controlled?

---

## 12. SOC investigation workflow and response

Use a repeatable workflow. Do not jump from one event to a conclusion.

### 12.1 Alert triage

1. **Validate the alert:** Check event source, timestamp, fields and collection health.
2. **Identify the identity:** Determine whether the account is a user, service, computer or administrator account.
3. **Identify the asset:** Establish the source and destination systems and their business importance.
4. **Build a timeline:** Correlate logons, failures, account changes, group changes and process activity.
5. **Compare with baseline:** Is the behavior normal for this identity, device and role?
6. **Check authorization:** Look for an approved change, maintenance window or support ticket.
7. **Assess scope:** Search for related accounts, hosts and similar events.
8. **Determine impact:** Establish what access may have been gained or what data/systems may be affected.
9. **Escalate or close:** Record evidence and rationale.

### 12.2 Evidence handling

Record:

- Case ID and analyst.
- Alert ID and detection name.
- Event IDs and original event records.
- UTC timestamp and original timezone.
- Account identifiers and relevant group memberships.
- Hostnames and source addresses.
- Relevant SIEM queries and time ranges.
- Hashes of exported evidence where appropriate.
- Actions taken, approvals and communications.

Keep original evidence unchanged. Work from copies, restrict access and follow the organization's retention and privacy policies. Sanitize usernames, domains, IPs and hostnames before publishing portfolio examples.

### 12.3 Response options

Depending on evidence, authority and incident policy, responders may:

- Disable or temporarily restrict a compromised account.
- Revoke sessions or reset credentials using the approved identity process.
- Remove unauthorized group membership.
- Isolate an affected endpoint through approved EDR procedures.
- Block a malicious source when justified.
- Preserve relevant logs and forensic evidence.
- Review other identities and systems for related activity.
- Restore policy or configuration from a known-good state.

Do not perform containment actions on production systems without the required authorization. A SOC analyst should follow escalation and approval procedures.

### 12.4 Case closure

A good closure note states:

- What happened.
- Which identities and assets were involved.
- What evidence supports the conclusion.
- Whether activity was authorized, suspicious or confirmed malicious.
- What containment or remediation occurred.
- What remains uncertain.
- What detection or control improvement is recommended.

---

## 13. Practical lab plan

The practical project will be built separately in the Projects repository as **Active Directory SOC Monitoring Lab**. This learning module does not claim that any lab has already been deployed.

Suggested isolated lab components:

- One Windows Server virtual machine configured as a domain controller.
- One Windows client joined to the test domain.
- A separate analyst workstation or the host machine for reviewing exported logs.
- Windows Security auditing configured for the required event categories.
- Optional Sysmon for endpoint process telemetry.
- A SIEM/log collector such as Wazuh, if the available hardware and configuration support it.

Use a private virtual network. Use test identities and synthetic business data. Never expose a lab domain controller directly to the public internet.

### Planned exercises

| Lab | Objective | Evidence to save |
|---|---|---|
| 1. Domain discovery | Identify domain, DC and client configuration | Sanitized command output and topology |
| 2. User lifecycle | Create, disable and enable a test user | Relevant event records and explanation |
| 3. Group membership | Add/remove a test user from a test group | Event record and before/after membership |
| 4. Failed logons | Generate a small number of controlled failures | 4625 event and field analysis |
| 5. Successful logon | Sign in with a test identity | 4624 event and logon-type explanation |
| 6. Account lockout | Demonstrate a configured test lockout safely | 4740 event and source analysis |
| 7. Password reset | Reset a test account password | Relevant event and authorized actor |
| 8. GPO review | Inspect an approved test policy change | GPO settings and change evidence |
| 9. Privileged group audit | Review membership of a test privileged group | Membership report; do not add unnecessary real privileges |
| 10. SIEM investigation | Search and correlate selected events | Query, alert, timeline and case note |

### Evidence standard

For every exercise, save:

1. Objective and environment.
2. Exact steps you performed.
3. Sanitized screenshot or exported event.
4. What you observed.
5. What the observation means to a SOC analyst.
6. Any error or limitation.
7. Completion status: Planned, In Progress or Verified.

Do not mark exercises Verified until you have personally performed them and checked the evidence.

---

## 14. Knowledge check

Try to answer these in your own words before checking external notes.

1. What problem does Active Directory solve in an organization?
2. What is the difference between a domain, a forest and an OU?
3. What is the role of a domain controller?
4. How is a security group different from an OU?
5. What is the purpose of Group Policy?
6. What is the high-level difference between LDAP and Kerberos?
7. What are a TGT and a service ticket?
8. Why might an organization still have NTLM traffic?
9. Which event IDs can help investigate a successful logon and a failed logon?
10. What does Event ID 4720 indicate?
11. Why should privileged group membership changes be monitored?
12. Why is a single failed logon not enough to prove an attack?
13. What evidence would you collect after an unexpected privileged-group addition?
14. What is the difference between an alert and a confirmed incident?
15. Why should an analyst document timezone and source computer?

### Short scenario

At 02:15, a domain controller records a user being added to a sensitive administrative group. The actor is a standard account. Shortly afterward, the new member account authenticates to a server it has never used before.

Write an investigation plan:

- Identify the group-change event and its actor/member fields.
- Confirm the domain controller and timestamp.
- Check whether the change was approved.
- Review the actor's recent logons and endpoint activity.
- Review the new member's authentication and subsequent access.
- Identify affected systems and preserve evidence.
- Escalate according to the incident-response policy.

Do not assume compromise until the evidence and authorization checks support that conclusion.

---

## 15. Glossary and learning references

### Essential glossary

- **AD DS:** Active Directory Domain Services.
- **DC:** Domain Controller.
- **OU:** Organizational Unit.
- **GPO:** Group Policy Object.
- **LDAP:** Lightweight Directory Access Protocol.
- **LDAPS:** LDAP protected with TLS.
- **KDC:** Key Distribution Center.
- **TGT:** Ticket-Granting Ticket.
- **TGS:** Ticket-Granting Service.
- **SPN:** Service Principal Name.
- **UPN:** User Principal Name.
- **DN:** Distinguished Name.
- **SID:** Security Identifier.
- **SYSVOL:** Domain share used for policy and script distribution.
- **FSMO:** Flexible Single Master Operations.
- **SIEM:** Security Information and Event Management.
- **EDR:** Endpoint Detection and Response.
- **Baseline:** A documented picture of normal activity used for comparison.
- **False positive:** An alert that fires on activity that is not actually malicious.

### Authoritative learning references

Use current vendor documentation because product behavior and security recommendations can change.

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Active Directory documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [Microsoft Learn — Windows security auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-policy-recommendations)
- [Microsoft Learn — Advanced security audit policy settings](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [Microsoft Learn — Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [Microsoft Learn — LDAP signing](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
- [Microsoft Learn — Group Policy overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
- [MITRE ATT&CK — Enterprise techniques](https://attack.mitre.org/)

---

## Completion checklist

- [ ] I can explain AD DS architecture without reading the notes.
- [ ] I can distinguish a domain, forest, OU and security group.
- [ ] I can explain the basic Kerberos ticket flow.
- [ ] I understand where LDAP and NTLM fit.
- [ ] I can identify the purpose of the key Windows event IDs in this module.
- [ ] I can investigate a privileged group change using actor, target and host context.
- [ ] I can describe at least three AD threat patterns and their defensive indicators.
- [ ] I have completed practical exercises and uploaded sanitized evidence to the companion project.
- [ ] I can explain one detection rule, its logic, limitations and triage steps.

**Portfolio status:** Theory module published. Practical completion remains dependent on your own lab work and evidence.
