# 14 — Capstone: Design and Operate a Mini-SOC

## Scenario
You are a junior analyst for a fictional company, Northstar Services. It has 25 Windows endpoints, 3 Linux servers, cloud email, a central identity provider, a firewall, DNS resolver, and a small customer portal. Your assignment is to design a basic monitoring capability and investigate a simulated account-compromise scenario.

All data in this capstone must be synthetic or collected from systems you own and are authorized to monitor.

## Phase 1 — Scope and assets
Create an asset inventory with owner, business purpose, criticality, operating system, identity type, data sensitivity, and logging capability. Identify the highest-risk assets and why.

## Phase 2 — Logging plan
Choose telemetry for endpoints, identity, email, firewall, DNS, Linux, and cloud control plane. For each source document collection method, key fields, retention requirement, access restriction, and failure monitoring.

## Phase 3 — SIEM pipeline
Draw source → collector → parser → normalized schema → enrichment → storage → detection → case workflow. Define source health checks and alerting for missing telemetry.

## Phase 4 — Detection content
Write at least five detection specifications:
1. Repeated authentication failures followed by success.
2. Unexpected privileged group membership change.
3. Suspicious mailbox forwarding rule.
4. Unusual script interpreter/process chain.
5. Endpoint contacting a rare or known-bad domain.

For each: threat hypothesis, required data, query logic, threshold rationale, false positives, test cases, severity, confidence, and analyst runbook.

## Phase 5 — Simulated investigation
Use synthetic events describing:
- A suspicious email received by a fictional employee.
- A sign-in from an unusual device.
- A new mailbox forwarding rule.
- A privileged action or unusual data access.
- An endpoint network connection that may be related.

Build a timeline, correlate evidence, identify affected entities, distinguish facts from hypotheses, and state what evidence is missing.

## Phase 6 — Response plan
Recommend containment options and identify who must approve them. Include account session revocation, password reset, device isolation, email rule removal, and log preservation as possible actions, but do not perform real actions. Explain business impact and rollback considerations.

## Phase 7 — Final report
Deliver:
- Executive summary.
- Scope and affected assets/accounts.
- Timeline with timezone.
- Evidence table and source references.
- Findings, confidence, and limitations.
- ATT&CK behavior mapping where justified.
- Containment/recovery recommendations.
- Lessons learned and detection improvements.

## Phase 8 — Portfolio presentation
Publish a sanitized README with architecture diagram, synthetic dataset description, detection specifications, example queries, screenshots of your own lab, report, and lessons learned. Clearly label simulated work. Never upload real credentials or private telemetry.

## Assessment rubric
- SOC workflow and scope: 10%
- Logging and SIEM design: 20%
- Detection quality and testing: 20%
- Investigation and evidence: 25%
- Response plan and communication: 15%
- Documentation, safety, and limitations: 10%

A strong capstone is not measured by the number of alerts. It is measured by reproducibility, evidence quality, sensible decisions, and clear communication.
