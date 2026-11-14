# 12 — Windows Detection Engineering

## 1. Definition
Detection engineering turns a threat hypothesis into testable logic, validates telemetry, measures false positives and maintains detections over time.

## 2. Lifecycle
1. Define behavior and business risk.
2. Write a clear hypothesis.
3. Identify required event sources and fields.
4. Confirm telemetry is enabled and collected.
5. Create an initial search or rule.
6. Test with safe activity or synthetic records.
7. Measure false positives and missed cases.
8. Tune for host role, account and expected software.
9. Document response guidance and limitations.
10. Version, review and retest.

## 3. Example hypotheses
- Privileged account signs in from an unusual endpoint.
- Process starts from an unexpected writable directory.
- PowerShell activity is inconsistent with user role.
- New task or service appears outside an approved change.
- Security logging or protection is unexpectedly altered.
- Process creates a file and then makes an unusual network connection.

## 4. Detection specification example

~~~yaml
detection_id: WIN-EXAMPLE-001
name: Unusual process execution
status: experimental
hypothesis: A process launched from an unusual path may require review.
data_sources:
  - Sysmon Event ID 1
required_fields:
  - Computer
  - Image
  - CommandLine
  - ParentImage
  - User
logic_summary: Compare process paths and parent-child relationships
  with an approved baseline for the endpoint role.
false_positives:
  - Approved software deployment
  - Administrative scripts
limitations:
  - Requires Sysmon process telemetry
response:
  - Validate user, host, parent process and business context
~~~

This is a documentation example, not a ready-to-deploy rule.

## 5. Correlation
Specify join keys, time windows, missing-field behavior and duplicate handling. Avoid PID-only correlation because PIDs can be reused; use stronger identifiers where available.

## 6. Sigma concepts
Sigma is a generic format for log-based detections. A rule defines metadata, log source, selections and conditions. Conversion is needed for a SIEM backend. Validate field mappings and test converted queries; valid syntax can still contain incorrect logic.

## 7. Quality measures
Telemetry coverage, freshness, true/false-positive review, alert volume, analyst effort, test coverage and documented limitations.

## 8. Practical task
Write one detection specification with hypothesis, sources, required fields, benign explanations, investigation steps and a safe test plan. Do not call it validated until results are saved.

## 9. Knowledge check
1. What makes a hypothesis testable?
2. Why validate telemetry before tuning?
3. Define false positive.
4. Why test Sigma after conversion?