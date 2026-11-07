# 12 — Advanced SOC Operations, Metrics, and Automation

## SOC service management
A mature SOC needs documented service scope, coverage hours, escalation criteria, roles, customer responsibilities, and service-level objectives. Define what monitoring includes and excludes. Clarify who can isolate devices, disable identities, block traffic, or notify regulators/customers.

## Metrics that matter
- **MTTA:** Mean time to acknowledge an alert.
- **MTTD:** Mean time to detect an incident or suspicious behavior.
- **MTTR:** Ambiguous acronym often used for mean time to respond or recover; define the organization's meaning before comparing.
- **Dwell time:** Time an attacker remains in an environment before detection or containment, depending on the measurement definition.
- **Alert-to-case conversion:** Portion of alerts that become tracked cases.
- **False-positive rate:** Portion of alerts judged benign under a defined method.
- **Detection coverage:** Systems, behaviors, and use cases with functioning telemetry and detections.
- **Ingestion health:** Sources reporting correctly, latency, dropped events, and parsing quality.
- **Case aging/reopen rate:** Helps identify stalled investigations or weak closure quality.

Metrics can be gamed. Fast closure is not success if analysts miss incidents. Always pair speed with quality, risk, and customer outcomes.

## SOAR and automation
Security Orchestration, Automation, and Response (SOAR) connects tools and automates repeatable workflows. Appropriate examples include enrichment, deduplication, ticket creation, notification, and gathering approved context. High-impact actions such as disabling accounts or isolating production servers need strict authorization, testing, logging, and rollback procedures.

## Automation design principles
- Start with a stable, repetitive, low-risk task.
- Define trigger, inputs, outputs, and failure behavior.
- Use least-privilege service identities and secrets management.
- Validate and sanitize input.
- Add rate limits, retries, timeouts, and idempotency.
- Log actions and preserve an audit trail.
- Require human approval for disruptive actions.
- Test in a lab and provide rollback.
- Monitor automation failures and credential expiry.

## Scripting for analysts
Python and PowerShell can help parse CSV/JSON, summarize events, compare indicators, normalize timestamps, and generate reports. Avoid executing commands embedded in logs, handling secrets in plain text, or automatically deleting/quarantining files without an approved response design.

## Advanced topics
- UEBA: User and Entity Behavior Analytics; useful for identifying deviations, but baselines can be noisy.
- Detection-as-code: Version-controlled rules, peer review, automated tests, and release pipelines.
- Purple teaming: Collaborative validation of defensive controls and detections using authorized simulations.
- Threat-informed defense: Prioritizing controls and detections based on relevant adversary behavior.
- Detection debt: Accumulated gaps, stale rules, unowned alerts, and brittle logic.
- Resilience: Maintaining monitoring and response during platform outages or degraded telemetry.

## Governance and privacy
Minimize collection to legitimate purposes; restrict access; define retention; protect sensitive data; document cross-border transfers; and follow applicable law and organizational policy. Analysts should not inspect personal content without authorization and a valid purpose.

## Practical exercise
Design an automation that enriches an alert with asset owner, identity role, and recent related events, then opens a case for analyst review. Specify permissions, error handling, audit log, and the human approval boundary. Do not connect it to production services.

## Knowledge check
1. Why must MTTR be defined?
2. What is the risk of optimizing only alert closure speed?
3. Which SOAR actions should require approval?
4. What does idempotency mean in automation?
5. How does detection-as-code improve quality?
