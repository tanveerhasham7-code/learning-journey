# 07 — Event Viewer and Windows Logging

## Why logs matter
Logs help build a timeline of system and application activity. Analysts use them to investigate sign-ins, account changes, service failures, software installation and alerts. One event rarely tells the whole story.

## Main logs
- **Application:** application-generated events.
- **System:** Windows components, drivers and services.
- **Security:** audited security activity, depending on audit policy.
- **Setup:** installation and servicing.
- **Forwarded Events:** events received from other computers when configured.

Open Event Viewer using eventvwr.msc.

## Event fields
Review Event ID, level, provider/source, time, computer, user and event details/XML. Interpret an ID with its provider, operating-system version and context. Do not rely on memorized IDs alone.

## PowerShell log review
~~~powershell
Get-WinEvent -ListLog * | Select-Object -First 20 LogName, RecordCount, IsEnabled
Get-WinEvent -LogName System -MaxEvents 20 |
    Select-Object TimeCreated, Id, LevelDisplayName, ProviderName, Message
~~~

Security log access may require elevation. Filter by time and event properties rather than exporting huge logs.

## Sign-in investigation
Establish which account was involved, whether the attempt succeeded, when it happened, which host was involved and whether related alerts exist. Commonly discussed Security event IDs include 4624 (successful logon), 4625 (failed logon), 4634 (logoff), 4720 (user created) and 4728/4732 (group membership changes). Availability depends on audit configuration; inspect event details.

## Safe lab
Review recent System and Application events, sign out and back into your lab VM, then inspect relevant Security events if auditing is enabled. Record time, provider, ID and your interpretation. Do not upload raw logs containing personal information.

## Log protection
Restrict access, configure suitable retention and time synchronization, forward important events to protected central storage where possible and monitor unexpected gaps.

## Check yourself
Why is an event ID alone insufficient? What details help build a timeline?
