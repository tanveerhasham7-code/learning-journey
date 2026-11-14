# 06 — PowerShell Security Logging

## 1. Why monitor PowerShell?
PowerShell is a legitimate administration tool that can also be misused. Analysts review execution context rather than assuming every PowerShell command is malicious.

## 2. Main logging options
- **Module logging:** records pipeline execution details for configured modules.
- **Script Block Logging:** records processed script blocks; Event ID 4104 is commonly associated with it.
- **Transcription:** records input and output in transcript files when configured.
- **Process telemetry:** adds executable, parent process and command-line context.
- **PowerShell Operational channel:** contains PowerShell provider events.

Behavior differs by PowerShell version and host. Windows PowerShell 5.1 and PowerShell 7 may use different channels and configurations.

## 3. Enablement and privacy
In an authorized test environment, review Group Policy under Administrative Templates → Windows Components → Windows PowerShell. Configure only the logging needed for the exercise. Protect transcript destinations and define retention.

Script Block Logging and transcription can record sensitive commands, paths or secrets. Do not enable broad collection without privacy and operational review. Never put passwords or tokens in commands.

## 4. Common event examples
- 400/403: engine lifecycle information in applicable versions.
- 4103: module logging details when configured.
- 4104: script-block logging when configured.

Verify provider, channel and version on the actual endpoint.

## 5. Investigation context
Review user, host, parent process, command line, script-block records if available, timeline, related network connections and files, and whether the action matches an approved task.

Encoded or obfuscated text alone does not prove compromise. Analyze suspicious content only in a safe environment and according to policy.

## 6. Query example

~~~powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Microsoft-Windows-PowerShell/Operational'
    Id = 4104
    StartTime = (Get-Date).AddHours(-24)
} -ErrorAction SilentlyContinue |
Select-Object TimeCreated, Id, Message
~~~

## 7. Security controls
Restrict access to logs and transcripts, protect centralized storage, define retention, redact secrets from portfolio evidence and test event arrival.

## 8. Practical task
Identify PowerShell versions and available channels on a test VM. Review whether Script Block Logging is enabled. If authorized, enable it in the lab, run a harmless command and verify the event.

## 9. Knowledge check
1. Purpose of Script Block Logging?
2. How does transcription differ?
3. Why can logs contain sensitive information?
4. Why correlate PowerShell with process telemetry?