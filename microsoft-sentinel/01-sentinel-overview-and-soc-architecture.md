# 01 — Microsoft Sentinel Overview and SOC Architecture

## 1. What is Microsoft Sentinel?
Microsoft Sentinel is a cloud-native Security Information and Event Management (SIEM) and Security Orchestration, Automation and Response (SOAR) platform. It collects security data from supported sources, allows analysts to query it, detects suspicious patterns and supports investigation and response workflows.

- **SIEM:** centralizes telemetry, search, correlation, alerting and investigation.
- **SOAR:** coordinates or automates repeatable response tasks.
- **Cloud-native:** delivered as a Microsoft cloud service rather than a traditional server that the customer installs and maintains.

Sentinel does not automatically protect every resource simply because it is enabled. Data sources, permissions, configuration, detections and operational processes must be set up.

## 2. Main components
- **Log Analytics Workspace:** Azure Monitor Logs data store and query context used by Sentinel.
- **Data connectors:** bring supported telemetry into the workspace.
- **Tables:** store records in structured schemas.
- **KQL:** query language used to search and analyze records.
- **Analytics rules:** identify patterns and generate alerts/incidents.
- **Incidents:** analyst-facing cases that group related alerts and entities.
- **Workbooks:** interactive dashboards and reports.
- **Automation rules and playbooks:** coordinate actions, commonly using Logic Apps.
- **Threat intelligence and UEBA capabilities:** enrich analysis when configured and available.

## 3. High-level architecture

~~~text
Identity | Endpoint | Network | Cloud | Applications
                     |
               Data connectors
                     |
                     v
          Log Analytics Workspace
             Tables / Records
                     |
               KQL queries
                     |
          Analytics / Detection rules
                     |
                Alerts
                     |
                Incidents
                     |
        SOC triage and investigation
              /             \
        Workbooks       Automation rules
                              |
                         Playbooks
                         (Logic Apps)
~~~

## 4. Typical SOC workflow
1. Data arrives from a configured source.
2. The analyst confirms ingestion and field quality.
3. A scheduled or near-real-time detection evaluates data.
4. A matching condition creates an alert.
5. Related alerts may be grouped into an incident.
6. The analyst validates entities, timeline, scope and context.
7. The analyst closes, escalates or responds according to policy.
8. Results and detection quality are documented.

Exact behavior depends on connector, rule type, configuration and service capabilities.

## 5. Sentinel versus traditional on-premises SIEM
A traditional SIEM may require the organization to operate servers, storage and upgrades. Sentinel is managed as a cloud service, but customers still manage data sources, access, detections, cost, retention, governance and response processes.

## 6. Important limitations
- No data connector means no corresponding telemetry.
- Ingestion delay or missing fields can weaken detections.
- A detection is not proof of compromise.
- Cloud costs depend on data volume, retention and selected features.
- Playbooks require permissions and careful safeguards.
- Features and portal workflows change; check current Microsoft documentation.

## 7. Example
An identity connector ingests sign-in records. An analyst uses KQL to find repeated failures followed by a successful sign-in. An analytics rule may create an alert; the incident is investigated using account, IP, device, location context and related activity. This sequence is a learning example, not a claim of a live detection.

## 8. Knowledge check
1. Difference between SIEM and SOAR?
2. What role does the workspace perform?
3. Why are connectors necessary?
4. Does enabling Sentinel guarantee that all security logs are collected?