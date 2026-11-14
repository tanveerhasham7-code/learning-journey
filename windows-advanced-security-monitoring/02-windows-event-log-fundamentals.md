# 02 — Windows Event Log Fundamentals

## 1. Event Log service
Windows Event Log is an operating-system logging framework. Windows components and applications publish structured records that analysts can inspect using Event Viewer or PowerShell.

## 2. Common channels
- **Application:** application events.
- **System:** operating-system, service and driver events.
- **Security:** audited security activity; access is restricted.
- **Setup:** setup and servicing events.
- **Forwarded Events:** records received through Windows Event Forwarding.
- **Operational channels:** component-specific logs such as PowerShell and Sysmon.

A provider can publish to one or more channels. Always identify both provider and channel.

## 3. Important event fields

| Field | Meaning |
|---|---|
| Provider / Source | Component that generated the event |
| Event ID | Event type identifier for that provider |
| Level | Critical, Error, Warning, Information or Verbose |
| TimeCreated | Recorded timestamp |
| Computer | Computer that recorded the event |
| User / Security ID | Security context, when supplied |
| EventData | Event-specific fields |
| Record ID | Record sequence within the log |

The computer that records an event may differ from a remote system mentioned in its event data.

## 4. Event Viewer workflow
1. Open Event Viewer and expand Windows Logs.
2. Select Security, System or Application.
3. Filter by event ID, level and time.
4. Open the event and inspect General and Details.
5. Record provider, computer, timestamp and relevant fields.
6. Export only necessary records and sanitize before sharing.

## 5. PowerShell examples

~~~powershell
# List available event logs
Get-WinEvent -ListLog *

# Read recent System events
Get-WinEvent -LogName System -MaxEvents 20

# Read recent Security events (permissions required)
Get-WinEvent -LogName Security -MaxEvents 20

# Filter failed logons in the last day
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4625
    StartTime = (Get-Date).AddHours(-24)
} -ErrorAction SilentlyContinue

# Inspect structured XML for one event
$event = Get-WinEvent -LogName System -MaxEvents 1
$event.ToXml()
~~~

Prefer time and ID filters rather than loading an entire busy log.

## 6. EVTX files
EVTX is the Windows event-log file format. Exports may contain usernames, hostnames, IP addresses, paths and organizational details. Treat them as sensitive.

## 7. Common mistakes
- Searching by ID without checking provider.
- Assuming every endpoint records every event.
- Ignoring timezone and clock drift.
- Treating missing events as proof an action did not happen.
- Sharing raw logs without sanitizing.
- Forgetting permissions may restrict Security log access.

## 8. Practical task
Choose a non-sensitive System event. Record provider, ID, level, computer, timestamp and message. Retrieve it with Get-WinEvent and compare the details.

## 9. Knowledge check
1. What is an event channel?
2. Why inspect the provider?
3. What does EVTX contain?
4. Why use a time filter?