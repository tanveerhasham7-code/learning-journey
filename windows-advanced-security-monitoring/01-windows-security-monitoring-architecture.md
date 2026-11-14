# 01 — Windows Security Monitoring Architecture

## 1. Meaning
Windows security monitoring is the collection and review of operating-system activity to identify suspicious behavior, policy violations, failures and possible compromise. A SOC analyst uses telemetry to establish what happened, which account or process was involved, which device was affected and what requires investigation.

Monitoring is not collecting every event. It means collecting useful records, protecting them, retaining context and building detections that can be investigated.

## 2. Main telemetry sources
- **Security log:** authentication, account management, privilege use and audited security activity.
- **System log:** services, drivers and operating-system components.
- **Application log:** application-generated events.
- **PowerShell logs:** script and module activity when configured.
- **Sysmon:** detailed process, network, file and registry telemetry.
- **Microsoft Defender:** detections, remediation and protection health.
- **Windows Firewall:** permitted or blocked traffic when logging is configured.
- **Task Scheduler and service records:** useful for execution and persistence investigations.

## 3. Event flow
1. A user, process or service performs an action.
2. Windows or an installed provider records an event when configured.
3. The event is written to a local channel.
4. An agent or Windows Event Forwarding may collect it.
5. A SIEM parses, stores and indexes it.
6. A detection identifies a condition for review.
7. An analyst validates, investigates and documents the alert.

~~~text
User / Process / Service
          |
          v
 Windows event providers
          |
          v
 Security | System | PowerShell | Sysmon | Defender
          |
          v
 Local Event Logs
          |
     Agent / WEF
          |
          v
         SIEM
          |
       Detection
          |
          v
 SOC triage -> investigation -> report
~~~

## 4. Important terms
- **Provider:** component that writes events.
- **Channel:** named event-log destination.
- **Event ID:** identifier for an event type within a provider.
- **Event record:** one recorded occurrence with timestamp and event data.
- **Collector:** component that gathers events.
- **Parser/decoder:** extracts fields from records.
- **Detection rule:** logic that identifies activity for review.
- **Retention:** how long records remain available.

## 5. Why context matters
An event ID alone rarely proves malicious activity. Review provider, host, account, process, parent process, command line, source address, timestamp, outcome and surrounding events. The same event can be normal on one host and suspicious on another.

## 6. Design principles
- Collect telemetry for defined detection or investigation needs.
- Enable auditing deliberately and measure event volume.
- Centralize important records.
- Synchronize clocks and document timezone assumptions.
- Restrict access and define retention.
- Test collection after configuration changes.
- Document blind spots and false positives.

## 7. SOC example
An alert reports unusual PowerShell. Do not assume it is malicious. Review user, host role, parent process, command line, script-block records if enabled, network activity and approved administrative context.

## 8. Knowledge check
1. Why is an event ID insufficient by itself?
2. Difference between provider and channel?
3. Why centralize important logs?
4. Name four Windows telemetry sources.