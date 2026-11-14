# 08 — Analytics Rules and Detection Engineering

## 1. Purpose
Analytics rules evaluate workspace data to identify behavior that may require investigation. Rule types, scheduling, query periods, grouping and incident creation options vary by current Sentinel capabilities.

## 2. Detection lifecycle
1. Define a threat hypothesis and business impact.
2. Identify telemetry source and required fields.
3. Validate ingestion and data quality.
4. Write and test KQL.
5. Measure normal activity and false positives.
6. Configure rule frequency and lookback period.
7. Map entities and set alert details.
8. Decide how alerts create or group incidents.
9. Test safely and document expected behavior.
10. Review performance and tune continuously.

## 3. Rule concepts
- **Query:** logic that selects suspicious records.
- **Schedule/frequency:** how often a scheduled rule runs.
- **Lookup period:** how far back the query examines data.
- **Threshold:** count or condition required to create an alert.
- **Entity mapping:** associates records with accounts, hosts, IPs and other entities.
- **Alert details:** title, description, severity and tactics.
- **Incident grouping:** combines related alerts into an analyst case.

## 4. Example hypothesis
Repeated authentication failures for one account, followed by a success from a source that differs from the normal pattern, may deserve review.

A basic query can identify failure volume, but a production detection needs correct result codes, baseline context, source fields, threshold testing, duplicate control and false-positive analysis.

## 5. Detection documentation

~~~yaml
detection_id: SENTINEL-IDENTITY-001
name: Unusual authentication failure pattern
status: experimental
hypothesis: Repeated failures followed by a success may indicate
  password guessing or an account issue requiring review.
data_source:
  - SigninLogs
required_fields:
  - TimeGenerated
  - UserPrincipalName
  - IPAddress
  - ResultType
logic_summary: Aggregate failures by account and source in a defined
  window, then investigate subsequent success and context.
false_positives:
  - Mistyped password
  - Expired credentials
  - Approved identity testing
limitations:
  - Requires complete sign-in telemetry and schema validation
response:
  - Review account, IP, device, risk context and related sign-ins
~~~

## 6. Rule quality
Track alert volume, precision, false-positive reasons, time-to-triage, telemetry coverage, query performance and missed scenarios. Version-control query text and change notes.

## 7. Practical task
Write a detection specification and test query against sample data. Do not publish it as enabled or validated unless you actually deploy and test it.

## 8. Knowledge check
1. Why validate telemetry before writing rules?
2. What is entity mapping?
3. Why does lookback period matter?
4. What evidence supports a detection being validated?