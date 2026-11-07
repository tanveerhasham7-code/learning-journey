# 16 — Glossary and Learning Resources

## Glossary
- **Alert:** Notification that activity may require review.
- **Asset:** Valuable system, data, identity, or service.
- **ATT&CK:** Knowledge base of adversary tactics and techniques.
- **Case:** Record of an investigation and its evidence/actions.
- **Correlation:** Connecting related events across time or sources.
- **Detection engineering:** Designing, testing, deploying, and maintaining analytics.
- **EDR:** Endpoint Detection and Response.
- **Enrichment:** Adding context to an event or alert.
- **False positive:** Alert that does not represent the targeted malicious behavior under the rule's definition.
- **IOC:** Indicator of Compromise.
- **IOA:** Indicator of Attack.
- **Ingestion:** Bringing telemetry into a platform.
- **Log source:** System or service that generates records.
- **MTTA:** Mean time to acknowledge.
- **MTTD:** Mean time to detect.
- **MTTR:** Often mean time to respond or recover; define locally.
- **Normalization:** Mapping different records to consistent fields and meanings.
- **Parser:** Component that extracts structured fields from raw data.
- **Playbook:** Documented steps for handling a scenario.
- **SIEM:** Security Information and Event Management.
- **SOAR:** Security Orchestration, Automation, and Response.
- **SOC:** Security Operations Center.
- **Telemetry:** Observable data from systems and services.
- **Threat hunting:** Proactive, hypothesis-driven search for threats.
- **TTP:** Tactics, techniques, and procedures.
- **UEBA:** User and Entity Behavior Analytics.
- **XDR:** Extended Detection and Response.

## Official documentation and frameworks
Use official sources for current syntax, product behavior, and framework details:
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- NIST SP 800-61 Computer Security Incident Handling Guide: https://csrc.nist.gov/pubs/sp/800/61/r2/final
- MITRE ATT&CK: https://attack.mitre.org/
- MITRE D3FEND: https://d3fend.mitre.org/
- CISA Cybersecurity resources: https://www.cisa.gov/cybersecurity
- Microsoft Sentinel documentation: https://learn.microsoft.com/azure/sentinel/
- Microsoft Kusto Query Language: https://learn.microsoft.com/azure/data-explorer/kusto/query/
- Splunk Search Reference: https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual
- Elastic Security documentation: https://www.elastic.co/guide/en/security/current/index.html
- Wazuh documentation: https://documentation.wazuh.com/current/
- OCSF schema: https://schema.ocsf.io/
- Elastic Common Schema: https://www.elastic.co/guide/en/ecs/current/index.html
- Sigma detection format: https://sigmahq.io/

## Study advice
Start with operating systems and networking, then logs and SIEM architecture, then queries and detection, then investigation and response. Practise one small lab at a time. Keep a glossary and write your own explanations. Vendor interfaces change, so focus on transferable concepts and verify syntax in current documentation.

## Resource safety
Use official downloads and documentation. Be careful with random log samples and malware repositories. Do not download or execute malware for beginner labs. Prefer synthetic data, safe test events, and isolated virtual machines.
