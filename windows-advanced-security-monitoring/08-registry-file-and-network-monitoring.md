# 08 — Registry, File and Network Activity Monitoring

## 1. Why monitor these areas?
Applications routinely change files, registry values and network connections. These records can also reveal suspicious execution, configuration changes, persistence attempts or unexpected communication.

## 2. Registry monitoring
Sysmon Events 12, 13 and 14 can record registry object creation/deletion, value setting and key/value rename activity. Coverage depends on configuration.

Analysts may review autorun-related locations, service configuration and security settings. Normal installers, updates and policy refreshes also modify the registry.

## 3. File monitoring
Sysmon Event 11 records file creation when included by configuration. Review full path, creating process, user, timestamp, hash if collected, expected software behavior and related events.

## 4. Network monitoring
Sysmon Event 3 can record network connections when enabled. Event 22 can provide DNS query information. Firewall and EDR telemetry may add context.

Review process/user, source and destination addresses, ports, protocol, DNS context, host role and expected application behavior.

## 5. Example investigation chain
A new executable appears in a user-writable directory. Identify the creating process, check whether it connected to a network, inspect related registry changes and determine whether it executed. Each link requires evidence.

## 6. Collection and tuning
Enable only categories needed for defined use cases, baseline known-good software, review dropped events and volume, preserve configuration and test field availability in the SIEM.

## 7. Practical task
Review one benign file or network event. Identify process, user, path/destination and timestamp. Write two legitimate explanations and one question to ask before escalation.

## 8. Knowledge check
1. Which Sysmon events monitor registry activity?
2. Why is process attribution valuable for network events?
3. Why are broad file rules noisy?
4. What should be recorded for a registry detection?