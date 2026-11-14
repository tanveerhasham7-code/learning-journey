# SOC Operations, Metrics and Shift Handover

## 1. How a SOC queue works

A SOC queue contains alerts or cases waiting for acknowledgement, triage, investigation, escalation or closure. Analysts should work according to documented severity, priority, SLA, playbooks and escalation paths—not simply the newest alert first.

## 2. Operational terms

- **Alert volume:** Number of alerts received in a defined period.
- **False positive:** Detection fired but the activity did not meet the intended malicious condition.
- **Benign positive:** Detection correctly identified the activity, but the activity was authorized or expected.
- **True positive:** Detection correctly identified activity that meets the malicious or policy-violation condition.
- **Inconclusive:** Available evidence is insufficient to decide.
- **MTTD:** Mean time to detect.
- **MTTA:** Mean time to acknowledge.
- **MTTR:** Mean time to respond or remediate; organizations define the exact start/end points differently.
- **SLA:** Agreed service-level target for acknowledgement, update or resolution.
- **Backlog:** Open work waiting for action.

## 3. Using metrics responsibly

Metrics can reveal queue pressure, detection quality and response delays, but they can be misleading without definitions and context. A lower alert count is not automatically better; it may reflect missing telemetry. A low false-positive rate is not useful if detections miss real threats.

Always define:
- Reporting period and timezone
- Included alert/case categories
- Start and end timestamps
- Paused or pending time treatment
- Severity and priority grouping
- Data exclusions and limitations

## 4. Shift handover checklist

For every open case, communicate:
1. Case ID, severity, priority and SLA status
2. Affected users, hosts, assets and business service
3. Short incident summary and current assessment
4. Confirmed facts versus hypotheses
5. Timeline and key evidence references
6. Queries and time ranges already checked
7. Actions completed and approvals obtained
8. Outstanding tasks and exact next steps
9. Escalation contact/team and pending response
10. Next update deadline and relevant communication channel

Never rely on verbal handover alone for important case details. Update the ticket or approved case system.

## 5. Example handover

**Case:** SOC-TRAINING-014  
**Priority:** Medium (training example only)  
**Status:** Investigating  
**Summary:** Several failed authentication events from one source were found in synthetic lab logs. No successful login is visible in the supplied sample.  
**Completed:** Grouped events by source and account; checked the provided sample range.  
**Unknown:** Whether activity continued outside the sample and whether the source is expected.  
**Next:** Correlate with VPN/firewall and endpoint logs; escalate if additional evidence supports compromise.  
**Reminder:** The case is simulated; it is not a real incident.

## 6. Practical exercises

- Prioritize a synthetic alert queue using a supplied severity/SLA matrix.
- Calculate MTTD and MTTA from fictional case timestamps.
- Prepare a handover note for three unresolved training cases.
- Identify how a missing telemetry source could distort a metric.

## 7. Common mistakes

Comparing metrics with different definitions, hiding unresolved work, handing over without evidence or next steps, treating pending cases as closed, and optimizing alert counts instead of detection quality and business risk.
