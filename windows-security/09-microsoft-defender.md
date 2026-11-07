# 09 — Microsoft Defender and Endpoint Security

## Endpoint protection
An endpoint is a device such as a laptop, desktop or server. Endpoint security aims to prevent, detect and respond to unsafe activity.

Microsoft Defender Antivirus provides malware protection on supported Windows editions. Microsoft Defender for Endpoint is a broader enterprise security platform with capabilities that depend on licensing and configuration. They are not the same product.

## Protection concepts
- **Real-time protection:** checks files and activity as they occur.
- **Cloud-delivered protection:** uses cloud intelligence when enabled.
- **Security intelligence updates:** update detection information.
- **Tamper protection:** helps prevent unauthorized changes to security settings.
- **Controlled Folder Access:** can help protect selected folders.
- **Attack Surface Reduction:** rules can reduce risky behaviors; test compatibility carefully.

## Inspect Defender status
~~~powershell
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, BehaviorMonitorEnabled, AntivirusSignatureLastUpdated
Get-MpPreference | Select-Object DisableRealtimeMonitoring, MAPSReporting, PUAProtection
~~~

Availability and property values vary. You can also review Windows Security → Virus & threat protection.

## Safe detection test
The official EICAR anti-malware test file is a harmless test string designed to be detected by many antivirus products. Use it only in a controlled lab and follow EICAR's official instructions. Do not disable protection to make a test work and do not use real malware.

## Alert triage
Record alert name, time, device and file path. Review the action taken, protection status and related alerts. Follow incident procedures. Do not restore or execute a detected file merely to inspect it.

Antivirus cannot guarantee detection of every threat. Combine it with patching, least privilege, backups, network controls and monitoring.

## Check yourself
How does real-time protection help? Why should you not disable Defender to run an unknown file?
