# SOC Ticketing, Case Management and Escalation

## 1. Purpose

A SOC ticket is the durable record of an alert investigation. It allows analysts to track ownership, evidence, decisions, response actions, deadlines and handovers. A ticket should let another analyst understand what happened without asking the original analyst to repeat the investigation.

## 2. Alert, event, incident and case

- **Event:** An observable activity, such as a logon.
- **Alert:** A detection-generated notification that activity may require review.
- **Incident:** A confirmed or sufficiently credible security event requiring coordinated response under policy.
- **Case / ticket:** The record used to investigate and manage the work. Organizations may use these terms differently.

## 3. Severity and priority

Severity describes the technical/business impact if the activity is real. Priority determines how quickly the organization should work it, considering severity, urgency, asset criticality, exposure, scope and SLA. Do not assume every organization uses the same scale.

Example severity model:
- Critical: widespread compromise, major business disruption or highly privileged compromise.
- High: credible compromise of an important system or account.
- Medium: suspicious activity with limited scope or incomplete confirmation.
- Low: low-impact event or informational investigation.

Priority must follow the organization's matrix, not an analyst's personal preference.

## 4. Minimum ticket fields

- Unique ticket/case ID and linked alert IDs
- Detection name, source system and detection time
- First-seen / last-seen timestamps with timezone
- Affected user, host, IP, application and business owner
- Severity, priority, status, assignee and SLA target
- Investigation summary and evidence references
- Queries, filters and time range used
- Analyst decision and confidence
- Actions taken, approvals and action timestamps
- Escalation target, reason and next update time
- Closure reason and lessons learned

## 5. Recommended case lifecycle

1. New: alert received and queued.
2. Acknowledged: analyst accepts ownership.
3. Triage: validate context, scope and evidence.
4. Investigating: gather and correlate telemetry.
5. Escalated: transfer to the correct team with a clear reason.
6. Pending: waiting for an approved dependency or stakeholder response.
7. Resolved: investigation outcome and authorized actions documented.
8. Closed: required review and closure fields completed.

Actual statuses vary by ticketing platform and organization.

## 6. Escalation rules

Escalate promptly when the playbook requires it, evidence suggests privileged-account compromise, malware execution, lateral movement, sensitive-data exposure, business email compromise, widespread impact, or a containment decision outside Tier 1 authority. Include facts, impact, evidence, actions already taken, uncertainty and the exact help required.

## 7. Good case-note example

**Observed:** Five failed SSH authentication events from one source address appear in the supplied 10-minute lab sample.

**Analysis:** Events share a source and target account. No successful login is present in this sample. The sample does not establish whether the source is malicious or whether the activity continued outside the captured period.

**Decision:** Suspicious authentication activity; escalate for correlation with firewall, VPN and host telemetry.

**Next step:** Tier 2 to review broader time range and related events.

## 8. Practical exercises

- Convert a synthetic SIEM alert into a complete ticket.
- Assign severity and priority using a written sample matrix.
- Write an escalation note with evidence and uncertainty.
- Close a benign alert with a defensible closure reason.

## 9. Common mistakes

Empty ticket descriptions, missing timezone, copied raw logs without interpretation, no evidence references, confusing severity with priority, unsupported claims, and closing cases without documenting why.
