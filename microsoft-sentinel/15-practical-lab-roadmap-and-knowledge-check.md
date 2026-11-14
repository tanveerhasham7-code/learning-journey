# 15 — Practical Lab Roadmap and Knowledge Check

## 1. Lab objective
Build an authorized Microsoft Sentinel training environment to demonstrate workspace setup, ingestion, KQL, detection, incident triage, workbooks and safe automation.

## 2. Before you start
- Confirm access to an authorized Azure tenant and subscription.
- Check current Microsoft Sentinel pricing, free offers, regional availability and trial conditions.
- Set a budget and alert where possible.
- Use synthetic/sample data first.
- Avoid employer or personal logs without explicit permission.
- Record cleanup steps and delete unused paid resources after the lab.

## 3. Proposed architecture

~~~text
Training data / authorized sources
      | identity / Azure / endpoint
      v
Sentinel data connectors
      |
      v
Log Analytics Workspace
      |
      +---- KQL hunting
      |
      +---- Analytics rules
                 |
               Alerts
                 |
              Incidents
                 |
       Analyst investigation
          /             \
     Workbooks      Automation rules
                          |
                     Logic Apps
                 (non-destructive lab)
~~~

## 4. Practical exercise backlog

| ID | Exercise | Evidence expected | Status |
|---|---|---|---|
| MS-01 | Draw Azure resource hierarchy | Tenant/subscription/resource plan | Planned |
| MS-02 | Review current pricing and trial terms | Dated cost notes | Planned |
| MS-03 | Plan workspace and region | Sanitized architecture | Planned |
| MS-04 | Create workspace and enable Sentinel (if authorized) | Redacted setup evidence | Planned |
| MS-05 | Review RBAC and least privilege | Role/scope notes | Planned |
| MS-06 | Explore data connector catalog | Connector inventory | Planned |
| MS-07 | Connect one approved source or sample data | Connector and table evidence | Planned |
| MS-08 | Inspect table schema | Column/type notes | Planned |
| MS-09 | Write five basic KQL queries | Query text and results | Planned |
| MS-10 | Build a hunting query | Hypothesis, query and interpretation | Planned |
| MS-11 | Draft an analytics rule | Rule specification and test plan | Planned |
| MS-12 | Triage a sample alert/incident | Triage notes | Planned |
| MS-13 | Design an entity map and workbook | Screenshots or design | Planned |
| MS-14 | Design a non-destructive playbook | Workflow and permissions | Planned |
| MS-15 | Complete a synthetic incident report | Timeline and case report | Planned |
| MS-16 | Review costs and clean up resources | Cleanup checklist/evidence | Planned |

## 5. Evidence template

~~~markdown
# MS-LAB-XX — Exercise title
Date/time and timezone:
Azure training environment:
Objective:
Authorization/scope:
Resource types (redact IDs):
Steps and configuration:
KQL query:
Expected result:
Actual result:
Evidence filenames (sanitized):
Interpretation:
Cost considerations:
Limitations/troubleshooting:
Status: Planned / In Progress / Verified
~~~

## 6. Completion criteria
- Workspace and Sentinel configuration documented.
- At least one authorized data source or sample dataset queried.
- Five KQL queries explained.
- One hunting hypothesis documented and tested.
- One analytics rule specification tested in a safe environment.
- One incident triage and timeline completed.
- Entity mapping/workbook design documented.
- Automation workflow designed with human approval.
- Cost, permissions, retention and cleanup reviewed.

## 7. Knowledge check
1. What is the role of Log Analytics Workspace?
2. How do data connectors feed Sentinel?
3. What does KQL do?
4. Difference between alert and incident?
5. What is entity mapping?
6. How can a workbook support SOC work?
7. Difference between automation rule and playbook?
8. Why should containment require approval?
9. Name three Sentinel cost considerations.
10. What evidence is needed before marking a lab Verified?

## 8. Glossary
- **Analytics rule:** detection logic evaluated against data.
- **Azure Monitor:** Azure monitoring platform.
- **Data connector:** integration that brings source telemetry into a workspace.
- **Entity mapping:** mapping query fields to recognizable entities.
- **Incident:** investigation container that can group related alerts.
- **KQL:** Kusto Query Language.
- **Logic Apps:** Azure workflow automation service.
- **Log Analytics Workspace:** Azure Monitor Logs environment for storing/querying records.
- **Playbook:** automated workflow, commonly implemented with Logic Apps.
- **RBAC:** role-based access control.
- **SIEM:** security information and event management.
- **SOAR:** security orchestration, automation and response.
- **UEBA:** user and entity behavior analytics.
- **Watchlist:** reference data maintained for query and detection context.

## 9. Authoritative references
- [Microsoft Learn — Microsoft Sentinel documentation](https://learn.microsoft.com/en-us/azure/sentinel/)
- [Microsoft Learn — Kusto Query Language](https://learn.microsoft.com/en-us/kusto/query/)
- [Microsoft Learn — Log Analytics workspaces](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)
- [Microsoft Learn — Sentinel data connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources)
- [Microsoft Learn — Sentinel analytics rules](https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-built-in)
- [Microsoft Learn — Sentinel automation](https://learn.microsoft.com/en-us/azure/sentinel/automation/automation)
- [Microsoft Sentinel pricing](https://azure.microsoft.com/en-us/pricing/details/microsoft-sentinel/)

Study one topic at a time. Do not claim a connector, rule, playbook or lab is working until actual evidence confirms it.