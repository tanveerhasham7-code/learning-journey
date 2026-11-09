# 11 — Security Monitoring and Logging

A log is a time-stamped record from an operating system, application, network device, or security tool. It may record authentication, process activity, configuration changes, network connections, and errors.

## Useful fields
Timestamp, hostname, account, source/destination address, event ID, process, action, result, and severity. Names and meanings differ by platform. Time synchronization is essential for timelines.

Telemetry is collected information about system behavior. An alert is a notification generated when a rule identifies activity that may need review. An alert is not automatically an incident or proof of malicious activity.

## SIEM
A Security Information and Event Management platform collects and normalizes events, supports search and correlation, and generates alerts and dashboards. Data quality, parsing, time settings, retention, access control, and tuning affect usefulness.

## Analyst workflow
Validate alert → identify assets/accounts → establish time window → gather related logs → compare with normal behavior → assess impact → document evidence → escalate or close under procedure.

## Practical
Inspect a harmless event in Windows Event Viewer or Linux system logs. Identify timestamp, source, and message. Explain what it records. Do not upload private logs or identifiers.
