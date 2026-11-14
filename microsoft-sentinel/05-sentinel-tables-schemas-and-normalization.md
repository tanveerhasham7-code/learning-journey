# 05 — Sentinel Tables, Schemas and Data Normalization

## 1. Tables and records
Log Analytics stores data in tables. Each row is a record and each column represents a field. Different connectors may send similar activity into different tables or schemas.

## 2. Common table examples
Depending on enabled products and collection design, analysts may encounter:
- SigninLogs
- AuditLogs
- SecurityEvent
- Syslog
- AzureActivity
- CommonSecurityLog
- DeviceProcessEvents (Defender XDR integration scenarios)
- Heartbeat

Availability is environment-dependent. Check the workspace's actual Tables list and current product documentation.

## 3. Schema awareness
Before writing a query, inspect:
- Table name.
- Available columns and data types.
- Timestamp columns.
- Host, user, source and destination fields.
- Dynamic JSON fields.
- Normalized fields and connector-specific variations.

Do not assume two products use identical field names.

## 4. ASIM and normalization
The Advanced Security Information Model (ASIM) provides normalization schemas and parsers for supported security data types. Normalization can help analysts write more consistent queries across sources, but parser support and coverage must be validated.

## 5. Basic discovery queries

~~~kusto
// List recent records in a table
SecurityEvent
| take 10

// Inspect recent sign-in records
SigninLogs
| take 10

// Count records by table is not a universal cross-table query;
// query the specific tables available in your workspace.
~~~

If a table does not exist, first check connector setup and workspace table availability rather than assuming a query syntax error.

## 6. Data quality checks
Look for null fields, inconsistent hostnames, unexpected timezones, duplicate records, ingestion delays, schema drift and missing source coverage.

## 7. Practical task
Choose one available table or use sample query data. Record five column names, data types, timestamp field, source and one limitation. Redact identities and IP addresses in public evidence.

## 8. Knowledge check
1. What is a table?
2. Why inspect schema before writing a query?
3. What problem does normalization address?
4. Does an absent table always mean KQL is wrong?