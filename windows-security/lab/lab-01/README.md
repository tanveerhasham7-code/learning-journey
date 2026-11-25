# Lab 1 — Windows System Baseline

## Lab details

- **Lab:** 01 — System Baseline
- **Date performed:** 25 November 2026
- **Platform:** Physical Windows endpoint (not a VM, based on the supplied evidence)
- **Objective:** Identify the Windows edition, version, build, architecture, computer name and current account using built-in Windows tools.
- **Scope:** Read-only system inventory on the learner's own Windows computer.

## Environment

| Field | Observed result |
|---|---|
| Operating system | Microsoft Windows 11 Pro |
| Version | 26H2 (reported from the `winver` window by the learner) |
| OS build | 26300.9974 (reported from `winver`; also visible in the Command Prompt banner) |
| Computer name | `DESKTOP-6RQ03JO` |
| Current account | `hp` |
| Architecture | 64-bit |
| Installation type | Client |
| OS configuration | Standalone Workstation |
| System manufacturer/model | HP / HP ProBook 650 G8 Notebook PC (visible in the captured `systeminfo` output) |

> **Privacy note:** Before keeping these screenshots in a public portfolio, redact the Product ID and consider masking the computer name, account name and other device details. Do not publish serial numbers, product keys, credentials or other secrets.

## Objective and theory

A system baseline is a snapshot of the endpoint's basic configuration. SOC analysts use this information to understand which operating system and architecture they are investigating, identify the endpoint, and provide context when reviewing alerts or logs.

## Procedure performed

The learner performed the following read-only checks:

1. Opened `winver` and reported Windows 11 Pro, Version 26H2, OS Build 26300.9974.
2. Ran `hostname` in Command Prompt to identify the computer name.
3. Ran `whoami` to identify the current Windows account.
4. Opened Windows PowerShell and ran:

   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture
   ```

5. Queried additional operating-system fields:

   ```powershell
   Get-ComputerInfo | Select-Object WindowsEditionId, WindowsInstallationType, OsName
   ```

6. Ran `systeminfo` in Command Prompt and reviewed the OS name, version and system type.

## Results and analysis

- `hostname` returned `DESKTOP-6RQ03JO`.
- `whoami` returned `desktop-6rq03jo\\hp`.
- `systeminfo` identified the OS as **Microsoft Windows 11 Pro**, with version **10.0.26300** and system type **x64-based PC**.
- PowerShell's `OsName` field also returned **Microsoft Windows 11 Pro**.
- `WindowsEditionId` returned `Professional`, and `WindowsInstallationType` returned `Client`.
- The learner reported that `winver` displayed **Windows 11 Pro, Version 26H2, OS Build 26300.9974**.

### Data-field discrepancy

The `WindowsProductName` field from `Get-ComputerInfo`, and the registry `ProductName` value, displayed **Windows 10 Pro**. However, the `OsName` field and `systeminfo` both identified **Microsoft Windows 11 Pro**. The baseline records this inconsistency rather than silently changing or omitting the output. The OS identity is supported by the `OsName` and `systeminfo` results; the differing product-name metadata remains an observation.

### Command-line troubleshooting

The learner first attempted `Get-ComputerInfo` in Command Prompt, where it was not recognized. This is expected because `Get-ComputerInfo` is a PowerShell cmdlet, not a CMD command. The learner then opened PowerShell and successfully ran the cmdlet. An additional parser error occurred after the CMD error text was pasted into PowerShell; the learner corrected this by entering the actual command.

## Evidence

1. [Screenshot 1 — PowerShell OS fields and systeminfo output](../screenshort/lab-01/Screenshot%202026-11-25%20143246.png)  
   Shows `OsName` as Windows 11 Pro, the `systeminfo` output, and the x64-based system type. It also contains a visible Product ID; redact that before public portfolio use.

2. [Screenshot 2 — Run dialog with winver command](../screenshort/lab-01/Screenshot%202026-11-25%20143347.png)  
   Shows the `winver` command being entered. It does **not** show the resulting About Windows window, so the reported 26H2/build details are recorded as learner-provided rather than independently visible in this image.

3. [Screenshot 3 — CMD hostname, whoami and command troubleshooting](../screenshort/lab-01/Screenshot%202026-11-25%20143408.png)  
   Shows the computer name, account name and the initial expected error from attempting to run a PowerShell cmdlet in CMD.

## Security observations

- Identifying the exact OS and architecture is useful when selecting appropriate endpoint security controls, investigation steps and software versions.
- `hostname`, `whoami`, `systeminfo` and `Get-ComputerInfo` provide useful baseline context without changing system configuration.
- Hostnames, account names and product identifiers can reveal information about a device. Sanitize screenshots before publishing them publicly.

## Troubleshooting summary

| Issue | Cause | Resolution |
|---|---|---|
| `Get-ComputerInfo` not recognized | PowerShell cmdlet was entered in CMD | Opened Windows PowerShell and ran the cmdlet there |
| Parser error: unexpected token | Error text was pasted as if it were a command | Cancelled the invalid input and entered only the PowerShell command |

## Cleanup and rollback

No configuration changes, accounts, services, firewall rules or files were created by this lab. No rollback was required.

## Learning reflection

This lab practiced collecting endpoint identity and operating-system information with CMD and PowerShell. It also demonstrated why command-shell context matters and why analysts should document inconsistent system fields instead of assuming every source reports identical metadata.

## Status

- [x] Planned
- [x] Performed
- [x] Evidence captured
- [x] Reviewed
- [x] Published

**Evidence limitation:** The screenshots show the successful PowerShell/systeminfo checks and the earlier CMD troubleshooting. The `winver` result itself was reported by the learner but is not visible in the uploaded Run-dialog screenshot.
