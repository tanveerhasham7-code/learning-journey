# SOC investigation workflow and response


Use a repeatable workflow. Do not jump from one event to a conclusion.

### 12.1 Alert triage

1. **Validate the alert:** Check event source, timestamp, fields and collection health.
2. **Identify the identity:** Determine whether the account is a user, service, computer or administrator account.
3. **Identify the asset:** Establish the source and destination systems and their business importance.
4. **Build a timeline:** Correlate logons, failures, account changes, group changes and process activity.
5. **Compare with baseline:** Is the behavior normal for this identity, device and role?
6. **Check authorization:** Look for an approved change, maintenance window or support ticket.
7. **Assess scope:** Search for related accounts, hosts and similar events.
8. **Determine impact:** Establish what access may have been gained or what data/systems may be affected.
9. **Escalate or close:** Record evidence and rationale.

### 12.2 Evidence handling

Record:

- Case ID and analyst.
- Alert ID and detection name.
- Event IDs and original event records.
- UTC timestamp and original timezone.
- Account identifiers and relevant group memberships.
- Hostnames and source addresses.
- Relevant SIEM queries and time ranges.
- Hashes of exported evidence where appropriate.
- Actions taken, approvals and communications.

Keep original evidence unchanged. Work from copies, restrict access and follow the organization's retention and privacy policies. Sanitize usernames, domains, IPs and hostnames before publishing portfolio examples.

### 12.3 Response options

Depending on evidence, authority and incident policy, responders may:

- Disable or temporarily restrict a compromised account.
- Revoke sessions or reset credentials using the approved identity process.
- Remove unauthorized group membership.
- Isolate an affected endpoint through approved EDR procedures.
- Block a malicious source when justified.
- Preserve relevant logs and forensic evidence.
- Review other identities and systems for related activity.
- Restore policy or configuration from a known-good state.

Do not perform containment actions on production systems without the required authorization. A SOC analyst should follow escalation and approval procedures.

### 12.4 Case closure

A good closure note states:

- What happened.
- Which identities and assets were involved.
- What evidence supports the conclusion.
- Whether activity was authorized, suspicious or confirmed malicious.
- What containment or remediation occurred.
- What remains uncertain.
- What detection or control improvement is recommended.

---
