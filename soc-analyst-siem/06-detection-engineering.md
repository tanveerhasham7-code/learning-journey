# 06 — Detection Engineering

## What is detection engineering?
Detection engineering is the disciplined process of converting threat knowledge and operational requirements into reliable analytics. A good detection is understandable, testable, scoped, monitored, and linked to an investigation action. More alerts do not automatically mean better security.

## Detection lifecycle
1. Identify a threat scenario and business risk.
2. Define observable behavior and required telemetry.
3. Write a detection hypothesis and logic.
4. Build a query/rule with clear time windows and thresholds.
5. Test against representative benign and simulated malicious data.
6. Measure true positives, false positives, and missed cases.
7. Tune exceptions carefully without hiding real activity.
8. Deploy through change control and version control.
9. Monitor rule health and review performance.
10. Retire or redesign detections when no longer useful.

## Detection types
- **IOC-based:** Match known hashes, domains, IPs, or other indicators. Fast but can become stale and may miss new infrastructure.
- **Behavior-based:** Detect actions such as unusual process chains or account changes.
- **Threshold-based:** Detect volume, rate, or repeated behavior.
- **Correlation-based:** Combine events across time or sources.
- **Anomaly-based:** Identify deviation from a baseline; requires careful tuning and context.
- **Sequence-based:** Detect ordered behaviors, such as failures followed by a successful sign-in and privileged action.

## Detection quality
Consider precision, recall, false-positive rate, time to detect, data coverage, rule stability, and analyst workload. A rule with many alerts may be poor if most are benign. A quiet rule may be broken or missing telemetry. Always check both detection outcomes and data pipeline health.

## Threshold design
A threshold should reflect expected behavior, user population, asset role, and time period. Avoid universal values such as “five failures always means attack.” Consider per-account and per-source rates, successful authentication after failures, MFA outcome, known scanners, service accounts, and business hours. Use baselines and test against real benign patterns.

## Exceptions and allowlists
Exceptions should be narrow, justified, owned, time-limited where possible, and reviewed. Prefer exact identities, hosts, applications, or signed management workflows over broad network ranges or generic process names. Record why an exception exists and who approved it.

## Detection rule documentation
Every rule should include:
- Name, ID, owner, version, and status.
- Threat scenario and business risk.
- Data sources, required fields, and prerequisites.
- Query logic and schedule.
- Severity, confidence, and routing.
- False-positive guidance and exclusions.
- Investigation steps and response boundaries.
- Test cases and known limitations.
- Change history and retirement criteria.

## Testing
Test positive examples, benign lookalikes, boundary conditions, missing fields, duplicate events, timezone differences, and ingestion delays. Use synthetic logs and approved simulation frameworks in isolated labs. Never execute live malware or attack techniques on production systems for a learning exercise.

## Practical exercise
Create a detection specification for a new privileged account created outside an approved change window. Include data sources, actor/target fields, business-hours context, expected benign cases, test records, severity rationale, and analyst steps. Use the template in templates/detection-rule-template.md.

## Knowledge check
1. Compare IOC and behavior detections.
2. Why is an allowlist dangerous if too broad?
3. What is the difference between precision and recall?
4. Name five test cases for a detection.
5. Why does every rule need an owner and review date?
