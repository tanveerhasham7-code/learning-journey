# Email and Phishing Alert Investigation

## 1. Why email investigations matter

Email is a common delivery path for credential theft, malware, business email compromise (BEC), and social engineering. A Tier 1 analyst must examine the message and its technical evidence without clicking suspicious links or opening attachments.

## 2. Key terms

- **Sender / From:** The displayed sender identity. It can be spoofed.
- **Return-Path:** Address used for bounce handling; compare it with the visible sender.
- **Reply-To:** Destination for replies; unexpected differences can be suspicious.
- **SPF:** Checks whether the sending host is authorized by the sender domain's SPF policy.
- **DKIM:** A cryptographic signature that helps verify message integrity and domain signing.
- **DMARC:** A policy and reporting mechanism that uses SPF/DKIM alignment.
- **URL reputation:** External context about a link. Reputation results are signals, not proof.
- **BEC:** Business Email Compromise, often involving impersonation or payment/information requests.

## 3. Common warning signs

Unexpected urgency, credential requests, payment changes, unusual attachments, mismatched sender domains, lookalike domains, unexpected Reply-To, link text that differs from the actual destination, and authentication failures. A single indicator does not automatically prove phishing.

## 4. Safe investigation workflow

1. Acknowledge the alert and note the detection source and time.
2. Preserve the original message or approved forensic copy; do not forward it casually.
3. Review sender, recipient, subject, timestamps, message ID, Return-Path and Reply-To.
4. Review SPF, DKIM and DMARC results and alignment.
5. Extract URLs and attachment metadata using approved tools; do not open or execute them.
6. Review mail gateway verdicts, sandbox results, URL reputation and threat-intelligence context where available.
7. Search approved telemetry for other recipients, clicks, downloads, sign-ins or endpoint activity.
8. Decide whether evidence supports true positive, false positive, benign positive or inconclusive.
9. Follow the playbook for escalation and containment. Do not delete messages or block senders without authorization.
10. Record findings, evidence references, actions, owner and next step.

## 5. Investigation decision examples

- A display name resembles the CEO, but the sending domain is unrelated and the message requests urgent payment: suspicious impersonation; escalate under the BEC playbook.
- SPF fails but DKIM and DMARC pass with valid alignment: do not decide from SPF alone; examine the full authentication result and mail path.
- A marketing message contains a tracking URL but no credential request, malicious attachment or other suspicious behavior: potentially benign; document why.

## 6. Evidence to record

Message ID, sender and recipient (redacted in public portfolio), timestamps and timezone, authentication results, URL/attachment hashes or safe metadata, gateway verdict, related sign-in/endpoint events, analyst conclusion, confidence, escalation and case ID.

## 7. Practical exercises

- Use a synthetic email sample to identify sender, Reply-To, URLs and authentication results.
- Build a simple phishing triage checklist.
- Write a case note that separates observed facts from assumptions.
- Practice identifying what must be escalated to Tier 2.

## 8. Common mistakes

Clicking links, opening attachments, trusting display names, treating one failed authentication check as proof, publishing real email addresses, or claiming an email was malicious without corroborating evidence.
