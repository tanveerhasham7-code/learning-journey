# 13 — SOC Investigation and Incident Response

## 1. Investigation objective
Determine what happened, when it happened, which identities/assets were involved, how far it spread, what evidence supports the conclusion and which response actions are authorized.

## 2. Investigation lifecycle
1. Validate the alert and source query.
2. Confirm entities and timestamps.
3. Establish a timeline.
4. Pivot across identity, endpoint, cloud and network sources.
5. Identify scope and potential impact.
6. Preserve relevant evidence.
7. Assess confidence and alternative explanations.
8. Escalate and recommend response.
9. Execute approved actions through the responsible team.
10. Close with findings and lessons learned.

## 3. Evidence quality
Record source table, query, time range, workspace context, record identifiers where available, collection time and analyst interpretation. Preserve original records according to organizational policy.

## 4. Response phases
- **Preparation:** roles, access, playbooks and logging.
- **Detection and analysis:** validate and scope.
- **Containment:** limit impact under approved authority.
- **Eradication:** remove root cause.
- **Recovery:** restore trusted operation.
- **Post-incident:** document, review and improve detections.

## 5. Case report template

~~~markdown
# Sentinel Incident Report
Incident reference:
Date/time and timezone:
Analyst:
Summary:
Severity and rationale:
Affected accounts/assets:
Timeline:
Queries and source tables:
Evidence references:
Findings:
Alternative explanations:
Scope and impact:
Actions and approvals:
Assessment: Benign / Suspicious / Confirmed / Inconclusive
Recommendations:
Limitations and lessons learned:
~~~

## 6. Practical task
Use a synthetic identity incident. Create a timeline, list confirmed facts and unknowns, identify three follow-up queries and write a response recommendation that does not exceed your authority.

## 7. Knowledge check
1. Why preserve query details?
2. What belongs in an incident timeline?
3. Why separate recommendation from approved action?
4. What should a post-incident review improve?