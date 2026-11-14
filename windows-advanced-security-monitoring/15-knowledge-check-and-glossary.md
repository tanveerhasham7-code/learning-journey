# 15 — Knowledge Check and Glossary

## Part A — Questions
1. What is Windows Event Log used for?
2. Difference between provider and channel?
3. Why does Security Event 4624 not prove malicious activity?
4. What does Advanced Audit Policy control?
5. How does Sysmon complement native logging?
6. What context can Sysmon Event 1 provide?
7. Why interpret Event 3 with process and host context?
8. What is Script Block Logging?
9. Why can PowerShell transcription create privacy risks?
10. What does process parent-child context reveal?
11. Why baseline registry changes?
12. Difference between WEF and SIEM?
13. What makes a detection hypothesis testable?
14. Why must containment follow authorization?
15. What evidence is needed before a lab is Verified?

## Part B — Scenario
A test endpoint records an unexpected script interpreter process. Shortly afterward, Sysmon records a network connection and file creation. PowerShell script-block logging is available.

Write an investigation plan identifying process lineage, user and host context, script sensitivity, network destination, created file, related events, timeline, benign explanations, evidence gaps and escalation recommendation. Do not label the scenario malicious without sufficient evidence.

## Part C — Glossary
- **Audit policy:** configuration controlling which auditable actions are recorded.
- **Channel:** named event-log destination.
- **Collector:** system that receives events from endpoints.
- **Detection:** logic identifying activity for analyst review.
- **Event ID:** identifier for an event type within a provider.
- **EVTX:** Windows event-log file format.
- **False positive:** alert that matches logic but is not the harmful behavior sought.
- **Forwarded Events:** channel commonly used for received WEF records.
- **Parent process:** process that launched another process.
- **Provider:** component that publishes events.
- **Script Block Logging:** PowerShell feature recording processed script blocks.
- **SIEM:** platform for collecting, searching, correlating and alerting on telemetry.
- **Sysmon:** Microsoft Sysinternals system-monitoring service and driver.
- **Telemetry:** data describing system activity or state.
- **WEF:** Windows Event Forwarding.
- **WEC:** Windows Event Collector.

## Authoritative references
- [Microsoft Learn — Windows Security Auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/)
- [Microsoft Learn — Advanced Security Audit Policy](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [Microsoft Sysinternals — Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Microsoft Learn — PowerShell Logging](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging)
- [Microsoft Learn — Windows Event Forwarding](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/use-windows-event-forwarding-to-assist-in-intrusion-detection)
- [Wazuh Documentation](https://documentation.wazuh.com/current/)
- [SigmaHQ](https://sigmahq.io/)

Study rule: Answer in your own words and support practical answers with evidence from your authorized lab.