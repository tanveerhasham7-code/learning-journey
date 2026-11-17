# Practical Exercises — Cybersecurity Fundamentals

Only use systems and accounts you own or are explicitly authorized to use.

1. **Asset inventory:** list 3–5 non-sensitive assets, purpose, sensitivity, owner, and protection needs.
2. **CIA analysis:** classify scenarios involving unauthorized reading, data alteration, outage, and changed installer hash.
3. **Risk register:** record asset, threat, weakness, likelihood, impact, controls, treatment, and owner.
4. **Control mapping:** choose administrative, technical, and detective controls for one risk; explain limitations.
5. **Account review:** inspect administrator versus standard-user access on your own device. Do not publish account names.
6. **SHA-256 integrity:** create a harmless text file, calculate its hash with PowerShell Get-FileHash or Linux sha256sum, change one character, and compare.
7. **Phishing tabletop:** identify warning signs and safe reporting steps for a fictional suspicious email.
8. **Patch review:** inspect OS update settings and record pending updates.
9. **Log reading:** inspect a harmless Windows Event Viewer or Linux log event; record timestamp, source, and meaning.
10. **Incident-response tabletop:** create a timeline, evidence list, containment proposal, and uncertainty notes for a fictional case.
11. **Backup plan:** back up non-sensitive study files and test restoring one file.

## Practical progress

- [Practical 01 — Asset Inventory](lab/lab-01-asset-inventory.md) — **Completed (initial inventory; some hardware query fields remain unverified).**
- [Practical 02 — CIA Triad Analysis](lab/lab-02-cia-triad-analysis.md) — **Completed (four scenario answers and reasoning documented; no screenshots taken).**
- [Practical 03 — Risk Register](lab/lab-03-risk-register.md) — **In progress (initial assessment of one Windows 11 Pro laptop documented; two more assets and final risk ratings remain).**
- [Practical 04 — Security Control Mapping](lab/lab-04-security-control-mapping.md) — **Completed (fictional phishing tabletop; controls, limitations, and response steps documented; no live system changes or screenshots).**

## Evidence record
For each exercise, record date, general environment, objective, steps performed, actual observations, safe screenshot filename, what the result proves and does not prove, problems, and next action.

Do not invent output or mark exercises complete just because instructions exist. Never upload credentials, tokens, personal data, or sensitive logs.

- [Practical 05 — Account Review](lab/lab-05-account-review.md) — **Completed (current signed-in account reported as Administrator; separate account under Other users remains unclassified).**
- [Practical 06 — SHA-256 Integrity](lab/lab-06-sha256-integrity.md) — **Completed (learner reported different hashes after modifying a harmless test file; exact hashes/screenshots not supplied).**
