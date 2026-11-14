# 12 — Splunk Enterprise Security, Correlation Searches and Risk-Based Alerting

## Objectives
Understand Splunk Enterprise Security (ES), correlation searches, notable events, and risk-based alerting (RBA).

## 1. Splunk ES
Splunk Enterprise Security is a security operations solution built on Splunk. It adds security-focused workflows such as correlation searches, investigations, risk analysis, and security dashboards. It is separately licensed; verify current packaging and availability.

## 2. Correlation searches
A correlation search evaluates data against detection logic and may create a notable event or trigger another configured action. It should be tested, scheduled appropriately, and tuned.

## 3. Notable events
A notable event is a security finding in ES workflows. Analysts assess severity, urgency, entities, evidence, and related activity. A notable event is not automatically a confirmed incident.

## 4. Risk-based alerting
RBA can accumulate risk observations around entities. Several low-confidence signals may combine into a higher-confidence reason to investigate.

Conceptual example:
- unusual authentication failures add risk;
- privileged logon from an uncommon host adds risk;
- suspicious process execution adds more risk;
- a documented entity-risk threshold prompts analyst review.

This is a learning example, not a tested rule.

## 5. Detection governance
Record owner, purpose, data dependencies, schedule, severity, suppression, exceptions, version, test evidence, and review date.

## Practical task
Write a detection specification for unusual failures followed by successful logon. Include required fields, query logic, threshold rationale, false positives, severity, and response steps. Do not call it a tested ES correlation search unless you have ES and have validated it.

## Knowledge check
1. What is Splunk ES?
2. What is a correlation search?
3. How does RBA differ from separate alerts for every signal?
4. Why check licensing?

## References
- [Splunk ES documentation](https://docs.splunk.com/Documentation/ES)
- [Splunk Security Content](https://research.splunk.com/)
