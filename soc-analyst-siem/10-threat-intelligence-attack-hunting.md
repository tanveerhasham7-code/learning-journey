# 10 — Threat Intelligence, MITRE ATT&CK, and Threat Hunting

## Threat intelligence
Threat intelligence is analyzed information about threats, actors, infrastructure, capabilities, and intent that supports decisions. Intelligence should be relevant, sourced, timely, and actionable. A raw feed of indicators is not automatically intelligence.

### Intelligence types
- **Strategic:** Long-term trends and business risk for leaders.
- **Operational:** Campaigns, likely targets, and adversary activity.
- **Tactical:** TTPs and behaviors used by adversaries.
- **Technical:** IOCs such as hashes, IPs, domains, and file paths.

### Indicator handling
For each indicator record source, first/last seen, confidence, context, expiry, and action taken. Check for shared hosting, cloud infrastructure, CDN use, false positives, and indicator age. Do not block a broad IP range solely because one feed labels an address suspicious.

## MITRE ATT&CK use
Map observed behaviors to tactics and techniques only when evidence supports the mapping. Use ATT&CK to identify data sources, build hunts, communicate behavior, and evaluate defensive coverage. ATT&CK is not a checklist that guarantees detection, and technique mapping is not attribution.

## Threat hunting
Threat hunting is a proactive, hypothesis-driven search for suspicious behavior that may have escaped existing detections.

### Hunt process
1. Choose a threat hypothesis based on risk, intelligence, incidents, or gaps.
2. Identify expected attacker behavior and plausible benign explanations.
3. Identify required data and validate coverage.
4. Write and scope queries.
5. Examine anomalies and pivot across sources.
6. Record findings, confidence, and limitations.
7. Create or improve a detection when justified.
8. Share results and schedule follow-up.

### Hunt examples
- Rare use of remote administration tools on user workstations.
- New privileged group membership followed by unusual access.
- Endpoints contacting rare domains shortly after script execution.
- Service accounts authenticating interactively.
- Unusual cloud storage reads by an identity that rarely accesses data.
- Mailbox forwarding changes after a suspicious sign-in.

## Hypothesis quality
A good hypothesis is specific enough to test, tied to a meaningful risk, and supported by available telemetry. Avoid vague hunts such as “find hackers.” Define what normal behavior looks like and what evidence would disprove the hypothesis.

## Practical exercise
Choose one hunt above. Define the hypothesis, data sources, query logic, expected benign activity, suspicious findings, gaps, and a detection improvement. Use synthetic or authorized data only.

## Knowledge check
1. Compare strategic and technical intelligence.
2. Why record indicator age and source?
3. How does threat hunting differ from incident response?
4. Why is ATT&CK mapping not attribution?
5. What makes a hunt hypothesis testable?
