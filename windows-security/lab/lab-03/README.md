# Lab 03 — User Account Control (UAC) and Windows Privilege Checks

## Lab overview

| Item | Details |
|---|---|
| Lab | 03 — User Account Control (UAC) and Windows Privilege Checks |
| Platform | Windows 11 Pro |
| OS version | 10.0.26300 |
| Build | 26300 |
| Tools | Windows UAC Settings, PowerShell, Windows Registry provider, CIM |
| Status | Completed |

## Objective

Review the Windows User Account Control (UAC) configuration, inspect local account group membership, and compare a command's behavior in elevated and non-elevated PowerShell sessions.

## Tasks performed

### 1. Reviewed the UAC slider

Opened **User Account Control Settings** and confirmed the selected option:

> Notify me only when apps try to make changes (Default)

This is the default UAC notification level. The setting was inspected and not changed.

### 2. Inspected UAC registry values

Ran the following command in PowerShell:

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" |
Select-Object EnableLUA, ConsentPromptBehaviorAdmin, PromptOnSecureDesktop
```

Observed output:

| Registry value | Result | Interpretation |
|---|---:|---|
| EnableLUA | 1 | UAC is enabled |
| ConsentPromptBehaviorAdmin | 5 | Default consent behavior for administrators |
| PromptOnSecureDesktop | 1 | UAC prompts use the secure desktop |

These values are consistent with the default UAC configuration observed in Settings.

### 3. Reviewed local security group membership

Used these commands to inspect the current account's security groups and local group membership:

```powershell
whoami /groups
Get-LocalGroupMember -Group "Administrators"
Get-LocalGroupMember -Group "Users"
```

The commands were executed as part of the account and privilege review. Exact member lists are not reproduced here because their complete output was not separately recorded in the lab notes.

### 4. Compared elevated and standard PowerShell behavior

Ran:

```powershell
net session
```

- In the elevated PowerShell session, the command returned: `There are no entries in the list.`
- In the standard, non-elevated PowerShell session, it returned:

```text
System error 5 has occurred.

Access is denied.
```

This demonstrated that the command requires administrative privileges in this environment. The difference is an expected access-control behavior, not evidence of a system fault.

### 5. Verified the operating system

Ran:

```powershell
Get-CimInstance -ClassName Win32_OperatingSystem |
Select-Object Caption, Version, BuildNumber
```

Observed output:

| Field | Result |
|---|---|
| Caption | Microsoft Windows 11 Pro |
| Version | 10.0.26300 |
| BuildNumber | 26300 |

## Security observations

- UAC is enabled (`EnableLUA = 1`).
- The administrator consent behavior is set to the default value observed in this lab.
- Secure Desktop prompting is enabled (`PromptOnSecureDesktop = 1`).
- The standard PowerShell session was denied access to the administrative `net session` operation, while the elevated session could run it.
- These checks demonstrate the importance of least privilege and elevation controls during Windows administration and SOC endpoint triage.

## Evidence

The following screenshots are stored in `lab/screenshort/lab-03/` and embedded below.

### Screenshot 1 — UAC settings
![Lab 03 screenshot 1 — UAC settings](../screenshort/lab-03/Screenshot%202026-11-25%20151812.png)

### Screenshot 2 — UAC registry configuration
![Lab 03 screenshot 2 — UAC registry values](../screenshort/lab-03/Screenshot%202026-11-25%20152002.png)

### Screenshot 3 — User and group privilege review
![Lab 03 screenshot 3 — User and group review](../screenshort/lab-03/Screenshot%202026-11-25%20152316.png)

### Screenshot 4 — Privilege behavior and system verification
![Lab 03 screenshot 4 — PowerShell privilege check and system verification](../screenshort/lab-03/Screenshot%202026-11-25%20152615.png)

## Result

Completed a practical review of UAC settings and registry configuration, inspected local security group membership, compared elevated and standard PowerShell access, and verified the Windows edition/build.

**Lab status: Completed.**

## Learning outcome

This lab reinforced how UAC and Windows group-based permissions help restrict administrative actions. For SOC work, understanding the difference between standard and elevated execution helps analysts interpret access-denied events and investigate privilege-related activity.

## Safety and privacy note

Before making evidence public, review screenshots for usernames, device identifiers, or other personal information and redact anything you do not want publicly visible.
