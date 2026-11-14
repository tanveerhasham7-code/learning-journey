# Windows domain security events


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
