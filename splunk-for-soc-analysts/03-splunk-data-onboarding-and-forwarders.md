# 03 — Data Onboarding and Forwarders

## Objectives
Understand ingestion, Universal Forwarder, metadata, and basic troubleshooting.

## 1. Data onboarding
Data onboarding selects a source, collects events, transports them, parses them, and makes them searchable. Start with a security question: what activity must the SOC investigate? Collect only data with a clear purpose.

## 2. Universal Forwarder
The UF is a lightweight agent that reads configured files or supported event sources and forwards data to Splunk. It is not the indexer or analyst interface.

Key configuration concepts:
- **Inputs:** which data to collect.
- **Outputs:** where to send it.
- **Receiver:** Splunk endpoint accepting forwarded data.
- **Deployment management:** distributing configuration in larger environments.

Use version-specific documentation for exact file paths and syntax.

## 3. Metadata
- **host:** system that generated the event.
- **source:** file, channel, or input where it came from.
- **sourcetype:** classification describing event format.
- **index:** logical storage location.
- **time:** source event time and indexed/ingestion time are not always identical.

## 4. Useful sources
Windows Security, System, Application, Defender, PowerShell, and Sysmon logs; Linux authentication and system logs; firewall, DNS, and network-device events. Collection depends on configuration and authorization.

## 5. Validate ingestion
1. Search the intended index.
2. Confirm events are recent.
3. Check host, source, sourcetype, and timestamp.
4. Compare event counts with the source where possible.
5. Inspect field extraction.
6. Record missing data and limitations.

## Troubleshooting
No events: check input, permissions, service, connectivity, receiver. Wrong time: check source clock, timezone, timestamp parsing. Wrong sourcetype: inspect input assignment and parsing. Duplicates: check for overlapping inputs.

## Practical task
Create a Windows Security log onboarding worksheet with channel, purpose, expected event families, index, sourcetype plan, privacy notes, and validation method.

## Knowledge check
1. What does a UF do?
2. Explain host, source, sourcetype, and index.
3. Why validate ingestion?
4. Name three causes of missing events.

## References
- [Universal Forwarder](https://docs.splunk.com/Documentation/Forwarder/latest/Forwarder/Abouttheuniversalforwarder)
- [Monitor Windows data](https://docs.splunk.com/Documentation/Splunk/latest/Data/MonitorWindowsdata)
