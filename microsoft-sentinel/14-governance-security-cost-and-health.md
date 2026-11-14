# 14 — Governance, Security, Cost and Operational Health

## 1. Governance
Define who owns the workspace, data connectors, detections, playbooks, retention and incident process. Document data classification, region requirements, access reviews and change approval.

## 2. Access control
Use least privilege and role separation. Review workspace and subscription scopes, privileged identities, service principals and managed identities. Remove access when no longer needed and protect automation credentials.

## 3. Data protection
Logs can contain personal data, IP addresses, usernames, URLs, command lines and business-sensitive details. Apply approved retention, access controls, export restrictions and redaction before portfolio publication.

## 4. Cost management
Cost can depend on ingestion volume, retention, analytics/search features, data tiers, automation and connected services. Before deployment:
- Estimate daily data volume.
- Review current regional pricing and eligible free allowances.
- Select retention according to policy.
- Configure budgets and alerts where supported.
- Monitor ingestion by table/source.
- Remove unused lab resources after preserving sanitized evidence.

Never assume a trial means unlimited or zero-cost use.

## 5. Operational health
Monitor connector status, agent health, ingestion delay, missing tables, parsing errors, query failures, rule execution and automation failures. A detection that silently stops receiving data creates a visibility gap.

## 6. Change management
Version-control KQL and detection documentation. Review changes, test in a lab, document rollback and record who approved production updates.

## 7. Practical task
Create a one-page Sentinel operations checklist covering identity, access, data sources, retention, cost, detection health, automation and evidence handling.

## 8. Knowledge check
1. Why review access regularly?
2. Name four cost drivers.
3. Why is connector health a security concern?
4. Why version-control detection queries?