# 10 — Registry, UAC and Security Controls

## Windows Registry
The Registry is a hierarchical configuration database for Windows, hardware, users and applications. Common root keys include HKEY_LOCAL_MACHINE, HKEY_CURRENT_USER, HKEY_USERS and HKEY_CLASSES_ROOT. Registry paths contain keys and values.

Incorrect edits can break applications or Windows. Read settings before changing them, export the relevant key or create a VM snapshot, record the original value and keep a rollback plan. Never import registry files from unknown websites.

Read-only example:
~~~powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" |
    Select-Object ProductName, DisplayVersion, CurrentBuild
~~~

## User Account Control
UAC helps ensure administrative changes require consent or credentials. It supports least privilege. Do not routinely lower or disable it. An elevation prompt does not prove a program is safe; verify the publisher and reason.

## Other controls
- **Secure Boot:** helps ensure trusted boot components are used.
- **BitLocker:** encrypts supported drives at rest.
- **Windows Update:** provides security and reliability fixes.
- **Screen lock:** prevents casual access to an unattended device.
- **Backup and recovery:** support restoration after failure or ransomware.

Availability depends on edition, hardware and configuration. Never upload a BitLocker recovery key or other recovery secret.

## Practical review
Inspect Windows Security, Windows Update and Device Encryption/BitLocker status where available. Record each as enabled, disabled, unavailable or not checked. Do not change encryption settings without understanding recovery-key handling.

## Check yourself
What is the Registry used for? Why is UAC not a malware scanner? Why must recovery keys remain private?
