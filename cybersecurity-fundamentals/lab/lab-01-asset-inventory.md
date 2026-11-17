# Practical 01 — Asset Inventory

## Objective
Identify the main hardware, operating system, security software, applications, network interfaces, virtual machines, and study-data assets on a personally owned Windows computer. This is a defensive inventory exercise; no scanning or configuration changes were performed.

## Environment
- Host operating system: Windows 10 Pro (shown by the PowerShell system-information query)
- Computer manufacturer: HP (reported by the hardware query)
- Virtualization environment: VMware Workstation Pro 17
- Evidence date: 17 November 2026

## Method and observations

1. **Operating system identification:** `Get-ComputerInfo` returned **Windows 10 Pro**. The selected Windows version and architecture fields were blank in the captured output, so those details are not claimed.
2. **System information cross-check:** the `systeminfo | findstr ...` command displayed the field labels but no values in the screenshot. This is recorded as an incomplete query result, not proof of the OS version or system type.
3. **Hardware identification:** `Get-CimInstance Win32_ComputerSystem` identified the manufacturer as **HP**. Model and total RAM were blank in the captured output.
4. **Storage inventory:** `Get-PhysicalDisk` listed a device named **PC711 NVMe SK**. Media type, size, and health status were not visible in the captured output.
5. **Security software:** Windows Security Center listed **Windows Defender** as a registered antivirus product. The screenshot does not independently verify real-time protection or current security health.
6. **Installed applications:** the registry query displayed applications including 7-Zip, Cisco Packet Tracer, Mozilla Firefox, Microsoft Office, PyCharm, Python, Google Chrome, VirtualBox, and other components. This query reads the specified machine-wide uninstall registry location and may not show every installed application.
7. **Network adapters:** the output showed Wi-Fi (Intel Wi-Fi 6 AX201) and several virtual/network adapters, including VirtualBox Host-Only, VMware VMnet1/VMnet8, TAP-Windows, and Ethernet. Wi-Fi and several virtual adapters were shown as Up; Bluetooth and physical Ethernet were disconnected in this snapshot.
8. **Virtual machines:** VMware Workstation's library showed Windows Server 2008 R2 x64, Windows 7 x64, Kali Linux, Windows 10 x64 (2), Metasploitable2-Linux, and Ubuntu 64-bit.

## Asset inventory summary

| Asset category | Observed assets | Security importance |
|---|---|---|
| Host computer | HP computer | Protect physical access and firmware; keep inventory details private |
| Operating system | Windows 10 Pro | Keep supported and patched; verify exact build separately |
| Storage | PC711 NVMe SK | Protect data and maintain backups; confirm capacity/health separately |
| Endpoint protection | Windows Defender registered | Verify protection status and update signatures |
| Applications | Browser, Office, Python, Packet Tracer, virtualization tools and others | Patch applications and remove software no longer needed |
| Network interfaces | Intel Wi-Fi 6 AX201, Ethernet and virtual adapters | Disable unused interfaces and understand virtual network exposure |
| Virtual lab | Kali, Metasploitable2, Windows, Ubuntu and other VMs | Keep vulnerable training VMs isolated from public and personal networks |
| Study data | Notes, lab reports, screenshots and GitHub projects (identified by the learner) | Back up work and avoid publishing private data or credentials |

## Security recommendations
- Keep Windows and installed applications updated.
- Confirm Windows Security reports protection is enabled and current.
- Keep Metasploitable2 and other intentionally vulnerable lab machines on an isolated host-only network.
- Back up university notes, lab reports, and project files.
- Do not publish serial numbers, account names, private IP details, credentials, or sensitive logs.
- Re-run the incomplete hardware and OS queries with suitable commands if exact model, RAM, Windows build, storage capacity, and health are required.

## Evidence gallery

### 1. Operating system — Windows 10 Pro
![Windows product information](screenshort/Screenshot%202026-11-17%20104354.png)

### 2. System information query — incomplete fields
![System information query output](screenshort/Screenshot%202026-11-17%20104455.png)

### 3. Hardware manufacturer — HP
![Computer hardware information](screenshort/Screenshot%202026-11-17%20104844.png)

### 4. Storage device — NVMe drive listed
![Physical disk inventory](screenshort/Screenshot%202026-11-17%20105032.png)

### 5. Registered antivirus — Windows Defender
![Antivirus inventory](screenshort/Screenshot%202026-11-17%20105147.png)

### 6. Installed applications
![Installed application inventory](screenshort/Screenshot%202026-11-17%20105237.png)

### 7. Network adapters and status
![Network adapter inventory](screenshort/Screenshot%202026-11-17%20105327.png)

### 8. VMware virtual machine library
![Virtual machine inventory](screenshort/Screenshot%202026-11-17%20110559.png)

## Result and completion status
The learner identified the principal host, security software, installed applications, network interfaces, and virtual lab assets, and recorded them in an asset inventory. Some queried fields were blank in the captured command output; those gaps are explicitly documented and should be verified in a follow-up review.

**Status: Completed — initial asset inventory.** This does not mean every hardware attribute or security setting has been fully verified.
