# Windows Administration & Security

A cybersecurity-focused notebook for Windows administration, endpoint defense, identity management, monitoring and practical labs.

> Portfolio honesty: these are learning notes and lab instructions. Mark a lab complete only after you perform it, verify the result and add your own evidence.

## Learning outcomes
- Understand Windows architecture, editions, accounts, services, registry and NTFS.
- Manage local users, groups and file permissions using supported tools.
- Use PowerShell for system inventory and defensive administration.
- Investigate Windows events and build a basic timeline.
- Inspect Windows Defender Firewall and Microsoft Defender Antivirus.
- Understand UAC, Group Policy, Active Directory, DNS and Kerberos.
- Apply and verify a safe Windows hardening baseline.

## Recommended lab setup
Use a Windows 10/11 virtual machine with snapshots. For advanced Active Directory practice, add a separate Windows Server Evaluation VM and a Windows client on an isolated internal/host-only virtual network. Do not expose a lab domain controller to the public internet. Feature availability differs by Windows edition; check your version before each exercise.

## Study chapters
1. [Windows fundamentals](01-windows-fundamentals.md)
2. [Accounts, groups and authentication](02-accounts-groups-authentication.md)
3. [NTFS permissions](03-ntfs-permissions.md)
4. [PowerShell](04-powershell.md)
5. [Processes, services and scheduled tasks](05-processes-services-tasks.md)
6. [Windows networking](06-windows-networking.md)
7. [Event Viewer and logging](07-event-viewer-logging.md)
8. [Windows Defender Firewall](08-windows-firewall.md)
9. [Microsoft Defender](09-microsoft-defender.md)
10. [Registry, UAC and security controls](10-registry-uac-security-controls.md)
11. [Group Policy](11-group-policy.md)
12. [Active Directory](12-active-directory.md)
13. [Windows hardening](13-windows-hardening.md)
14. [Incident triage](14-incident-triage.md)
15. [Practical labs](15-practical-labs.md)
16. [Troubleshooting](16-troubleshooting.md)
17. [Checklist, glossary and resources](17-checklist-glossary-resources.md)
18. [Lab report template](LAB-REPORT-TEMPLATE.md)

## Evidence folders
Save sanitized screenshots in windows-security/evidence/lab-01-system-baseline, lab-02-accounts, lab-03-permissions, lab-04-powershell, lab-05-logging, lab-06-firewall, lab-07-defender and so on. Never upload passwords, hashes, recovery keys, tokens, private keys, sensitive logs or identifying personal data.

## Final project
Build a Windows endpoint security baseline report containing system inventory, account review, NTFS test, network configuration, firewall and Defender status, event-log review, hardening checklist, evidence and recommendations.

## Progress
- [ ] Study the chapters
- [ ] Perform the practical labs in an isolated VM
- [ ] Capture and sanitize evidence
- [ ] Complete and review the final project
