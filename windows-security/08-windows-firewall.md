# 08 — Windows Defender Firewall

## Purpose
Windows Defender Firewall filters network traffic using rules. It helps reduce unwanted inbound connections and can also control outbound traffic. It is one layer of defense, not a replacement for patching or endpoint protection.

## Profiles
- **Domain:** for an authenticated domain network.
- **Private:** for a network the user trusts.
- **Public:** for untrusted networks such as public Wi-Fi.

## Inspect status and rules
~~~powershell
Get-NetFirewallProfile | Format-Table Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-NetFirewallRule -Enabled True | Select-Object DisplayName, Direction, Action, Profile
~~~

## Rule concepts
Rules specify direction, action, profile, protocol, ports, addresses, program and service. Prefer narrow rules tied to a real requirement. Avoid broad rules that allow all inbound traffic.

## Safe lab
1. Record current profile status and default actions.
2. Confirm firewall is enabled for the active profile.
3. Review enabled inbound allow rules.
4. In an isolated VM only, create a temporary narrow test rule if needed and if you understand the effect.
5. Verify the rule, then remove it.
6. Record before/after evidence.

To inspect a matching rule:
~~~powershell
Get-NetFirewallRule -DisplayName "*Remote Desktop*" |
    Select-Object DisplayName, Enabled, Direction, Action, Profile
~~~

Do not enable Remote Desktop or open ports on an internet-facing device for this exercise.

## Troubleshooting
Check the active profile, matching rules, application path, protocol and port. Do not disable the firewall as the first troubleshooting step. Restore any temporary test configuration.

## Check yourself
What is the difference between inbound and outbound rules? Why should Public profile rules be restrictive?
