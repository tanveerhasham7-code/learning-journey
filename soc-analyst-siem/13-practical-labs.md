# 13 — Practical SOC and SIEM Labs

Complete labs in order. Use synthetic records or an isolated lab you own. Each lab should produce a short report with objective, environment, steps, observations, evidence, limitations, and lessons learned.

## Lab 1 — SOC alert triage worksheet
Create a fictional alert and fill out alert source, time, affected entity, severity, confidence, evidence, benign explanations, decision, and escalation path.

## Lab 2 — Build a log-source inventory
Document Windows, Linux, identity, firewall, DNS, email, and cloud sources. Record owner, collection, key fields, sensitivity, retention, and gaps.

## Lab 3 — Read Windows security events
On your own Windows lab, inspect available logon and account-management events. Record audit policy and event source. Do not assume all event categories are enabled by default.

## Lab 4 — Linux authentication review
On your own Linux VM, review SSH and sudo authentication records. Identify successful and failed logins and explain limitations of the available logs.

## Lab 5 — Normalize a synthetic dataset
Create a CSV with different vendor-style field names and map them into common fields such as timestamp, user, source IP, action, and result. Preserve original columns.

## Lab 6 — Authentication pattern analysis
Use synthetic sign-in data to group failures by user and source, then identify successes after repeated failures. Explain why shared NAT, VPN, and user error can produce similar patterns.

## Lab 7 — Process tree investigation
Use a synthetic process dataset to reconstruct parent-child relationships. Identify unusual chains and list benign alternatives. Do not run suspicious commands.

## Lab 8 — DNS investigation
Analyze synthetic DNS records for rare domains, high query volume, and repeated NXDOMAIN responses. Consider update services, internal zones, and typos as benign explanations.

## Lab 9 — Firewall and network timeline
Correlate firewall allow/deny events with endpoint process records and DNS answers. Explain what metadata cannot prove without packet or endpoint evidence.

## Lab 10 — Phishing investigation
Create a fictional email header summary, URL click event, identity sign-in, and mailbox audit event. Determine what is confirmed and what remains unknown. Never open a real suspicious attachment.

## Lab 11 — Privilege-change detection
Write a detection specification for an unexpected privileged group membership change. Include actor, target, group, time context, exceptions, and investigation steps.

## Lab 12 — SIEM ingestion health
Design checks for last-seen time, ingestion latency, event volume, parser failures, queue depth, and source coverage. Create synthetic examples of a healthy and unhealthy source.

## Lab 13 — Threat hunt
Choose a hypothesis such as service accounts authenticating interactively. Define data, query, expected normal behavior, suspicious results, and limitations.

## Lab 14 — Incident timeline and report
Build a timeline from synthetic endpoint, identity, DNS, and firewall events. Complete the incident report template.

## Lab 15 — Detection test cases
For one detection, create positive, benign lookalike, missing-field, duplicate-event, boundary-threshold, and delayed-ingestion test cases.

## Lab 16 — Mini-SOC dashboard plan
Sketch a dashboard for ingestion health, open cases, severity, case aging, detection coverage, and recurring false positives. Explain who uses each panel and what decision it supports.

## Evidence requirements
Use sanitized screenshots or synthetic data only. Remove account names, public IPs tied to personal activity, internal hostnames, email addresses, tokens, cookies, keys, and private business data. Label generated events as synthetic. Do not claim a simulation proves a real compromise.

## Lab report
Use templates/incident-report-template.md for investigations and templates/lab-evidence-guide.md for evidence handling.
