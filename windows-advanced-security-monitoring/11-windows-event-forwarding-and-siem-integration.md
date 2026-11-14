# 11 — Windows Event Forwarding and SIEM Integration

## 1. Why centralize?
Local logs can roll over, be deleted or become unavailable when a device is offline. Central collection supports cross-endpoint searches, correlation and retention.

## 2. Windows Event Forwarding
WEF forwards selected events from source computers to a Windows Event Collector (WEC). Subscriptions define which events are collected and from which sources.

~~~text
Windows source endpoints
        | subscription
        v
Windows Event Collector
        |
        v
Forwarded Events channel
        |
        v
SIEM / analyst workflow
~~~

WEF is not itself a SIEM. It collects and forwards selected Windows events; a SIEM provides broader search, correlation, alerting and case workflows.

## 3. Subscription models
- **Source-initiated:** endpoints identify a collector subscription.
- **Collector-initiated:** collector manages which sources it queries.

Choose based on network design, scale and administration. Secure WinRM, authentication, firewall scope and permissions.

## 4. SIEM agent integration
A SIEM agent may collect local channels and send them to a manager. Define channels, filters, parsing, retention and health checks. Product-specific configuration must be validated against its documentation.

## 5. Validation checklist
1. Confirm source and collector versions.
2. Verify services and network reachability.
3. Confirm subscription or agent configuration.
4. Generate a harmless test event.
5. Verify it on the collector.
6. Verify SIEM arrival with host and timestamp.
7. Compare counts and identify gaps.
8. Document permissions and retention.

## 6. Common problems
WinRM/firewall blocks forwarding, filters omit events, sources are not subscribed, collector capacity or permissions are incorrect, agent is unhealthy, or time differences disrupt correlation.

## 7. Practical task
Draw a WEF or SIEM collection architecture. If available, forward one harmless event and record source, collector and SIEM evidence. Otherwise mark implementation pending.

## 8. Knowledge check
1. Difference between WEF and SIEM?
2. What is a subscription?
3. Why validate each stage?
4. What controls protect the collector?