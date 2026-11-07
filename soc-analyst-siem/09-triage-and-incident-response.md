# 09 — SOC Triage and Incident Response

## Alert triage
Triage is the first structured assessment of an alert. The goal is to decide whether it is expected, a false positive, suspicious, or an incident requiring escalation—not to close alerts as quickly as possible.

### Triage checklist
1. Read the alert name, rule logic, severity, confidence, and time window.
2. Confirm the data source is healthy and fields are parsed correctly.
3. Identify the affected asset, account, user, application, and business owner.
4. Check asset criticality and whether the activity was approved.
5. Review related alerts and nearby events.
6. Enrich with identity, endpoint, network, vulnerability, and threat context.
7. Decide whether evidence supports benign, suspicious, or confirmed malicious activity.
8. Record the reason, evidence, uncertainty, and next action.

## Investigation structure
Use a repeatable structure:
- **What happened?** Describe the observed behavior without exaggeration.
- **When?** Record first/last observed timestamps and timezone.
- **Where?** Identify assets, accounts, IPs, applications, and locations.
- **Who?** Identify actor, target, and account owner where known.
- **How?** Explain the process, access path, or technique.
- **Impact:** State what may have been exposed, changed, or disrupted.
- **Scope:** Identify other potentially affected systems/accounts.
- **Confidence:** Explain evidence strength and gaps.
- **Next action:** Recommend an approved action and owner.

## Incident response lifecycle
A common lifecycle includes preparation; detection and analysis; containment; eradication; recovery; and post-incident improvement. Follow the organization's incident response plan and current authoritative guidance. Different frameworks use different names and phases.

### Containment
Containment may include isolating a host, disabling an account, revoking sessions, blocking a domain, or restricting a workload. These actions can disrupt business and destroy volatile evidence. SOC analysts should follow approval, authority, and emergency procedures. Never independently take disruptive action unless explicitly authorized.

### Evidence handling
Record who collected evidence, when, from which system, using which method, and where it was stored. Preserve original files, compute hashes when appropriate, restrict access, and maintain chain-of-custody records when required. Do not alter original evidence. Follow legal, privacy, and retention requirements.

## Escalation
Escalate promptly when there is credible compromise, privileged account activity, sensitive data exposure, ransomware, destructive behavior, multiple affected systems, critical service impact, or uncertainty that exceeds your authority. Include concise summary, timeline, impacted assets, evidence links, actions already taken, business impact, confidence, and requested decision.

## Case closure
A closure note should explain what was investigated, evidence reviewed, conclusion, reason for benign/false-positive classification or incident escalation, remaining uncertainty, and follow-up work. Avoid vague notes such as “looks fine.”

## Communication during an incident
Use a single source of truth for updates. Separate confirmed facts from working hypotheses. State time zone. Avoid blame and unsupported attribution. Share only with authorized stakeholders. Record decision owner and next update time.

## Practical exercise
Use a simulated alert about a privileged account added outside a change window. Write triage notes, evidence checklist, escalation summary, and a closure/escalation decision. Do not make actual account changes.

## Knowledge check
1. What is the purpose of triage?
2. Why can containment affect evidence?
3. What belongs in an escalation summary?
4. What is chain of custody?
5. Why separate facts from hypotheses?
