# 11 — Workbooks, Dashboards and Reporting

## 1. What is a workbook?
A Microsoft Sentinel workbook is an interactive reporting and visualization surface that can use workspace data and parameters. It helps SOC teams understand trends, coverage and operational activity.

## 2. Common workbook uses
- Sign-in failures and authentication trends.
- Incident volume by severity and status.
- Alert trends over time.
- Endpoint or cloud asset coverage.
- Data connector health and ingestion patterns.
- Threat hunting summaries.

## 3. Workbook design
1. Identify the audience and decision.
2. Select reliable tables and fields.
3. Define time range and filters.
4. Write and validate KQL.
5. Choose visualizations that answer a question.
6. Add clear titles, units and context.
7. Explain missing data and limitations.
8. Test access and refresh behavior.

## 4. Metrics
Examples include alert volume, incident backlog, mean time to acknowledge (MTTA), mean time to respond (MTTR), ingestion delay and data-source coverage. Define formulas consistently; do not compare teams using different definitions.

## 5. Practical task
Design a one-page SOC dashboard on paper or with sample data: incident trend, severity distribution, top alert categories and data-source health. State what each visualization helps an analyst decide.

## 6. Knowledge check
1. What is a workbook?
2. Why define the audience first?
3. What makes a metric misleading?
4. Why disclose missing telemetry?