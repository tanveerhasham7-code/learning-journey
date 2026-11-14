# 13 — Windows SOC Investigation and Response

## 1. Objective
A Windows alert is a starting point. Determine whether activity is expected, suspicious, confirmed malicious or inconclusive, and support the assessment with evidence.

## 2. Triage workflow
1. Read alert name, severity, logic and triggering event.
2. Confirm host, user, timestamp and data source.
3. Check telemetry completeness and parsing.
4. Identify asset role and criticality.
5. Search related process, authentication, PowerShell, registry, file and network events.
6. Compare with baseline and approved changes.
7. Scope related accounts, devices and time.
8. Preserve evidence.
9. Escalate or recommend containment under policy.
10. Document findings and unresolved questions.

## 3. Build a timeline
Include timestamp/timezone, host/channel, provider/event ID, actor and target, process/parent/command line, file or registry object, network destination and analyst interpretation.

Use UTC or explicitly record timezone. Do not mix local and UTC without conversion.

## 4. Evidence handling
Preserve original exports where policy permits, record collection time and source, hash evidence when appropriate, analyze working copies, maintain chain-of-custody notes for formal cases and sanitize portfolio material.

## 5. Response decisions
Actions may include escalation, account disablement, credential reset, endpoint isolation or indicator blocking. These can disrupt business. Do not take them without authority, policy and impact review.

## 6. Case report
- Case ID and alert.
- Summary and severity rationale.
- Affected user and assets.
- Timeline.
- Evidence and queries.
- Findings and confidence.
- Scope and impact.
- Actions and approvals.
- Recommendations.
- Limitations and lessons learned.

## 7. Practical task
Use synthetic scenario data or harmless lab events. Build a five-event timeline, identify known and unknown facts, propose three next questions and write a short conclusion.

## 8. Knowledge check
1. Why is an alert not a final conclusion?
2. What belongs in a timeline?
3. Why must containment be authorized?
4. How preserve evidence integrity?