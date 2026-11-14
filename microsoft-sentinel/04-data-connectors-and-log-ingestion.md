# 04 — Data Connectors and Log Ingestion

## 1. What is a data connector?
A data connector is an integration that brings telemetry from a source into Sentinel/Log Analytics. Examples include Microsoft Entra ID, Microsoft Defender services, Azure activity, Windows endpoints, selected network devices and third-party sources.

Connector availability, prerequisites and licensing vary.

## 2. Common source categories
- Identity: sign-in and audit activity.
- Endpoint: device and threat telemetry.
- Cloud: Azure resource and control-plane activity.
- Network: firewall, DNS, proxy and VPN events.
- Application: service-specific audit and activity.
- Third-party: supported APIs, agents, syslog or Common Event Format (CEF) routes.

## 3. Ingestion pipeline
1. Source generates an event.
2. Connector or collection mechanism retrieves/forwards it.
3. Data is authenticated and transported.
4. The workspace stores it in a destination table.
5. A query confirms arrival and field quality.
6. Detections and workbooks use the data.

A connector marked connected is not sufficient evidence that every expected event is arriving.

## 4. Connector validation
For each source document:
- Source and tenant/endpoint scope.
- Required permissions and configuration.
- Expected destination table(s).
- Expected event volume and latency.
- Required fields and timestamp semantics.
- Health/diagnostic signals.
- Retention and cost implications.

## 5. Windows data options
Windows telemetry may be collected through supported Azure Monitor Agent/Data Collection Rules, Microsoft Defender integrations or other supported mechanisms. The correct route depends on the event channel, OS, architecture and current Microsoft guidance. Do not assume every local EVTX channel is automatically ingested.

## 6. Common failures
Permission expiry, API throttling, agent offline, wrong workspace, data collection rule mismatch, firewall/DNS problems, unsupported source configuration, parsing changes or low event volume.

## 7. Practical task
Build a connector inventory table with source, owner, expected tables, required fields, validation query, health check and cost sensitivity. Do not connect real organizational logs without approval.

## 8. Knowledge check
1. What does a connector do?
2. Why query the destination table after setup?
3. Name four telemetry source categories.
4. What should be documented for each connector?