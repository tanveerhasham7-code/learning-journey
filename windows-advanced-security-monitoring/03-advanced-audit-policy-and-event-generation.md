# 03 — Advanced Audit Policy and Event Generation

## 1. Auditing
Auditing controls which security-relevant actions Windows records. Audit settings determine whether events are generated; they do not automatically create SIEM alerts. Verify the event on the correct computer and channel.

## 2. Common audit subcategories
- Account Logon
- Logon/Logoff
- Account Management
- Detailed Tracking
- Policy Change
- Object Access
- Directory Service Access
- Privilege Use
- System

Useful settings depend on the machine role and the event you need. Domain controllers and workstations do not generate identical telemetry.

## 3. Policy configuration
In a controlled lab, review Local Security Policy or Group Policy under:

Computer Configuration → Policies → Windows Settings → Security Settings → Advanced Audit Policy Configuration → System Audit Policies.

Choose Success and Failure auditing deliberately. Excessive auditing can create high event volume. In domain environments, verify which GPO applies and how policy precedence affects the endpoint.

## 4. Review effective policy

~~~cmd
auditpol /get /category:*
~~~

This displays effective settings. It does not prove a particular event will be generated. Perform a controlled test.

## 5. Example event IDs

| Event ID | Meaning | Context |
|---|---|---|
| 4624 | Successful logon | Computer recording the logon |
| 4625 | Failed logon | Computer recording the attempt |
| 4634 | Logoff | Computer recording session end |
| 4648 | Explicit credentials used | Process/logon context |
| 4672 | Special privileges assigned | Privileged logon context |
| 4688 | Process created | Process creation auditing |
| 4720 | User account created | Account management |
| 4732 | Member added to local group | Group management |
| 1102 | Security audit log cleared | Affected host's Security log |

Event generation depends on Windows version, audit policy, action and source computer.

## 6. Validation workflow
1. Identify the action to test.
2. Identify the computer expected to record it.
3. Check required audit subcategory.
4. Perform a harmless controlled action with a test account.
5. Search the correct channel and time range.
6. Inspect fields and source computer.
7. Record whether the event appeared.
8. Troubleshoot policy, permissions, event location and test method if absent.

## 7. Common pitfalls
Confusing basic and advanced policy, configuring a GPO that does not apply, searching the wrong computer, assuming settings create events without activity, ignoring log volume and treating event presence as proof of malicious intent.

## 8. Practical task
Capture auditpol output on a test VM. Select one safe event, document its required policy, enable the setting, perform the action and record the observed result. Do not change production policy without authorization.

## 9. Knowledge check
1. Difference between enabling auditing and creating a detection?
2. Why may a DC record an event that a workstation does not?
3. How verify effective policy?
4. What evidence proves the test worked?