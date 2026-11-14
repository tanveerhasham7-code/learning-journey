# Identity Threat Monitoring and Account Compromise

## 1. Why identity telemetry matters

Attackers often target user accounts, service accounts, administrators and authentication systems. Identity monitoring helps analysts detect account takeover, credential abuse, privilege misuse and suspicious authentication patterns.

## 2. Important identity signals

- Repeated failed logons followed by a success
- Logins from unusual locations, devices or network paths
- Impossible-travel or atypical session patterns (signals requiring validation)
- MFA fatigue or repeated push requests
- MFA method registration, reset or removal
- Password reset followed by unusual access
- New device or token activity
- Privileged group membership changes
- New accounts, disabled accounts re-enabled, or unusual service-account use
- Legacy or unusual authentication protocols
- Access to sensitive applications outside normal patterns

## 3. Windows identity events to recognize

Common Windows Security event IDs include:
- **4624:** Successful logon
- **4625:** Failed logon
- **4634:** Logoff
- **4648:** Logon using explicit credentials
- **4672:** Special privileges assigned to a new logon
- **4720:** User account created
- **4728 / 4732 / 4756:** Member added to a security-enabled group (global / local / universal)
- **4726:** User account deleted
- **4740:** User account locked out
- **4768 / 4769:** Kerberos ticket-granting ticket / service ticket activity
- **4771:** Kerberos pre-authentication failed
- **4776:** NTLM credential validation

Event meaning and availability depend on audit policy, Windows version and log source. Validate fields and context rather than relying on event ID alone.

## 4. Investigation workflow

1. Identify the user, account type, affected systems and alert time.
2. Review authentication result, logon type, source device/IP, destination and authentication method.
3. Compare activity with the user's baseline and expected working pattern.
4. Correlate endpoint, VPN, cloud identity, MFA and directory audit logs.
5. Check password/MFA changes, group membership, new devices and token/session activity.
6. Determine whether the activity is expected, suspicious, confirmed malicious or inconclusive.
7. Escalate suspected compromise or privileged identity activity according to policy.
8. Recommend approved response steps; do not reset passwords, revoke sessions or disable accounts without authorization.
9. Record the timeline, evidence, scope and confidence.

## 5. Distinguishing benign from suspicious

A user may travel, use a VPN, change devices or mistype a password. Validate with approved context and user verification processes. Do not label a person or location malicious based on a single anomaly.

## 6. Practical exercises

- Build a timeline from synthetic 4624, 4625 and 4740 events.
- Investigate a fictional sequence of failed logons followed by a successful logon.
- Review a synthetic privileged-group membership change.
- Write a case note explaining what is known, unknown and required for escalation.

## 7. Common mistakes

Treating every failed logon as an attack, ignoring logon type, confusing account lockout with compromise, overlooking service accounts, and performing identity containment without authority.
