# 04 — Sysmon Architecture and Installation

## 1. What is Sysmon?
System Monitor (Sysmon), part of Microsoft Sysinternals, is a Windows service and driver that records detailed activity in Microsoft-Windows-Sysmon/Operational. It supplements native Windows logs; it does not replace them or determine whether activity is malicious.

## 2. SOC value
Sysmon can provide visibility into process creation, network connections, file creation, registry changes, DNS queries and other activity. This helps reconstruct behavior that default logs may not fully describe.

## 3. Components
- **Service:** manages event collection.
- **Driver:** supports monitoring.
- **Configuration:** controls included and excluded event types.
- **Operational channel:** stores Sysmon records.
- **Collector:** forwards selected records to centralized monitoring.

A broad configuration can create noise; an overly restrictive one can create blind spots.

## 4. Safe installation outline
1. Download only from Microsoft's official Sysinternals site.
2. Verify source and review documentation.
3. Use a disposable or snapshot-backed test VM.
4. Read command help and configuration documentation.
5. Review a configuration before applying it.
6. Install with administrator approval.
7. Confirm service and Operational channel.
8. Generate harmless activity and inspect the record.
9. Document version, configuration source and result.

~~~powershell
# Review help first
.\Sysmon64.exe -?

# Install with a reviewed local configuration
.\Sysmon64.exe -accepteula -i .\sysmon-lab-config.xml

# Check service
Get-Service Sysmon*

# Read recent records
Get-WinEvent -LogName 'Microsoft-Windows-Sysmon/Operational' -MaxEvents 20
~~~

Do not run unknown binaries or configurations.

## 5. Configuration lifecycle
Keep configuration under version control, record its source and version, test changes on a lab endpoint, review event volume and exclusions, and revalidate collection after upgrades.

## 6. Troubleshooting
If no events appear, check installation and service state, channel availability, configuration filters, whether the test generated the activity and whether the user can read the log.

## 7. Practical task
Review official Sysmon documentation and configuration. If you install it, record version, service state, channel availability and one harmless event. Otherwise mark installation pending.

## 8. Knowledge check
1. Does Sysmon replace Security logs?
2. What does its configuration control?
3. Why test before deployment?
4. Where are Sysmon events recorded?