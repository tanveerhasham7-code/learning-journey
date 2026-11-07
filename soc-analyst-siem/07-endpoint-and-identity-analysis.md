# 07 — Windows, Linux, Identity, and Endpoint Analysis

## Endpoint investigation mindset
Endpoint investigations answer: who was logged in, what ran, how it started, what changed, what it contacted, and whether the behavior is expected. Correlate endpoint telemetry with identity, network, email, and change-management records.

## Windows investigation areas
- Logon and logoff activity, including interactive, network, remote, and service logons.
- Process creation, parent-child relationships, command lines, hashes, signatures, and execution paths.
- Services, scheduled tasks, startup locations, and other persistence locations.
- PowerShell and script activity when logging is enabled.
- Local users, groups, privileges, and security policy changes.
- Defender/EDR alerts, quarantine, device isolation, and process trees.
- Removable media, file changes, and unusual archive activity.

Important: Windows event IDs depend on audit policy and product configuration. Consult official event documentation and validate your lab configuration rather than relying on memorized IDs alone.

## Process tree analysis
A process tree shows parent and child processes. Ask:
- Is the parent process expected for this user and host?
- Does the command line match the application purpose?
- Is the binary signed and located in a normal path?
- Was it downloaded, extracted, or launched from a temporary directory?
- Did it create files, change persistence, or open network connections?
- Do endpoint, identity, and network records support the same timeline?

A suspicious-looking command can be legitimate administration. Context is essential.

## Linux investigation areas
Review SSH authentication, sudo usage, user/group changes, process and service activity, cron/systemd persistence, package changes, kernel/audit events, web server logs, and unusual outbound connections. Commands and log paths vary by distribution. Preserve evidence before making changes where an incident process requires it.

## Identity investigation
Investigate unusual sign-in location/device, impossible-travel indicators, repeated MFA prompts, MFA method registration, password reset, risky OAuth consent, new service principals, privilege/group changes, token/session anomalies, and suspicious mailbox rules.

Questions:
- Is the account human, service, shared, or privileged?
- Is the device managed and compliant?
- Was MFA satisfied, bypassed, denied, or not required?
- Was access conditional on risk, location, or device state?
- What resources were accessed after authentication?
- Are there other affected accounts or sessions?

## EDR and XDR
Endpoint Detection and Response tools collect endpoint activity and support investigation and response actions. Extended Detection and Response combines telemetry across endpoint, identity, email, cloud, and network sources. Understand the difference between a vendor alert, raw telemetry, analyst conclusion, and response action.

## Practical exercise
Use synthetic process and authentication records. Build a timeline for a fictional workstation where a user opens an attachment, a script interpreter starts, a child process runs, and an outbound connection occurs. Identify facts, hypotheses, missing evidence, and safe next steps.

## Knowledge check
1. Why is parent-child process context valuable?
2. What evidence helps distinguish admin automation from abuse?
3. List identity events to check after suspicious MFA activity.
4. Why should an analyst preserve evidence before containment when possible?
5. What is the difference between EDR and XDR?
