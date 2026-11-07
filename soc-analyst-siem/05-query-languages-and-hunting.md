# 05 — Query Languages and Threat Hunting

## Why queries matter
SOC analysts search large event collections to answer focused questions: Which accounts failed authentication? What process launched a script interpreter? Which hosts contacted a domain? Queries should be reproducible, scoped, time-bounded, and based on known field semantics.

## Query design workflow
1. State the question and hypothesis.
2. Select the relevant data source and time range.
3. Identify the fields needed to test the hypothesis.
4. Start with a narrow filter, then broaden carefully.
5. Group or summarize to reveal patterns.
6. Pivot from one event to related host, user, process, or network activity.
7. Save the query with purpose, assumptions, and limitations.

## Core query operations
- Filter: retain records matching conditions.
- Projection: display only useful fields.
- Search: find text or values.
- Aggregation: count, sum, average, minimum, maximum.
- Grouping: summarize by user, host, source IP, or event type.
- Sorting: order by timestamp or count.
- Time binning: compare event frequency over intervals.
- Join/correlation: connect records using a stable key.
- Deduplication: remove duplicate records when appropriate.

## Example pseudo-query patterns
These are conceptual patterns, not guaranteed syntax for every SIEM.

**Failed sign-ins by account**
    SELECT user, COUNT(*) AS failures
    FROM authentication_events
    WHERE result = 'failure' AND timestamp >= now_minus_1_hour
    GROUP BY user
    ORDER BY failures DESC

**New administrative group membership**
    SELECT timestamp, actor, target_user, group_name, host
    FROM identity_audit
    WHERE action = 'member_added'
      AND group_name IN ('Administrators', 'Domain Admins')
    ORDER BY timestamp DESC

**Rare outbound destinations**
    SELECT host, destination_domain, COUNT(*) AS connections
    FROM network_events
    WHERE direction = 'outbound'
    GROUP BY host, destination_domain
    ORDER BY connections ASC

Validate field names and syntax in your own platform. The pseudo-query examples explain logic only.

## KQL-style concepts
In Microsoft Sentinel/Defender environments, Kusto Query Language commonly uses a table followed by operators such as where, project, summarize, extend, join, and order by. Learn the actual table and column names in the workspace; schemas differ by connector.

Example shape:
    SigninLogs
    | where TimeGenerated > ago(1d)
    | where ResultType != "0"
    | summarize Failures=count() by UserPrincipalName, IPAddress
    | order by Failures desc

Treat this as a starting pattern and verify the schema and meaning of ResultType for your data.

## Splunk SPL-style concepts
Common SPL operations include search, table, stats, timechart, eval, sort, dedup, and transaction. Example shape:
    index=security sourcetype=authentication action=failure
    | stats count by user, src
    | sort - count

Field names, index names, and exact behavior depend on deployment.

## Elastic KQL / ES|QL concepts
Elastic environments may support Kibana Query Language for filtering and ES|QL for structured processing. Learn the difference between filtering syntax and a full query pipeline. ECS field names are common but must be validated against the installed integrations.

## Hunting versus alert triage
Triage begins with an alert. Threat hunting begins with a hypothesis or question and searches for evidence that may not have triggered an alert. Hunting is not random searching; it is structured and evidence-driven.

## Hunt hypothesis template
- Question/hypothesis:
- Why it matters:
- ATT&CK behavior (if applicable):
- Data sources required:
- Query and time window:
- Expected normal behavior:
- Suspicious result:
- Findings and confidence:
- Gaps/limitations:
- Detection opportunity:

## Practical exercise
Use a synthetic CSV containing timestamp, user, host, source_ip, action, result, and application. Calculate failures by user and source, identify a success after repeated failures, and explain why the pattern needs context before calling it password spraying.

## Knowledge check
1. Why should every query have a time range?
2. What is the difference between filtering and aggregation?
3. How does hunting differ from alert triage?
4. Why can joins create misleading results?
5. What must be documented with a saved query?
