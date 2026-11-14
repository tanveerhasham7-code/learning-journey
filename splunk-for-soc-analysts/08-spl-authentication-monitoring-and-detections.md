# 08 — Authentication Monitoring and Detection Use Cases

## Objectives
Identify authentication telemetry and build detection hypotheses.

## 1. Useful Windows events
- **4624:** successful logon.
- **4625:** failed logon.
- **4648:** logon using explicit credentials.
- **4672:** special privileges assigned to a new logon.
- **4768 / 4769 / 4771:** Kerberos-related authentication events on domain controllers.
- **4776:** NTLM credential validation.

Confirm meanings and context with Microsoft documentation and the role of the source host.

## 2. Failed logon baseline
    index=windows EventCode=4625
    | stats count by user src host
    | sort - count

This summarizes failures. It does not prove password guessing.

## 3. Detection hypotheses
- One source generates unusually many failures.
- One source targets many accounts.
- A successful logon follows a burst of failures.
- A privileged logon occurs from an unusual host or time.

Investigate count, time window, account, source, destination, expected service behavior, lockouts, and successful logons.

## 4. False positives
User typing errors, VPN gateways, shared NAT, scheduled tasks, service accounts, and application retries may create repeated failures. Establish a baseline and tune thresholds.

## 5. Detection specification
Document name, purpose, data sources, required fields, query, schedule, threshold rationale, severity, confidence, false positives, response steps, owner, and tuning history.

## Practical task
Use authorized or synthetic events to count failed logons by user and source. Record likely false positives and one extra signal that could improve confidence.

## Knowledge check
1. What does event 4625 mean?
2. Why is a high failure count not proof of brute force?
3. Which fields help group authentication activity?
4. What should a detection specification contain?

## Reference
- [Microsoft logon auditing events](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events)
