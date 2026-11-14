# Practical lab plan


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
