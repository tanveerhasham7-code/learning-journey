# 01 — SOC Foundations and Operating Model

## What is a SOC?
A Security Operations Center (SOC) is a people, process, and technology function that monitors an organization's systems, identifies suspicious activity, investigates security events, coordinates response, and reduces cyber risk. A SOC is not simply a room with screens. Its value comes from reliable telemetry, useful detections, trained analysts, documented procedures, and timely communication.

**Security event:** An observable occurrence such as a login, process start, firewall connection, or file change.  
**Alert:** A notification created when a rule or analytic identifies activity that may need review.  
**Incident:** A confirmed or credible security event requiring coordinated response under policy.  
**Case:** The tracked record containing alert context, evidence, decisions, actions, and communications.

An alert is not automatically an incident. One failed login may be normal; repeated failures followed by a successful login from an unusual source may deserve investigation.

## Why organizations need a SOC
- Detect attacks that preventive controls did not stop.
- Identify compromised accounts, endpoints, servers, applications, and cloud resources.
- Reduce time between suspicious activity and containment.
- Preserve evidence and support reporting duties.
- Find gaps in logging, identity security, endpoint protection, and network controls.
- Learn from incidents and improve prevention and detection.

## SOC operating models
- **In-house:** Organization employs analysts and operates its tools.
- **MSSP/MDR:** A provider monitors or responds under a defined contract.
- **Hybrid:** Internal team owns risk and response while a provider supplies monitoring or specialist support.
- **Follow-the-sun:** Teams in different time zones provide continuous coverage through handovers.
- **Virtual/distributed:** Analysts work remotely with centralized processes.

Every model needs clear ownership, escalation paths, service levels, data-access rules, and customer communication.

## Common SOC roles
- **Tier 1 / Monitoring analyst:** Validate alerts, enrich context, close known benign activity, and escalate suspicious cases.
- **Tier 2 / Incident analyst:** Perform deeper host, identity, network, and application investigation; determine scope; recommend containment.
- **Tier 3 / Senior analyst or hunter:** Investigate complex threats, develop hypotheses, hunt, and guide major incidents.
- **Detection engineer:** Build, test, deploy, document, and tune analytics.
- **SIEM engineer:** Manage ingestion, parsing, normalization, storage, access, availability, and performance.
- **Incident responder / DFIR:** Coordinate containment, evidence preservation, eradication, and recovery.
- **SOC manager:** Own staffing, priorities, quality, metrics, stakeholder reporting, and improvement.

Titles differ between organizations; not every SOC uses exactly three tiers.

## SOC workflow
1. **Collect:** Endpoint, identity, network, application, email, and cloud telemetry.
2. **Process:** Parse fields, normalize timestamps, enrich, and route records.
3. **Detect:** Apply correlation rules, analytics, intelligence, and behavior models.
4. **Triage:** Determine whether an alert is relevant, expected, duplicate, or suspicious.
5. **Investigate:** Build a timeline, identify affected assets/accounts, and test hypotheses.
6. **Respond:** Coordinate approved containment and recovery actions.
7. **Document:** Record evidence, decisions, timestamps, impact, and communication.
8. **Improve:** Tune detections, close telemetry gaps, and update playbooks.

## Severity, priority, and confidence
- **Severity** describes potential technical impact.
- **Priority** describes how quickly the organization should act, considering impact, exposure, and business context.
- **Confidence** describes how strongly evidence supports a detection or conclusion.

A high-severity alert may be low priority on a known test asset; a medium-severity alert may become urgent on a critical identity. Use the organization's approved matrix.

## Essential skills
Technical: operating systems, networking, authentication, logs, query languages, endpoint tools, SIEM, scripting, and cloud basics.  
Analytical: timeline building, hypothesis testing, correlation, gap identification, and separating evidence from assumptions.  
Professional: concise writing, calm escalation, confidentiality, teamwork, curiosity, and accurate handovers.

## Example: suspicious sign-in
A detection reports many failed sign-ins followed by success. Check account role, normal pattern, source IP, device, application, authentication method, MFA result, and conditional-access outcome. Look for password resets, MFA changes, mailbox rules, token activity, and endpoint alerts. Determine affected resources, escalate or close with reasons, and preserve supporting evidence.

## Practical task
Create a one-page SOC workflow for a fictional company. Include alert intake, triage, escalation, incident commander, IT operations, legal/privacy contact, and closure. Mark actions that require approval.

## Knowledge check
1. Differentiate event, alert, incident, and case.
2. Why is an alert not proof of compromise?
3. What should Tier 1 include when escalating?
4. How do severity, priority, and confidence differ?
5. Why are handovers and documentation security controls?
