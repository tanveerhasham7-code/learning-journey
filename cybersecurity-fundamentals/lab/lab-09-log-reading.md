# Practical 09 — Log Reading

**Status:** Assistant-prepared reference exercise; learner inspection of local logs is pending  
**Date prepared:** 2026-11-17  
**Suggested environment:** Windows 11 Pro, Version 26H2 (user-reported)

## Objective

Understand how to read a Windows Security event by identifying its timestamp, log, source, event ID, and message, then explain what the record does and does not prove.

## Important evidence note

The records below are **fictional training examples**. They were created for this report and were not collected from the learner's computer. No claim is made that these events occurred on the user's device.

## Example event records

| Field | Example A — Successful logon | Example B — Failed logon |
|---|---|---|
| Example timestamp | 2026-11-17 09:15:00 | 2026-11-17 09:18:42 |
| Log | Windows Logs → Security | Windows Logs → Security |
| Source | Microsoft-Windows-Security-Auditing | Microsoft-Windows-Security-Auditing |
| Event ID | 4624 | 4625 |
| Meaning | An account successfully logged on | A logon attempt failed |
| Training interpretation | A successful authentication was recorded | Credentials or another logon condition were not accepted |

These timestamps and event details are illustrative, not observed system evidence.

## How to inspect a real event safely

1. On your own Windows computer, open Start and search for **Event Viewer**.
2. Open **Windows Logs → Security**.
3. Review available events without changing or clearing any logs.
4. Select one ordinary event and note its **Date and Time**, **Source**, **Event ID**, and **General** message.
5. Avoid copying account names, email addresses, public IP addresses, device identifiers, or other personal information into a public repository. Replace them with labels such as `[REDACTED]`.
6. If Security log access is denied, do not change permissions just for this exercise. You can use a harmless System or Application event instead.

## Understanding the two example IDs

### Event ID 4624 — Successful logon

Windows records this event when an account successfully logs on. The event can include a logon type and other context. A successful logon is not automatically suspicious; users sign in during normal work. Review context such as time, logon type, and whether the activity is expected.

### Event ID 4625 — Failed logon

Windows records this event when a logon attempt fails. A single failure may result from a typing mistake, an expired password, a background service, or an unauthorized attempt. Repeated failures can justify further investigation, but the event alone does not prove an attack.

## Analyst questions and model answers

1. **What happened?** The example 4625 record indicates that a logon attempt failed.
2. **When did it happen?** Use the timestamp shown in the event record; the example time above is fictional.
3. **Where should it be checked?** Windows Logs → Security in Event Viewer.
4. **Does one failed logon prove brute force?** No. Look for a pattern, frequency, account context, and source context before drawing a conclusion.
5. **What should an analyst do?** Preserve relevant event details, correlate nearby events, check whether the activity is expected, and follow the organization's incident process if suspicious patterns appear.

## Result and limitations

This report demonstrates how to interpret common Windows log fields and two well-known Security event IDs. It does not establish that either event exists on the learner's device, and it does not constitute a live investigation.

**Practical 09 remains reference-prepared, not learner-completed.** To complete the hands-on portion, inspect one real, non-sensitive event on the learner's own computer and add sanitized details (or a redacted screenshot) to this report.

## Safety

Never clear logs, alter audit settings, attempt unauthorized access, or publish sensitive event data. Logs can contain personal and security-sensitive information.
