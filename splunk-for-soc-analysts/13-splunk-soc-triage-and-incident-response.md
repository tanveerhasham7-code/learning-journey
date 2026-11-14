# 13 — SOC Triage and Incident Response with Splunk

## Objectives
Triage alerts, scope activity, preserve evidence, and communicate findings.

## 1. Alert triage
1. Read the detection description and trigger condition.
2. Validate source, time range, and raw events.
3. Identify account, host, source, destination, and process.
4. Inspect surrounding activity.
5. Search for related alerts and prior events.
6. Check asset criticality and business context.
7. Close as benign, investigate further, or escalate according to policy.

## 2. Scoping
Determine whether one account or host is affected or whether related systems show similar behavior. Do not assume a shared IP or username proves the same actor.

## 3. Evidence handling
Record query, time range, timezone, event references, evidence location, analyst, and collection time. Sanitize sensitive data before publishing. Follow organizational retention and chain-of-custody rules.

## 4. Incident response
Common phases include preparation, detection and analysis, containment, eradication, recovery, and lessons learned. Follow the organization's plan. Splunk provides visibility; it does not authorize account disabling, endpoint isolation, or production changes.

## 5. Case report
Include case ID, summary, detection, severity, affected entities, timeline, exact searches, evidence, analysis, confidence, scope, authorized actions, recommendations, and closure reason.

## Practical task
Use synthetic events from the companion lab to complete a triage worksheet and short incident report. Clearly label sample data as synthetic.

## Knowledge check
1. What must be checked before trusting an alert?
2. Why is scoping important?
3. What makes a search reproducible?
4. Why must containment follow authorization?

## References
- [NIST Incident Handling Guide](https://csrc.nist.gov/pubs/sp/800/61/r2/final)
- [Splunk documentation](https://docs.splunk.com/)
