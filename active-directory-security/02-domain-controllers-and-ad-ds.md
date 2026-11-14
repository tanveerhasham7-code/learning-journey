# Domain controllers and AD DS components


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
