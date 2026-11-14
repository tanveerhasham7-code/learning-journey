# 09 — Alerts, Incidents and Triage

## 1. Alert versus incident
An alert is a detection output describing a condition that matched rule logic. An incident is an investigation container that can group related alerts and entities. Grouping behavior depends on configuration.

## 2. Triage steps
1. Read alert title, description, severity and rule.
2. Inspect raw query results and timestamps.
3. Confirm source, account, host and IP fields.
4. Check whether entities were mapped correctly.
5. Review related alerts and incidents.
6. Establish normal business context.
7. Search related activity before and after the alert.
8. Decide whether to close, escalate or investigate further.
9. Record rationale and evidence.

## 3. Severity is not certainty
Severity estimates potential impact or urgency. It does not prove the event is malicious. A high-severity alert may be benign; a low-severity alert may be important when combined with other evidence.

## 4. Incident lifecycle
New → triage → investigation → containment/eradication/recovery as authorized → closure and lessons learned. Actual status labels and workflows can vary.

## 5. Useful incident fields
Incident number, title, severity, status, owner, created/updated times, alert links, entities, tactics, comments, tasks and closure classification.

## 6. Example
An alert reports multiple sign-in failures. Validate the user, source IP, device, authentication method, success/failure result, MFA context and whether a password reset or approved test explains the activity.

## 7. Practical task
Use a fictional incident record. Write a triage summary with known facts, unknowns, benign explanations, next queries, severity rationale and escalation decision.

## 8. Knowledge check
1. Difference between alert and incident?
2. Why is severity not proof?
3. What should a triage summary contain?
4. Why document closure rationale?