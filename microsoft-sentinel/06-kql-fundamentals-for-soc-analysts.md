# 06 — KQL Fundamentals for SOC Analysts

## 1. What is KQL?
Kusto Query Language (KQL) is used to explore and analyze data in Azure Monitor Logs and related Microsoft services. It is a read-oriented query language for filtering, projecting, summarizing and correlating telemetry.

## 2. Query pipeline
KQL commonly uses the pipe character `|`. Each operator receives the previous operator's result.

~~~kusto
SecurityEvent
| where TimeGenerated > ago(24h)
| take 20
~~~

## 3. Essential operators

~~~kusto
// Select rows
SecurityEvent
| where EventID == 4625

// Select columns
SecurityEvent
| project TimeGenerated, Computer, Account, EventID

// Sort newest first
SecurityEvent
| order by TimeGenerated desc

// Count records
SecurityEvent
| summarize TotalEvents = count()

// Group counts
SecurityEvent
| summarize EventCount = count() by EventID
| order by EventCount desc

// Search text in selected data
SecurityEvent
| where tostring(EventData) has "failed"
~~~

Column names and types differ by table. Adapt examples to the actual schema.

## 4. Time filtering
Use explicit time windows to reduce cost and focus analysis.

~~~kusto
SigninLogs
| where TimeGenerated between (ago(24h) .. now())
| take 50
~~~

TimeGenerated usually represents event/record time in the table, but understand source semantics and ingestion delay.

## 5. String operators
- `==`: exact equality.
- `!=`: not equal.
- `has`: term-based matching.
- `contains`: substring matching.
- `startswith` / `endswith`: prefix/suffix checks.
- `in`: match against a set.

Choose operators based on the data and performance requirements.

## 6. Nulls and types
Use `isnull()`, `isnotnull()`, `tostring()`, `toint()` and other conversion functions carefully. Converting malformed data may produce nulls; validate results.

## 7. Practical exercises
1. Retrieve 20 recent records from an available table.
2. Filter a 24-hour time window.
3. Project timestamp, host and account fields.
4. Count records by event type.
5. Explain one null or missing field.

## 8. Knowledge check
1. What does the pipe operator do?
2. Difference between project and where?
3. Why specify a time range?
4. Difference between has and contains?