# 10 — Entity Mapping, UEBA and Threat Intelligence

## 1. Entity mapping
Entity mapping links query result fields to recognizable entities such as account, host, IP address, URL, file hash or cloud resource. Correct mapping helps analysts pivot across alerts and incidents.

Bad mapping can mislead investigations. Confirm that a field actually represents the selected entity type.

## 2. UEBA
User and Entity Behavior Analytics (UEBA) identifies patterns that differ from expected user or entity behavior. It can provide context such as unusual activity, peer comparisons or risk signals where supported and configured.

An anomaly is not automatically malicious. Consider role changes, travel, service accounts, maintenance and data quality.

## 3. Threat intelligence
Threat intelligence provides contextual indicators and assessments, such as malicious IPs, domains, URLs or file hashes. Indicator sources vary in freshness and reliability.

Review:
- Source and confidence.
- First/last observed time.
- Expiry and freshness.
- Context and attribution confidence.
- False-positive and shared-infrastructure risk.

## 4. Watchlists versus threat intelligence
A watchlist is a reference list maintained for a use case, such as critical assets or approved IPs. Threat intelligence is externally or internally assessed information about threats. Both need ownership and lifecycle management.

## 5. Practical workflow
1. Validate entity field mapping.
2. Pivot from account to sign-ins and audit activity.
3. Pivot from host to endpoint and network telemetry.
4. Check indicator freshness and confidence.
5. Document why the context supports or does not support the hypothesis.

## 6. Practical task
Create a fictional entity map for an identity alert. Identify account, IP, device and timestamp fields. Explain two ways incorrect mapping could affect investigation.

## 7. Knowledge check
1. Why map entities?
2. What does UEBA try to identify?
3. Why check indicator expiry?
4. Difference between a watchlist and threat intelligence?