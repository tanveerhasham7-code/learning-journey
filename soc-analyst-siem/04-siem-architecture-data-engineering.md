# 04 — SIEM Architecture and Data Engineering

## What is a SIEM?
A Security Information and Event Management platform collects and analyzes security-relevant data from many sources. It supports search, correlation, alerting, dashboards, investigation, retention, and reporting. A SIEM is a tool—not a replacement for skilled analysts, good logging, incident processes, or endpoint/network controls.

## Typical data pipeline
1. **Source:** Endpoint, server, network appliance, identity provider, application, or cloud service.
2. **Collection:** Agent, forwarder, API integration, syslog, event subscription, or cloud connector.
3. **Transport:** Secure authenticated transfer with buffering and retry where supported.
4. **Parsing:** Extract fields from raw records.
5. **Normalization:** Map different vendor formats into a consistent schema.
6. **Enrichment:** Add asset criticality, user department, geolocation context, threat intelligence, or vulnerability context where lawful and useful.
7. **Storage/indexing:** Make data searchable under access and retention controls.
8. **Analytics:** Rules, correlation, statistics, and behavior analytics.
9. **Alert/case:** Route actionable findings to analyst workflows.
10. **Feedback:** Record outcomes and improve data, rules, and processes.

## Collection methods
- **Agent:** Installed on endpoints/servers; rich telemetry but requires lifecycle management.
- **Syslog:** Common message transport for network and Unix-like systems; consider secure transport and delivery.
- **API/webhooks:** Common for SaaS/cloud; manage permissions, rate limits, pagination, and API changes.
- **Windows event forwarding:** Centralized Windows event collection.
- **File collection:** Tails or forwards application log files.
- **Network sensors:** Collect metadata or packets; consider privacy, bandwidth, and storage.

## Parsing and normalization
Parsing extracts fields from raw input. Normalization maps vendor-specific names into a common schema. For example, client_ip, src, and sourceAddress may all represent source IP. Consistent schemas make cross-source queries and correlation easier.

Preserve raw records where policy allows. Keep parser version and source identity. Test parsing against normal, malformed, and edge-case events.

## Enrichment
Useful enrichment includes asset owner and criticality; identity department and privilege; vulnerability context; threat-intelligence reputation with source and freshness; and network context such as VPN ranges and internal subnets. Enrichment is context, not proof.

## Data models
Platforms may use vendor schemas or common models such as ECS or OCSF. Understand field types, event categories, datasets, and mapping quality. A field called user may represent an actor, target, or service account depending on the event. Validate semantics before writing detections.

## Storage, retention, and access
Plan storage around event volume, event size, retention, search frequency, and legal requirements. Use role-based access, encryption, secure backups, audit trails, and separation of duties. Restrict sensitive identity, HR, health, financial, and personal data. Retention follows policy and applicable law, not an arbitrary universal number.

## SIEM health monitoring
Monitor source heartbeat and last-seen time; events per second; parsing failures and unmapped fields; queue depth and dropped events; connector/API errors; storage capacity; retention; search and alert latency; rule execution failures; and agent coverage/version drift. A SIEM outage or ingestion gap is itself a security concern.

## Common implementation mistakes
Collecting everything without use cases or cost planning; onboarding sources without validating field quality; alerting on one weak indicator; ignoring time zones and duplicates; excessive analyst access; not monitoring ingestion; undocumented parser/rule changes; and retaining sensitive data longer than justified.

## Practical exercise
Design a pipeline for 50 fictional endpoints, 5 servers, one identity provider, firewall, DNS, and email platform. Draw source → collection → parsing → normalization → enrichment → storage → detection → case. Add failure points and monitoring for each stage.

## Knowledge check
1. Explain parsing versus normalization.
2. Why preserve raw event data?
3. What is enrichment, and why is it not proof?
4. Name five SIEM health metrics.
5. Why are retention and role-based access important?
