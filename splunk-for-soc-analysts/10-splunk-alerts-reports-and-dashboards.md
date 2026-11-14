# 10 — Alerts, Reports and Dashboards

## Objectives
Design useful alerts and dashboards for SOC analysts.

## 1. Search and reporting concepts
- **Ad hoc search:** manually run to answer a question.
- **Saved search:** stored search definition.
- **Report:** saved search output, often scheduled.
- **Dashboard:** visual panels summarizing searches and metrics.
- **Alert:** condition that triggers a notification or action.

Availability and terminology vary by Splunk product and version.

## 2. Alert design
Include clear name, description, source, time window, detection logic, threshold, severity, confidence, impacted entities, evidence, suppression behavior, investigation steps, and owner.

## 3. False-positive reduction
Tune using a documented baseline. Exclusions should be narrow, justified, reviewed, and time-limited where practical. Do not suppress a noisy source without understanding its activity.

## 4. Dashboard ideas
- Alert volume by severity.
- Top affected hosts or accounts.
- Ingestion health and freshness.
- Detection coverage.
- Incident aging and response time.

Dashboards summarize; they do not replace raw-event investigation. Show time range, freshness, and metric definitions.

## 5. Responsible metrics
Alert count is not incident count. Lower alert volume may mean better tuning or broken ingestion. Pair security metrics with data-health metrics.

## Practical task
Design a four-panel dashboard: authentication failures, endpoint alerts, ingestion health, and open high-severity cases. Define purpose, source, time range, and limitations for each.

## Knowledge check
1. Alert versus report?
2. What is throttling for?
3. Why show data freshness?
4. Why can fewer alerts be misleading?

## References
- [Splunk alerting](https://docs.splunk.com/Documentation/Splunk/latest/Alert/Aboutalerts)
- [Splunk dashboards](https://docs.splunk.com/Documentation/Splunk/latest/Viz/Aboutdashboards)
