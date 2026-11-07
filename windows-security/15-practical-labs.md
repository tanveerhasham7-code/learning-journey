# 15 — Windows Security Practical Labs

Perform these exercises only on your own VM or systems you are explicitly authorized to administer. Take a snapshot before configuration changes. Instructions are not proof of completion.

## Lab 1 — System baseline
Run hostname, whoami, winver and Get-ComputerInfo. Record Windows edition, version, build and architecture. Evidence: sanitized screenshot. Explain which features your edition supports.

## Lab 2 — Local accounts and groups
Run Get-LocalUser, Get-LocalGroup and Get-LocalGroupMember -Group "Administrators". Create a standard test account through Settings, sign in and compare its access with an administrator. Remove the test account after the lab. Never publish account secrets.

## Lab 3 — NTFS permissions
Create C:\CyberLab\Reports. Inspect with icacls. Grant a test user read access through folder Properties → Security. Sign in as that user and test read versus write. Restore or remove the test folder. Never modify Windows system-folder permissions.

## Lab 4 — PowerShell inventory
Run the read-only inventory example in chapter 04. Save a short report in your lab folder. Review it for private identifiers before sharing. Evidence: script and sanitized output.

## Lab 5 — Processes and services
Run Get-Process and Get-Service. Research three expected services and record purpose, state and startup type. Do not stop critical or unfamiliar services.

## Lab 6 — Network configuration
Run ipconfig /all, Get-NetIPConfiguration and Get-DnsClientServerAddress. Resolve a known domain and test HTTPS using Test-NetConnection example.com -Port 443. Explain address, gateway, DNS and result. Redact identifying network details.

## Lab 7 — Event Viewer
Open eventvwr.msc. Review System and Application events. Use Get-WinEvent -LogName System -MaxEvents 20. Sign out and back into the lab VM, then inspect Security events if auditing is enabled. Record a short timeline.

## Lab 8 — Firewall review
Run Get-NetFirewallProfile and inspect enabled inbound rules. Confirm firewall protection is enabled for the active profile. Do not turn off the firewall or expose services to the internet. Evidence: sanitized profile status.

## Lab 9 — Defender status
Open Windows Security → Virus & threat protection and inspect status. Run Get-MpComputerStatus if available. Optionally use the harmless official EICAR test file in a controlled lab, following EICAR instructions. Never use real malware or disable protection.

## Lab 10 — Group Policy
Check whether gpedit.msc is available. Inspect account, audit and Defender policy sections. Run gpresult /r. Change only one low-risk setting in a snapshot after recording its original value, verify it and restore it.

## Lab 11 — Active Directory design
Design a fictional company directory with OUs for Users, Workstations and Servers. Create role-based group designs such as Helpdesk-Readers and Finance-Users. Explain permissions and privileged account separation. Evidence: diagram and design notes.

## Lab 12 — Optional AD DS deployment
In an isolated network, deploy a Windows Server Evaluation VM as a domain controller and a Windows client. Configure the client to use lab DNS, verify name resolution, join the test domain and sign in with a test domain account. Document problems and fixes. Never test against an organization domain without explicit permission.

## Lab 13 — Hardening review
Review updates, firewall, Defender, local Administrators, screen lock and encryption status. Mark each Enabled, Disabled, Not available or Not checked. Recommend safe improvements and verify any changes.

## Lab 14 — Final project: Windows Endpoint Security Baseline
Deliver:
- System inventory and VM/software versions.
- Local account and administrator group review.
- NTFS test-folder permission demonstration.
- Network configuration and firewall review.
- Defender status and event-log summary.
- Hardening checklist with verification evidence.
- Risk findings, recommendations and rollback notes.

### Final report structure
Objective and scope; environment; method and commands; findings and evidence; risks; recommended changes; verification and rollback; lessons learned and limitations.

## Evidence naming
Use names such as lab-01-system-info.png, lab-02-admin-group.png and lab-07-event-review.png. Mark a lab complete only after performing it and checking the evidence.
