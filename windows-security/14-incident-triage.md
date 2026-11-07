# 14 — Windows Incident Triage

## Purpose
Triage is the first structured review of a possible security event. The goal is to understand what happened, preserve evidence and follow the organization's response process.

## Basic workflow
1. **Validate:** identify alert source, time, device, user and detection details.
2. **Scope:** determine whether other devices or accounts may be involved.
3. **Preserve:** follow policy for logs, timestamps and evidence handling.
4. **Assess:** consider data, availability, privilege and business impact.
5. **Contain:** authorized responders act according to the incident plan.
6. **Eradicate and recover:** remove the cause, patch or rebuild and restore trusted data.
7. **Learn:** document root cause, timeline, control gaps and preventive actions.

## Initial read-only collection examples
~~~powershell
Get-Date
hostname
whoami
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, Id, CPU
Get-NetTCPConnection -State Established
Get-Service | Where-Object Status -eq "Running"
Get-WinEvent -LogName System -MaxEvents 30 |
    Select-Object TimeCreated, Id, LevelDisplayName, ProviderName
~~~

These commands are starting points, not complete forensic collection. Follow approved procedures.

## Evidence handling
Record who collected evidence, when, from which system, which tool was used and where evidence is stored. Preserve originals and calculate hashes when required by process. Never upload sensitive production logs, memory images or personal data to a public repository.

## Example
A user reports repeated sign-in prompts. Record the time, inspect relevant sign-in events, confirm whether the account should be active, check related alerts and escalate if compromise is suspected. Repeated failures alone do not prove an attack.

## Check yourself
Why preserve evidence? Why must containment actions follow authorization and incident policy?
