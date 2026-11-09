# 07 — Common Cyber Attacks and Attack Lifecycle

## Common attacks
- Phishing: deceptive messages that seek credentials, clicks, or harmful file execution.
- Malware: software intended for harmful or unauthorized actions; examples include trojans, spyware, worms, and ransomware.
- Ransomware: an operation that makes data unavailable, often through encryption or theft/extortion.
- Credential attacks: misuse of stolen, guessed, reused, or exposed credentials.
- Denial of service: attempts to make a service unavailable.
- Man-in-the-middle: interception or manipulation of communication.
- Web attacks: injection, broken access control, insecure design, and cross-site scripting.
- Insider threats: harmful or accidental actions by people with legitimate access.

## Attack lifecycle
An intrusion may involve reconnaissance, initial access, execution, persistence, privilege escalation, defense evasion, credential access, discovery, lateral movement, collection, command and control, and actions on objectives. Incidents do not always follow a fixed order.

MITRE ATT&CK describes adversary tactics (goals) and techniques (methods). Mapping an event to ATT&CK is a hypothesis that needs evidence, not automatic proof.

## Indicators and evidence
Unusual login times, unexpected processes, suspicious connections, hashes, or repeated failures may be indicators. One indicator alone rarely proves compromise. Correlate sources, build a timeline, compare normal behavior, and document uncertainty.

## Practical
Analyze a fictional suspicious-email report. List warning signs, evidence to preserve, who should be notified, and safe response steps. Do not click suspicious links or open attachments.
