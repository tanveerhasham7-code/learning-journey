# 05 — Sysmon Event IDs and Telemetry

## 1. Understanding event IDs
Sysmon assigns IDs to activity categories. Verify current meanings and fields against Microsoft documentation and your Sysmon version. An event is evidence of recorded activity, not automatic proof of an attack.

## 2. Common IDs

| ID | Activity | SOC value |
|---|---|---|
| 1 | Process creation | Image, command line, parent, hashes |
| 2 | File creation time changed | Timestamp manipulation review |
| 3 | Network connection | Process-associated network activity; configurable |
| 5 | Process terminated | Process lifecycle |
| 6 | Driver loaded | Driver inventory |
| 7 | Image/DLL loaded | Module loading; potentially high volume |
| 8 | CreateRemoteThread | Cross-process thread creation |
| 10 | Process accessed | Process access relationships |
| 11 | File created | File drops and staging |
| 12–14 | Registry changes | Key/value modifications |
| 15 | File stream created | Alternate data stream visibility |
| 17–18 | Named pipe activity | Inter-process communication |
| 22 | DNS query | Process-associated DNS lookup |
| 23 / 26 | File deletion | File deletion visibility; configuration-dependent |

Some categories require explicit configuration and may generate substantial volume.

## 3. Event ID 1 — Process creation
Useful fields include ProcessGuid, ProcessId, Image, CommandLine, User, hashes, ParentImage and ParentCommandLine. ProcessGuid helps correlate a process across events more reliably than PID alone because PIDs can be reused.

Ask:
- Is the executable expected on this host?
- Is its path unusual?
- Does the parent process make sense?
- Does the command line match the user's role?
- Did it create files or connect to a network?

## 4. Event ID 3 — Network connection
When enabled, review source/destination addresses and ports, protocol, image and user. A connection is not inherently malicious; compare it with application purpose, destination context and related endpoint evidence.

## 5. Registry and file activity
Events 11–14 and related file events can help investigate autorun locations, service configuration, scripts and dropped files. Software installation and normal applications can also create many legitimate changes.

## 6. Correlation example
A hypothetical chain: Event 1 records an unexpected script host; Event 3 records a connection; Event 11 records file creation; Event 12–14 records a related registry change. This is a hypothesis to investigate. Validate timestamps, process identity and context.

## 7. Query example

~~~powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-Sysmon/Operational'
    Id = 1
    StartTime = (Get-Date).AddHours(-24)
} -ErrorAction SilentlyContinue |
Select-Object TimeCreated, Id, ProviderName, Message
~~~

For scalable analysis, parse event XML into named fields rather than relying only on message text.

## 8. Practical task
Choose one Sysmon event present in your lab. Document its ID, provider, fields, source, purpose and two benign explanations.

## 9. Knowledge check
1. Why is ProcessGuid useful?
2. What does Event 1 provide?
3. Why can Event 7 be high volume?
4. Why treat event sequences as hypotheses?