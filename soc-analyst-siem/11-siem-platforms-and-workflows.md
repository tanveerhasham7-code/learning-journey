# 11 — SIEM Platforms and Practical Workflows

## Platform-neutral knowledge first
Learn the underlying concepts before memorizing a vendor interface: data onboarding, parsing, normalization, field mapping, search, correlation, alerting, dashboards, case management, access control, retention, and health monitoring.

## Common platforms
- **Microsoft Sentinel:** Cloud-native SIEM/SOAR in the Microsoft security ecosystem; KQL is central to many investigations.
- **Splunk Enterprise Security:** SIEM content and investigations built on Splunk data and SPL searches.
- **Elastic Security:** Security analytics and investigation using the Elastic data platform and supported query languages.
- **IBM QRadar:** SIEM platform with event/flow processing, rules, offenses, and integrations.
- **Wazuh:** Open-source security monitoring platform with agents, log analysis, integrity monitoring, vulnerability detection, and integrations.

Features, licensing, table names, and query syntax change by version and deployment. Consult the official documentation for the version used in your lab.

## Core analyst workflow
1. Open alert and read rule description.
2. Confirm timestamp, source, severity, and affected entity.
3. Open raw event and validate parsed fields.
4. Search related events for the same user, host, IP, process, or session.
5. Build a timeline and identify expected behavior.
6. Add asset and identity context.
7. Record findings and disposition.
8. Escalate or close according to procedure.

## SIEM engineering workflow
1. Define source owner and security use case.
2. Select collection method and permissions.
3. Onboard a test source.
4. Validate event arrival and latency.
5. Inspect raw and parsed records.
6. Map fields to a consistent schema.
7. Create a saved query and test it.
8. Build a detection with documentation and test cases.
9. Configure routing and case ownership.
10. Monitor health, cost, and performance.

## Dashboards
Useful dashboards may show ingestion health, event volume by source, active alerts by severity, aging cases, mean time to acknowledge, mean time to respond, endpoint coverage, identity risk, detection status, and top recurring false positives. A dashboard should answer a question and have an owner; decorative charts are not operational value.

## Platform comparison exercise
Create a comparison matrix for two SIEM platforms. Compare ingestion, supported sources, query language, normalization, detection content, SOAR integrations, case management, retention, access control, deployment, cost, and learning resources. Use current vendor documentation for version-specific claims.

## Safe beginner lab choice
Wazuh is a useful learning option for a small home lab, while Sentinel, Splunk, and Elastic provide exposure to widely used enterprise workflows. Select based on hardware, free-tier terms, and learning objectives. Do not upload sensitive logs to a public cloud workspace.

## Knowledge check
1. Why learn concepts before vendor-specific syntax?
2. What should be validated after onboarding a log source?
3. What makes a dashboard useful?
4. Which platform uses KQL in common Sentinel workflows?
5. Why check current documentation for version details?
