# 14 — Practical Lab Roadmap

## 1. Objective
Build a safe Windows endpoint monitoring environment demonstrating event generation, collection, search, detection design and investigation. Start with one Windows test VM. Add a second endpoint or SIEM after the basics are understood.

## 2. Suggested components

| Component | Purpose |
|---|---|
| Windows 10/11 test VM | Endpoint telemetry |
| Windows Server VM (optional) | Central policy or collection |
| Sysmon (optional) | Detailed endpoint telemetry |
| PowerShell | Event review and automation |
| Wazuh or another SIEM (optional) | Central collection and detection |
| Analyst notes folder | Sanitized evidence and reports |

Use authorized systems, isolate test VMs appropriately and take snapshots before configuration changes.

## 3. Exercise backlog

| ID | Exercise | Expected evidence | Status |
|---|---|---|---|
| WIN-LAB-01 | Record OS version, hostname and topology | Sanitized inventory | Planned |
| WIN-LAB-02 | Explore Event Viewer channels | Channel/provider notes | Planned |
| WIN-LAB-03 | Query System and Security logs | Commands and output | Planned |
| WIN-LAB-04 | Review effective audit policy | auditpol output | Planned |
| WIN-LAB-05 | Inspect benign process event | 4688 or equivalent | Planned |
| WIN-LAB-06 | Review Sysmon official configuration | Configuration notes | Planned |
| WIN-LAB-07 | Install and validate Sysmon | Version, service and channel | Planned |
| WIN-LAB-08 | Analyze Sysmon process event | Event 1 fields | Planned |
| WIN-LAB-09 | Review network or DNS telemetry | Event 3/22 if configured | Planned |
| WIN-LAB-10 | Review PowerShell logging | Channel and event evidence | Planned |
| WIN-LAB-11 | Inspect Defender and Firewall | Sanitized status output | Planned |
| WIN-LAB-12 | Inventory services and tasks | Read-only inventory | Planned |
| WIN-LAB-13 | Draft and test detection hypotheses | Logic, results and tuning | Planned |
| WIN-LAB-14 | Investigate synthetic endpoint scenario | Timeline and report | Planned |

## 4. Evidence template

~~~markdown
# WIN-LAB-XX — Exercise name
Date/time and timezone:
Windows edition/version:
VM or host role:
Objective:
Authorization/scope: Own test environment
Commands/settings:
Expected result:
Actual result:
Evidence files:
Relevant event IDs/providers:
Interpretation:
False positives or limitations:
Problems and troubleshooting:
Status: Planned / In Progress / Verified
~~~

## 5. Completion criteria
- Environment and scope documented.
- Relevant channels and audit settings reviewed.
- At least one native event generated and explained.
- Sysmon installed and validated if included.
- PowerShell logging reviewed and tested if included.
- At least two detection hypotheses tested.
- One investigation timeline and case report completed.
- Evidence sanitized and reproducible.

## 6. Troubleshooting
If an event is missing, verify action occurred, correct host and channel, audit policy or Sysmon filter, permissions, retention and collector health.

Every exercise starts as Planned. Mark Verified only after reviewing actual evidence.