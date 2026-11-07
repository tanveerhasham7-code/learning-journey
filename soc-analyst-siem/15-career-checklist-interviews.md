# 15 — Career Checklist and Interview Preparation

## Beginner readiness
- Explain SOC, SIEM, EDR, XDR, SOAR, event, alert, incident, and case.
- Understand TCP/IP, DNS, HTTP/S, VPN, firewall, and common ports.
- Navigate Windows Event Viewer and Linux logs.
- Explain authentication, MFA, least privilege, and account lifecycle.
- Read a basic alert and identify affected user/host/time.

## Junior SOC analyst readiness
- Query authentication, endpoint, DNS, firewall, and email data.
- Build a timeline from multiple sources.
- Explain false positives and confidence.
- Investigate a process tree and suspicious sign-in.
- Write an escalation note and incident report.
- Explain common ATT&CK tactics and techniques.
- Identify telemetry gaps and SIEM ingestion failures.

## Intermediate readiness
- Write and test detection rules.
- Tune thresholds and document exceptions.
- Perform a hypothesis-driven threat hunt.
- Correlate identity, endpoint, network, email, and cloud events.
- Understand evidence preservation and response approval.
- Explain SIEM normalization, retention, and access control.
- Automate low-risk enrichment tasks safely.

## Advanced readiness
- Design detection-as-code workflow.
- Measure detection coverage and quality.
- Review SOAR permissions and failure modes.
- Lead complex investigations and handovers.
- Build threat-informed hunting plans.
- Communicate business impact to technical and nontechnical stakeholders.
- Improve SOC process based on metrics and post-incident reviews.

## Interview questions to practise
1. What is the difference between a security event, alert, and incident?
2. How would you investigate repeated failed logins?
3. What evidence would you collect after a suspicious PowerShell alert?
4. How do you determine whether an IP address is malicious?
5. Explain SIEM parsing and normalization.
6. What would you do if a critical log source stopped sending events?
7. How do you reduce false positives without creating blind spots?
8. What is the difference between EDR, XDR, SIEM, and SOAR?
9. How would you investigate a suspicious mailbox forwarding rule?
10. What should an incident escalation contain?
11. How do you use MITRE ATT&CK responsibly?
12. What is the difference between threat hunting and alert triage?
13. How do you preserve evidence?
14. Which SOC metrics are useful, and how can they be misleading?
15. Describe a detection you would design for unexpected privileged access.

## How to answer scenario questions
Use a structured response: clarify the alert and scope; validate telemetry; identify entities; build a timeline; correlate sources; consider benign explanations; state facts and unknowns; recommend approved actions; document and escalate. Do not claim certainty without evidence.

## Portfolio checklist
- [ ] SOC workflow diagram.
- [ ] Log-source inventory.
- [ ] Synthetic event dataset and schema.
- [ ] SIEM query examples with field assumptions.
- [ ] At least five documented detections.
- [ ] Positive and benign test cases.
- [ ] Sanitized investigation timeline.
- [ ] Incident report and lessons learned.
- [ ] Capstone architecture and clear lab limitations.

## Important career note
Course completion is not equivalent to professional experience. Be honest about which tools you used, what you configured yourself, what was simulated, and what you learned. A clear, reproducible beginner project is stronger than an exaggerated claim.
