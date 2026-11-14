# Detection engineering for Active Directory


A useful detection is more than an event ID. It has a clear hypothesis, data requirements, logic, exclusions, severity, triage steps and a test plan.

### 11.1 Detection lifecycle

1. Define the threat behavior and business risk.
2. Identify the telemetry needed.
3. Confirm that logging is enabled and fields are populated.
4. Write a detection hypothesis.
5. Implement a query or correlation rule in the chosen SIEM.
6. Test with safe, authorized simulation or synthetic events.
7. Review false positives and tune thresholds.
8. Document investigation steps and response guidance.
9. Version-control the rule and review it periodically.

### 11.2 Example detection hypothesis: privileged group membership change

**Hypothesis:** A user is added to a highly privileged group outside an approved administrative change.

**Telemetry:** Windows Security events for group membership changes, especially 4728, 4732 and related events appropriate to the group type; include the actor, member, group, domain controller and timestamp.

**Logic outline:**

- Identify membership-addition events for a maintained list of sensitive groups.
- Enrich the actor and member with account and asset context.
- Check approved change windows or tickets.
- Raise severity when the actor is unexpected, the member is a normal user, or the event occurs outside approved activity.

**Triage questions:**

- Which account made the change?
- Which account was added?
- Which group was modified?
- Was the change approved?
- Did the actor recently authenticate from an unusual device?
- What did the new member do after the change?

### 11.3 Example detection hypothesis: repeated failures followed by success

**Hypothesis:** A sequence of failures followed by a successful authentication may indicate password guessing or a user entering an incorrect password and then succeeding.

**Telemetry:** 4625 and 4624, plus source address, target account, target host, logon type and timestamps.

**Logic outline:**

- Group failures by account and source over a defined time window.
- Identify a subsequent success for the same account or relevant source.
- Suppress known noisy systems only when there is a documented reason.
- Increase priority if the account is privileged or the source is unusual.

**Caution:** A fixed threshold should be based on local baseline and business context. A single universal threshold is rarely suitable for every organization.

### 11.4 Example detection hypothesis: suspicious account creation

**Hypothesis:** A new user account is created by an unexpected actor or outside the normal provisioning workflow.

**Telemetry:** Event 4720 and nearby events such as account enablement, password reset, group membership changes and first logon.

**Triage:** Identify creator, new account, timestamp, domain controller, initial group memberships, approval record and first authentication activity.

### 11.5 Detection quality checklist

- Does the rule detect a meaningful behavior rather than a noisy single event?
- Are the required audit policies enabled?
- Are event fields normalized consistently?
- Is there a clear severity rationale?
- Are legitimate admin workflows documented?
- Can the analyst explain why an alert fired?
- Does the runbook say what evidence to collect?
- Has the rule been tested with benign and suspicious examples?
- Is the detection version-controlled?

---
