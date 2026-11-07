# 02 — Security Principles, Threats, and Attack Lifecycle

## Security foundations
- **Confidentiality:** Information is accessible only to authorized people and systems.
- **Integrity:** Information and systems remain accurate and are changed only in authorized ways.
- **Availability:** Services and information remain usable when needed.
- **Authentication:** Establishing who or what is requesting access.
- **Authorization:** Determining what an authenticated identity may do.
- **Accounting/auditing:** Recording actions so they can be reviewed.

SOC analysts use these ideas to explain impact. Stolen credentials threaten confidentiality and integrity; ransomware may threaten availability and integrity.

## Threat vocabulary
- **Asset:** Something valuable, such as a laptop, identity, database, or service.
- **Threat actor:** Person or group capable of causing harm.
- **Vulnerability:** A weakness that could be exploited.
- **Exploit:** A method that takes advantage of a weakness.
- **IOC:** Indicator of Compromise, an artifact associated with possible malicious activity, such as a hash, domain, IP, or file path.
- **IOA:** Indicator of Attack, behavior suggesting an attack is underway.
- **TTP:** Tactics, techniques, and procedures used by an actor.
- **Risk:** Likelihood and impact considered in organizational context.

An IOC is not automatically malicious forever. IPs and domains can be shared, reassigned, or used legitimately. Validate context and freshness.

## Common attack categories
Phishing and business email compromise; password spraying, brute force, credential stuffing, and stolen sessions; malware and ransomware; exploitation of exposed services; privilege escalation and persistence; lateral movement; data theft and cloud compromise; denial of service; insider misuse; and accidental data exposure.

## Attack lifecycle as an investigation aid
A simplified lifecycle includes reconnaissance, initial access, execution, persistence, privilege escalation, defense evasion, credential access, discovery, lateral movement, collection, command and control, and impact. Real incidents do not always follow a neat sequence. Use the lifecycle to ask what may have happened before and after an observed alert.

## MITRE ATT&CK
MITRE ATT&CK is a knowledge base of adversary tactics and techniques based on observed behavior. Tactics describe an adversary goal; techniques describe ways to achieve it; sub-techniques add detail. Use ATT&CK to describe behavior consistently, identify telemetry and detection opportunities, organize hunting hypotheses, find coverage gaps, and communicate findings. A technique mapping does not prove a specific actor was responsible.

## Important concepts
- **Least privilege:** Give identities only required access.
- **Defense in depth:** Use multiple complementary controls.
- **Zero trust:** Evaluate identity, device, and context rather than trusting network location alone.
- **Attack surface:** Systems and paths that could be exposed.
- **Lateral movement:** Moving from one system or account to another.
- **Persistence:** Maintaining access after initial compromise.
- **Exfiltration:** Unauthorized movement of data out of an environment.
- **Living off the land:** Misusing legitimate system tools for malicious purposes.

## Build an investigation hypothesis
Observation: PowerShell starts with an encoded command on a workstation. Possible explanations include a legitimate management script, an administrator deployment, a user launching a suspicious attachment, or malware execution. Collect parent process, command line, user, host, signature, script logs if enabled, file origin, network connections, and surrounding events. Do not decide from one field alone.

## Practical task
For each scenario, list likely assets, possible impact, useful telemetry, and three investigation questions:
1. A user reports an unexpected MFA prompt.
2. A server makes repeated DNS requests to a rare domain.
3. A new administrator account appears outside the change window.
4. A workstation creates many files with unusual extensions.

## Knowledge check
1. Distinguish IOC and IOA.
2. Why is IP reputation not conclusive?
3. Explain tactic versus technique.
4. Give two defense-in-depth controls.
5. Why avoid unsupported threat-actor attribution?
