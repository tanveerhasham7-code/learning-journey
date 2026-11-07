# 11 — Network Monitoring, Logs, SNMP and Flow Data

## 1. Why monitoring?
Prevention is never perfect. Monitoring helps detect outages, misconfiguration and suspicious behavior. A useful monitoring system answers: what happened, when, where, who/what was involved and what evidence supports the conclusion?

## 2. Telemetry types
- **Syslog:** event messages from routers, switches, firewalls, servers and applications.
- **SNMP:** polling or receiving device status and counters. Prefer SNMPv3 with authentication and privacy.
- **NetFlow/IPFIX/sFlow:** summarized flow or sampling data describing communication metadata, not normally full packet payload.
- **Packet capture:** packet-level detail at a specific observation point.
- **Device/API telemetry:** vendor-specific health, configuration and security events.

## 3. Useful network signals
Monitor interface status/errors, bandwidth utilization, CPU/memory, route changes, VPN sessions, firewall denies, DNS patterns, DHCP leases, wireless associations, authentication failures and configuration changes.

## 4. Time synchronization
All devices should use approved time sources. Record timezone and clock offset. Without consistent time, a SIEM may order events incorrectly and make it difficult to connect a DNS query, firewall session and endpoint alert.

## 5. Baselines and alert quality
A baseline describes normal behavior by asset, user, service and time. Alert on meaningful deviations, such as a workstation contacting a new administrative service or a server sending unexpected outbound traffic. Tune alerts to reduce noise and record the reason for every threshold.

## 6. SIEM correlation example
A possible investigation chain:
1. DHCP log maps an IP address to a device during a lease period.
2. DNS log shows the device resolving an unusual domain.
3. Firewall/flow data shows an outbound connection shortly afterward.
4. Endpoint telemetry shows a process responsible for the connection.
5. Analyst validates the user, host and business context.

No single log line proves malware. Preserve evidence and document uncertainty.

## 7. Protect the monitoring system
Restrict access, use MFA, protect log transport, set retention rules, monitor collector health, back up configurations and ensure logs cannot be casually altered by ordinary users.

## Practical lab
Generate a small set of synthetic syslog lines or use logs from your own VM. Parse timestamps, source device, severity and message. Build a simple table of event counts and write three observations. Do not upload real sensitive logs.

## SOC analyst questions
- Is this behavior new for this asset?
- Is the source IP correctly mapped to a device at that time?
- Is the destination expected?
- Which protocol/port was used?
- Is the activity blocked or successful?
- What endpoint process initiated it?
- What additional evidence is needed?
