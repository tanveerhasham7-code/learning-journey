# 13 — Windows Hardening Baseline

## Meaning
Hardening reduces unnecessary exposure and configures a system to resist common threats. It must match the device's role and business requirements.

## Baseline checklist
- Install supported Windows and application updates.
- Remove or disable unused accounts and review privileged group membership.
- Use standard accounts for daily work.
- Enable Defender Antivirus and keep security intelligence current.
- Enable Windows Firewall for relevant profiles.
- Use screen lock and device encryption where supported.
- Review startup applications, services and scheduled tasks.
- Restrict remote access and unused network services.
- Enable appropriate auditing and protect logs.
- Use secure backups and test restoration.
- Apply appropriate Group Policy and application controls.
- Document exceptions and compensating controls.

## Baselines and benchmarks
Microsoft security baselines and CIS Benchmarks are useful references, not universal one-click configurations. Review the device role, application compatibility and current official guidance before applying settings.

## Verify, do not assume
For each control record initial state, desired state, reason, change, verification method, result, exception and rollback.

~~~powershell
Get-NetFirewallProfile | Select-Object Name, Enabled
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
Get-LocalGroupMember -Group "Administrators"
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
~~~

Do not blindly run hardening scripts. They can disable required services, break applications or lock administrators out. Review every line and test in a snapshot.

## Check yourself
Why must hardening be verified? Why might one benchmark setting be unsuitable for a particular server?
