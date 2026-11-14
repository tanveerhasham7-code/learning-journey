# 14 — Splunk Security, Hardening and Administration

## Objectives
Identify key controls for securing and maintaining Splunk.

## 1. Identity and access
Use named accounts, strong authentication, least privilege, and role-based access. Avoid shared administrator accounts. Grant index access and search capabilities according to job duties.

## 2. Platform protection
- Keep Splunk and apps updated under change policy.
- Restrict management and receiving ports.
- Use TLS for data in transit where supported and configured.
- Protect secrets; never store them in public repositories.
- Review authentication and administrative activity.
- Back up configuration and test recovery procedures.
- Separate lab and production environments.

## 3. Data governance
Logs may contain usernames, IP addresses, hostnames, command lines, and personal data. Define collection purpose, access, retention, masking, and deletion requirements. Follow applicable law and organizational policy.

## 4. Platform health
Monitor forwarder connectivity, ingestion volume and latency, parsing errors, timestamp problems, storage, retention, search performance, license or usage warnings, scheduled search failures, and system resources.

## 5. Change management
Document reason and impact, back up configuration, test in an approved environment, obtain required approval, deploy, validate, and record rollback steps.

## Practical task
Create a hardening checklist for a small SOC covering identity, network exposure, encryption, data governance, backup, patching, and monitoring. Mark controls proposed until verified.

## Knowledge check
1. Why use least privilege?
2. Name three sensitive data types in logs.
3. What should be checked after a configuration change?
4. Why monitor ingestion health?

## References
- [Splunk security configuration](https://docs.splunk.com/Documentation/Splunk/latest/Security/ConfigureSplunksecurity)
- [Splunk documentation](https://docs.splunk.com/)
