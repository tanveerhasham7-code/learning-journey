# 10 — Windows Persistence Indicators

## 1. Meaning
Persistence is a method that allows software or an intruder to maintain execution or access after restart, logoff or another interruption. Analysts look for unauthorized changes to automatic execution locations.

## 2. Common areas
- Windows services and service configuration.
- Scheduled tasks.
- Run and RunOnce registry keys.
- Startup folders.
- WMI event subscriptions.
- Local accounts and group membership.
- Logon scripts and Group Policy.
- Security tooling or audit settings.

A change is not automatically malicious.

## 3. Useful telemetry
Security account/process events, System service events, Task Scheduler Operational events, Sysmon process/registry/file events, PowerShell logs and Defender/EDR alerts.

Availability depends on policy, Windows version and collection setup.

## 4. Safe read-only inventory

~~~powershell
# List scheduled tasks
Get-ScheduledTask | Select-Object TaskName, TaskPath, State

# List services
Get-CimInstance Win32_Service |
Select-Object Name, State, StartMode, StartName, PathName

# Review common Run keys
Get-ItemProperty 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Run' -ErrorAction SilentlyContinue
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -ErrorAction SilentlyContinue
~~~

Review output carefully; paths and arguments may be sensitive. Do not delete or modify entries on production systems as an experiment.

## 5. Investigation questions
Who changed the item? When? Is the binary expected and signed? Does the path and account make sense? Is there an approved change? Did it execute? Are there related logons, process events or network connections?

## 6. Practical task
Inventory scheduled tasks and services on a lab VM. Select one legitimate item and explain purpose, execution identity and startup behavior. Do not create persistence for this exercise.

## 7. Knowledge check
1. What is persistence?
2. Name four Windows persistence areas.
3. Why inspect execution identity?
4. What makes a change suspicious?