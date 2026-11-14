# 07 — Data Models, CIM and Add-ons

## Objectives
Understand normalization, Common Information Model (CIM), and technology add-ons.

## 1. Why normalization?
Different vendors use different names and formats for similar activity. One firewall may use src_ip while another uses sourceAddress. Normalization maps source-specific fields into consistent concepts.

## 2. Splunk CIM
CIM defines common field names and data models for security and IT activity, including authentication, endpoint, network traffic, and web. Availability depends on version, add-ons, and correct mapping.

CIM does not automatically normalize every event. Data must be mapped and validated.

## 3. Technology add-ons
A technology add-on (TA) may provide field extractions, event types, tags, CIM mappings, inputs, and parsing configuration for a product. Use trusted sources and check compatibility and permissions.

## 4. Data models
A data model organizes events into datasets and fields. Acceleration may improve searches but consumes resources and requires correct configuration.

## 5. Validation
1. Confirm source ingestion.
2. Inspect raw events.
3. Verify expected fields.
4. Check tags and event types.
5. Confirm events appear in the intended data model.
6. Compare model results with raw-event searches.
7. Document gaps.

## Practical task
Map one sample authentication event's account, source, destination, action, and outcome into a common schema. Do not claim CIM compliance until mappings are tested.

## Knowledge check
1. What problem does CIM solve?
2. What is a TA?
3. Does installing an add-on prove all events are normalized?
4. Why compare model searches with raw events?

## References
- [Splunk CIM](https://docs.splunk.com/Documentation/CIM/latest/User/Overview)
- [Splunkbase](https://splunkbase.splunk.com/)
