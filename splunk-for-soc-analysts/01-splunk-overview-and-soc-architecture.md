# 01 — Splunk Overview and SOC Architecture

## Objectives
Understand Splunk, its main components, and how security events travel from an endpoint to a SOC analyst.

## 1. What is Splunk?
Splunk collects, indexes, searches, analyzes, and visualizes machine-generated data. SOC teams use it as a SIEM platform to centralize logs, investigate activity, create detections, and monitor security operations. An alert is an investigation lead, not automatic proof of compromise.

## 2. Main components
- **Splunk Enterprise:** self-managed Splunk platform.
- **Splunk Cloud Platform:** hosted Splunk service.
- **Universal Forwarder (UF):** lightweight agent that collects configured data and forwards it.
- **Heavy Forwarder:** can receive, parse, filter, and forward data when the architecture needs it.
- **Indexer:** processes and stores events for searching.
- **Search Head:** provides the analyst search interface and search-processing role.
- **Deployment Server / Cluster Manager:** management roles used in specific deployment designs.

## 3. SOC data flow
1. Windows records a logon event.
2. A collection input reads the event.
3. A forwarder or supported ingestion method sends it to Splunk.
4. Splunk parses the event and assigns metadata.
5. The indexer stores it.
6. An analyst searches it using SPL.
7. A saved search may generate an alert.
8. The analyst validates context, investigates, and documents findings.

## 4. Important terms
- **Event:** one recorded activity.
- **Log source:** system or application creating events.
- **Ingestion:** bringing data into Splunk.
- **Parsing:** interpreting raw data and timestamps.
- **Indexing:** storing events for search.
- **Correlation:** connecting related observations.
- **Detection:** analytic logic that identifies activity for review.

## 5. SOC use cases
Repeated failed logons, privileged group changes, unusual PowerShell execution, unexpected services, suspicious DNS activity, and endpoint protection alerts. Each requires validation and context.

## Practical task
Draw an architecture: Windows endpoint → UF/collection method → Splunk receiver/indexer → Search Head → SOC analyst. Explain each component. Save the diagram as evidence.

## Knowledge check
1. Forwarder versus indexer?
2. What does a Search Head do?
3. Why is field normalization useful?
4. Does an alert prove compromise?

## References
- [Splunk documentation](https://docs.splunk.com/)
- [Splunk architecture](https://docs.splunk.com/Documentation/Splunk/latest/Deploy/IntroductiontoSplunk)
