# 04 — Indexes, Events and Field Extraction

## Objectives
Understand event structure, indexes, fields, timestamps, and normalization.

## 1. Event structure
An event is a searchable record created from incoming data. It may include timestamp, raw text, metadata, and extracted fields. JSON sources may be structured; plain-text sources may need parsing.

## 2. Indexes
An index is a logical location for stored events. Organizations may separate data by source, environment, sensitivity, or retention. Design indexes around access control, governance, retention, and operational simplicity.

## 3. Fields
Fields are named values extracted from events, such as user, src, dest, action, or EventCode. Names are not universal; inspect your own events before writing detections.

## 4. Field extraction
Splunk can extract fields from supported formats or configured knowledge objects. Extraction may use delimiters, regular expressions, JSON parsing, or add-ons. Poor extraction can cause false negatives and false positives.

## 5. Time handling
Distinguish source event timestamp, indexed time, and display timezone. Check timezone and clock synchronization before building timelines.

## 6. Normalization
Different products may use different names for the same concept. Normalization maps source-specific fields into consistent names. Splunk CIM provides common field conventions and data models, but correct mapping must be configured and validated.

## Practical task
Inspect five sample events. Record timestamp, host, source, sourcetype, index, and available fields. Identify one field that could be normalized across sources.

## Knowledge check
1. What is an index?
2. How is a field different from raw text?
3. Why does timestamp parsing matter?
4. What problem does normalization solve?

## References
- [Fields and field extraction](https://docs.splunk.com/Documentation/Splunk/latest/Knowledge/Aboutfields)
- [Splunk CIM](https://docs.splunk.com/Documentation/CIM/latest/User/Overview)
