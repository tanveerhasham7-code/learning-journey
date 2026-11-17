# Practical 10 — Incident Response Tabletop

**Status:** Assistant-prepared fictional tabletop; learner walkthrough pending  
**Date prepared:** 2026-11-17  
**Scenario type:** Simulated suspicious account activity at a fictional small company

## 1. Objective

Practice the basic incident-response process: prepare, identify, analyze, contain, eradicate, recover, and learn. Build a timeline, identify evidence, propose safe containment, and record uncertainty without treating assumptions as facts.

## 2. Fictional incident scenario

A fictional employee reports an unexpected sign-in notification for their company email account. Shortly afterward, the employee notices an unfamiliar email in the Sent folder. The employee does not recognize the activity.

**All names, times, events, and details in this scenario are invented for training.** No real account or system was accessed.

## 3. Incident timeline

| Time (fictional) | Event | Analyst interpretation |
|---|---|---|
| 09:02 | Employee receives an unexpected sign-in alert | Possible account access; verify through the official service, not links in the alert |
| 09:05 | Employee reports an unfamiliar sent message | Potential account misuse; preserve the message and relevant metadata |
| 09:10 | Help desk opens an incident record | Establishes a record and response owner |
| 09:15 | Security team checks identity-provider sign-in records | Correlate timestamps, device, location, and authentication details |
| 09:25 | Team revokes active sessions and temporarily blocks sign-in if compromise is reasonably suspected | Containment limits continued access; follow approved procedures |
| 09:40 | Password reset and MFA review completed through a trusted device/channel | Helps regain control; verify recovery methods and MFA registrations |
| 10:00 | Mailbox rules, forwarding settings, sent items, and connected applications reviewed | Look for persistence or unauthorized changes |
| 10:30 | Account owner confirms expected access and business services are restored | Recovery check; continue monitoring |

This timeline is a model sequence, not a record of a real incident.

## 4. Evidence collection plan

Collect only information needed for the investigation and preserve it according to organizational policy.

- Identity-provider sign-in events around the reported time.
- Authentication method, MFA prompts, and any newly registered factors.
- Message headers and metadata for the unfamiliar sent email.
- Mailbox forwarding rules, inbox rules, and delegate permissions.
- Recent password, recovery-information, and session changes.
- Relevant endpoint security alerts, if available.
- Incident ticket, reporter's description, and actions taken with timestamps.

**Privacy:** redact usernames, email addresses, tokens, session IDs, IP addresses where disclosure is not necessary, and any personal or confidential message content before public sharing. Preserve original evidence securely for authorized investigators.

## 5. Containment proposal

1. Contact the employee through a trusted channel to confirm the report.
2. Notify the designated security/IT incident-response owner.
3. If account compromise is reasonably suspected, revoke active sessions and temporarily block sign-in using approved administrative controls.
4. Reset credentials from a trusted device and review MFA methods and recovery options.
5. Remove unauthorized mailbox rules, forwarding, delegates, or connected application grants only after recording them as evidence and following policy.
6. If the same password may have been reused, advise the user to change it on other affected services.
7. Preserve relevant logs and message evidence; do not delete suspicious messages before evidence handling is complete.

Containment actions should be proportionate and authorized. Avoid destructive actions or broad account shutdowns without considering business impact and incident policy.

## 6. Eradication and recovery

- Remove confirmed unauthorized mailbox rules, forwarding, delegates, or application access.
- Ensure the account has a unique strong password and appropriate MFA.
- Verify recovery email/phone details and registered authentication methods.
- Check other affected accounts if credential reuse is suspected.
- Restore normal access only after the response owner confirms the account is secured.
- Monitor sign-in and mailbox activity for further suspicious behavior.

## 7. Communication

- Tell the employee what is known, what actions are being taken, and how to report further alerts.
- Keep management and relevant stakeholders updated according to incident policy.
- Escalate potential exposure of customer, regulated, or confidential information through the organization's required process.
- Do not speculate about attacker identity or claim data theft without supporting evidence.

## 8. Uncertainty and questions

| Question | Current status in scenario | What would help answer it? |
|---|---|---|
| Was the account actually compromised? | Suspected, not proven | Correlated sign-in and authentication evidence |
| Who performed the sign-in? | Unknown | Identity-provider records and authorized investigation |
| Was information accessed or copied? | Unknown | Available audit records and service-specific evidence |
| Was the unfamiliar message sent by the account owner? | Not confirmed | Message metadata and confirmation from the employee |
| Are other accounts affected? | Unknown | Review related alerts and possible credential reuse |

A sign-in alert alone does not prove compromise. A suspicious sent message increases concern but still requires verification.

## 9. Lessons learned and preventive controls

- Require MFA, preferably phishing-resistant MFA where supported.
- Use conditional access and risk-based sign-in monitoring where available.
- Alert on unusual sign-ins, suspicious mailbox rules, and unexpected forwarding.
- Train employees to report unexpected authentication prompts and suspicious messages.
- Maintain a documented incident-response contact path and session-revocation procedure.
- Review access permissions and connected applications regularly.
- Test the incident-response plan with tabletop exercises.

## 10. Model conclusion

The correct initial response is to treat the report seriously, preserve evidence, verify the activity through trusted administrative records, and contain suspected account access using authorized procedures. The team should distinguish confirmed facts from assumptions and document every action with a timestamp.

## Completion note

This is an **assistant-prepared reference simulation**. The timeline, evidence, and event details are fictional; no live investigation, account access, containment, or recovery action was performed. The learner's own tabletop walkthrough and reflection remain pending, so this practical is not marked learner-completed.
