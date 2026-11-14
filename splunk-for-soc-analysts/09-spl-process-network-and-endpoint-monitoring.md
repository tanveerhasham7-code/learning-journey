# 09 — Process, Network and Endpoint Monitoring

## Objectives
Use endpoint and network telemetry to investigate suspicious activity.

## 1. Process telemetry
Useful fields include process name, command line, parent process, user, process ID, hash, and timestamp. Sysmon Event ID 1 records process creation when configured. Windows process-creation auditing can also provide telemetry with different detail.

## 2. Network telemetry
Network events may include source/destination IP, port, protocol, action, and bytes. A connection alone does not prove malicious activity. Compare it with asset role, destination context, expected application behavior, and other evidence.

## 3. Endpoint protection
Endpoint products may report detections, blocked actions, quarantine, policy changes, or sensor health. Confirm whether an event means detected, blocked, quarantined, or remediated.

## 4. SPL patterns
    index=endpoint
    | stats count by host user process_name
    | sort - count

    index=network
    | stats count by src dest dest_port action
    | sort - count

These require matching fields in your data.

## 5. Correlation
A stronger investigation may combine authentication, process execution, network connection, endpoint alert, and asset context. Validate entity fields and clock synchronization before correlating.

## 6. Telemetry gaps
Missing command lines, incomplete Sysmon configuration, disabled audit policies, NAT, time drift, or disconnected agents can weaken an investigation. A missing event does not prove that activity did not happen.

## Practical task
Build a field matrix for investigating a suspicious process followed by an outbound connection. Identify the log source for each field and how you would correlate records.

## Knowledge check
1. What is process parentage?
2. Why is a network connection not proof of compromise?
3. Name two endpoint telemetry sources.
4. Why check time synchronization?

## References
- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [Splunk Security Content](https://research.splunk.com/)
