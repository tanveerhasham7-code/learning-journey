# 16 — Windows Troubleshooting

## PowerShell command not found
Check spelling, Windows version, module availability and command discovery with Get-Command. Do not install modules from unknown sources.

## Access denied
Check whether elevation is required, then review account membership and target permissions. Do not permanently run every shell as Administrator.

## Local Users and Groups tools unavailable
Some Windows editions lack certain snap-ins. Use supported Settings pages or PowerShell cmdlets and check edition/module availability.

## Group Policy Editor unavailable
gpedit.msc is not included in every Windows edition. Local and domain policy features differ. Avoid unofficial scripts that claim to force-install management components.

## DNS or domain join failure
Confirm client and server are on the same isolated network, the client uses the domain controller for DNS, the domain resolves, system time is synchronized and required services are available.

## Firewall blocks an application
Identify active profile, application, protocol, port and matching rules. Add only a narrow justified rule in the lab. Do not permanently disable the firewall.

## Event logs appear empty
Check selected log, time range, audit policy and read permissions. Not every action creates a Security event.

## Defender cmdlets unavailable
Check platform, edition and PowerShell session. Use Windows Security UI to inspect status. Some settings may be managed by policy.

## Safe troubleshooting method
Capture exact error and time; identify expected behavior; change one thing at a time; verify; restore original configuration; document cause and fix without exposing secrets.
