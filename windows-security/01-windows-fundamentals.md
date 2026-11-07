# 01 — Windows Fundamentals and Architecture

## What is Windows?
Windows is an operating-system family for personal computers and servers. It manages hardware, memory, processes, files, users, applications and network communication. Security is built into these areas: Windows authenticates identities, checks permissions, isolates processes and records selected activity.

## Main architecture
- **Kernel:** core operating-system component that manages memory, processes, threads and hardware access.
- **User mode:** restricted environment where ordinary applications run.
- **Kernel mode:** highly privileged environment for the kernel and trusted drivers. A kernel failure can affect the whole system.
- **Drivers:** allow Windows to communicate with hardware.
- **Services:** background processes providing functions such as updates, networking and event logging.
- **Registry:** hierarchical configuration database for Windows and applications.
- **NTFS:** common Windows file system with permissions, auditing and other features.
- **Access token:** information about a user and group memberships used during access checks.

## Windows editions
Home, Pro, Enterprise and Education do not offer identical management features. Domain join, Local Group Policy tools and some advanced security controls depend on edition and configuration. Windows Server supports server roles such as Active Directory Domain Services. Always identify your edition first.

## Boot and sign-in overview
Firmware starts the boot process. Windows Boot Manager selects the installation, the Windows loader loads required components, and the kernel initializes. Windows starts services and displays the sign-in interface. Secure Boot, when supported and enabled, helps ensure trusted boot components are used.

## Essential security terms
- **Authentication:** proving who you are.
- **Authorization:** deciding what you may access.
- **Least privilege:** giving only the access needed for a task.
- **UAC:** prompts for consent or credentials before many administrative changes.
- **Security principal:** a user, group or computer identity.
- **SID:** a unique Security Identifier for a security principal.

## Read-only practical commands
~~~powershell
hostname
whoami
winver
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber, OsArchitecture
systeminfo
~~~

Record the edition, version, build and architecture in a lab report. Remove identifying details before publishing.

## Defensive habits
Keep systems patched, use a standard account daily, enable firewall and endpoint protection, review accounts and services, back up important files and document administrative changes.

## Check yourself
1. Explain user mode versus kernel mode.
2. Explain authentication versus authorization.
3. Why should a daily account normally not be a local administrator?
