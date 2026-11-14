# 09 — Defender, Firewall and Endpoint Protection Telemetry

## 1. Endpoint protection telemetry
Microsoft Defender and related Windows components can record detections, remediation, health, configuration changes and scans. Channels and event IDs vary by Windows release and product configuration.

## 2. What SOC analysts review
- Detection name and severity.
- Detection time and affected device.
- File, process or object involved.
- Action taken: blocked, quarantined, removed or failed.
- Protection status and update health.
- User context and related process activity.
- Whether the detection reappeared after remediation.

A successful quarantine does not prove all related activity has stopped.

## 3. Windows Firewall
Windows Defender Firewall controls traffic according to profiles and rules. Configured logging can record dropped packets and permitted connections. Firewall logs do not normally provide the same process lineage as Sysmon or EDR.

Review profile, rule scope, direction, protocol, ports and source/destination.

## 4. Read-oriented commands

~~~powershell
# Defender status where available
Get-MpComputerStatus

# Firewall profiles
Get-NetFirewallProfile

# Enabled firewall rules
Get-NetFirewallRule -Enabled True |
Select-Object DisplayName, Direction, Action, Profile
~~~

Output varies by edition, policy and installed product.

## 5. Event channels
Review Microsoft-Windows-Windows Defender/Operational and relevant Firewall logging on the actual system. Confirm provider and event details instead of relying on memorized IDs.

## 6. Detection ideas
Unexpected protection degradation, repeated detections, failed remediation, disabled firewall profile or new broad inbound rules may deserve investigation. Validate maintenance and policy context.

## 7. Practical task
Record Defender status and firewall profile state on a test endpoint. Review available channels. Do not disable protections to create an alert.

## 8. Knowledge check
1. Why inspect remediation status?
2. What context can firewall logs lack?
3. Why monitor endpoint protection health?
4. Why verify event IDs against OS version?