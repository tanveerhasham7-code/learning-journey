# SOC Analyst and SIEM: Beginner to Professional

A defensive cybersecurity learning path combining theory, operational workflows, SIEM engineering, detection, investigation, incident response, practical labs, and a capstone.

> **Lab safety:** Use systems you own, isolated virtual machines, synthetic logs, or explicitly authorized environments. Never test against third-party systems without written permission. Do not commit credentials, tokens, personal data, or unredacted security logs.

## Learning outcomes
Understand SOC operations; collect and interpret telemetry; normalize and query events; build and tune detections; investigate endpoint, identity, network, email, and cloud activity; respond to incidents; document evidence; and communicate risk.

## Roadmap
1. [SOC foundations](01-soc-foundations.md)
2. [Security principles and attack lifecycle](02-security-threats-and-attack-lifecycle.md)
3. [Logs, telemetry, and data sources](03-logs-telemetry-data-sources.md)
4. [SIEM architecture and data engineering](04-siem-architecture-data-engineering.md)
5. [Query languages and threat hunting](05-query-languages-and-hunting.md)
6. [Detection engineering](06-detection-engineering.md)
7. [Endpoint and identity analysis](07-endpoint-and-identity-analysis.md)
8. [Network, email, and cloud investigations](08-network-email-cloud-investigations.md)
9. [Triage and incident response](09-triage-and-incident-response.md)
10. [Threat intelligence and ATT&CK hunting](10-threat-intelligence-attack-hunting.md)
11. [SIEM platforms and workflows](11-siem-platforms-and-workflows.md)
12. [Advanced SOC operations](12-advanced-soc-operations.md)
13. [Practical labs](13-practical-labs.md)
14. [Capstone: mini-SOC](14-capstone-mini-soc.md)
15. [Career checklist and interviews](15-career-checklist-interviews.md)
16. [Glossary and resources](16-glossary-resources.md)
17. [Incident report template](templates/incident-report-template.md)
18. [Detection rule template](templates/detection-rule-template.md)
19. [Lab evidence guide](templates/lab-evidence-guide.md)

## Suggested sequence
- Foundation: Modules 01–04.
- Analyst core: Modules 05–09.
- Advanced: Modules 10–12.
- Portfolio: Complete labs and capstone; publish sanitized queries, synthetic datasets, screenshots, timelines, and reports.

## Suggested home lab
Use a Windows evaluation VM, an Ubuntu VM, and a SIEM/log-analysis platform such as Wazuh or Elastic in an isolated host-only network. Start with synthetic logs if hardware is limited. Add Sysmon after understanding event sources. Keep the lab isolated from sensitive personal systems.

## Professional habits
Validate alerts; correlate independent sources; preserve timestamps and context; separate facts from hypotheses; follow authorization and privacy rules; document false positives; and improve detections from lessons learned.

## Portfolio integrity
These materials are learning resources, not proof that the author has completed labs or worked in a SOC. Add evidence only after personally running each exercise, and label simulated results clearly.

## Completion standard
For every module, explain the concept in your own words, perform the lab, save sanitized evidence, write observations, state limitations, and identify one improvement.
