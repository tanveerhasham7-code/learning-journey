# 07 — Advanced KQL Hunting and Investigation

## 1. Goal
Advanced KQL helps analysts build timelines, summarize behavior, correlate data sources and investigate hypotheses. Always verify table schemas and query results.

## 2. Aggregation and time buckets

~~~kusto
SigninLogs
| where TimeGenerated > ago(7d)
| summarize Attempts = count() by bin(TimeGenerated, 1h), ResultType
| order by TimeGenerated desc
~~~

## 3. Distinct values and top entities

~~~kusto
SigninLogs
| where TimeGenerated > ago(24h)
| summarize Attempts = count() by UserPrincipalName, IPAddress
| top 20 by Attempts desc
~~~

## 4. Joins
Joins combine records from two datasets using a shared key. Confirm key quality and expected cardinality before using them.

~~~kusto
let recentSignins =
    SigninLogs
    | where TimeGenerated > ago(24h)
    | project UserPrincipalName, IPAddress, SigninTime = TimeGenerated;
let recentAudit =
    AuditLogs
    | where TimeGenerated > ago(24h)
    | project InitiatedBy, ActivityTime = TimeGenerated;
recentSignins
| join kind=inner (recentAudit)
    on $left.UserPrincipalName == $right.InitiatedBy
~~~

This is a conceptual example: InitiatedBy may be a dynamic object rather than a string, so extract and normalize the correct field for your schema before joining.

## 5. Let statements and reusable logic
Use `let` to define time ranges, watchlists, intermediate datasets and reusable calculations. Keep query scope narrow and avoid unnecessary scans.

## 6. Watchlists
Watchlists can provide reference data such as approved IP ranges, critical assets or service accounts. Maintain owners, expiry/review dates and data quality. A watchlist match is context, not automatic proof of malicious activity.

## 7. Hunting methodology
1. State a hypothesis.
2. Identify data sources and required fields.
3. Confirm telemetry coverage.
4. Define a time window.
5. Query and inspect representative records.
6. Compare with baseline and approved activity.
7. Pivot on user, device, IP or process.
8. Record limitations and evidence.

## 8. Performance and reliability
Filter early, project only required columns, use bounded time windows, avoid expensive broad text searches, inspect join behavior and validate time semantics. Query success does not guarantee correct logic.

## 9. Practical task
Write a hunt plan for repeated sign-in failures followed by a success. Identify the required fields, query stages, false positives and evidence you would preserve. Use sample data if no workspace exists.

## 10. Knowledge check
1. What is a join?
2. Why validate join keys?
3. What are watchlists useful for?
4. Why filter early?