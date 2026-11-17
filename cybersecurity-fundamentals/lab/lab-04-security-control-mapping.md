# Practical 04 — Security Control Mapping

## Objective
Map administrative, technical, and detective security controls to a fictional phishing risk. Explain each control's purpose, limitations, and what to do if prevention fails.

## Scenario
A company's employees receive fake emails containing malicious links. An employee may click a link and enter their work password on a fraudulent website. An attacker could then attempt to access company systems using the stolen credentials.

This is a fictional tabletop scenario. No phishing email was sent, no account was accessed, and no security settings were changed.

## Risk summary
- **Asset:** Employee accounts and company information
- **Threat:** Phishing attacker attempting to steal employee credentials
- **Potential weakness:** Employees may not recognize a convincing fake email, and password-only authentication may allow stolen credentials to be reused
- **Potential impact:** Unauthorized account access, data exposure, fraudulent actions, and disruption to business operations

## Control mapping

### 1. Administrative control — Security awareness and reporting policy
Provide regular phishing-awareness training and a clear policy explaining how employees should verify suspicious requests, avoid unexpected links and attachments, and report suspicious emails to the security team.

- **Purpose:** Reduce the chance that an employee will trust and act on a phishing message.
- **Limitation:** Training cannot prevent every mistake. Attackers can create convincing messages, and employees may still click a link.

### 2. Technical control — Email filtering and multi-factor authentication
Use an email security gateway to detect or quarantine suspicious messages, malicious links, and spoofed sender domains. Configure domain email authentication (SPF, DKIM, and DMARC) appropriately. Require multi-factor authentication (MFA) for employee accounts.

- **Purpose:** Filtering reduces the number of dangerous emails reaching inboxes. MFA adds another authentication step, making a stolen password alone less useful.
- **Limitation:** Filters can miss new or carefully crafted phishing messages. MFA methods can also be targeted through phishing or social engineering; stronger phishing-resistant MFA is preferable where supported.

### 3. Detective control — Email and identity monitoring
Collect and monitor email-security alerts and identity sign-in logs. Alert on suspicious sign-in patterns, unexpected authentication attempts, and reports of phishing messages. Provide an easy way for employees to report suspicious email.

- **Purpose:** Help the security team detect suspicious activity and investigate quickly.
- **Limitation:** Monitoring does not itself stop an attack. Alerts need to be reviewed, tuned, and acted upon.

## If prevention fails
If an employee clicks the link or enters a password:
1. Report the email and incident to the security team immediately.
2. Preserve the suspicious email and relevant timestamps; do not forward it widely or interact with the link again.
3. From a trusted device, reset the affected password and revoke active sessions or tokens where appropriate.
4. Review sign-in logs and account activity for unauthorized access.
5. Quarantine or block the malicious email, URL, and sender indicators where appropriate.
6. If compromise is confirmed, follow the organization's incident-response process, assess affected data, and document actions and lessons learned.

## Control comparison

| Control type | Selected control | Main purpose | Key limitation |
|---|---|---|---|
| Administrative | Phishing awareness and reporting policy | Help staff recognize and report phishing | Human error can still happen |
| Technical | Email filtering plus MFA | Reduce malicious email delivery and protect accounts | Filters may miss messages; MFA can be targeted |
| Detective | Email and identity log monitoring | Identify suspicious activity for investigation | Requires alert review and response |

## What this exercise demonstrates
- A single risk should be addressed with multiple layers of defense.
- Administrative, technical, and detective controls serve different purposes and work best together.
- Detection and incident response remain important even when preventive controls are enabled.

## Evidence and limitations
This report documents a completed, fictional scenario-based control-mapping exercise. It is not evidence that any company deployed these controls or that a live environment was tested. No screenshots were required or collected, and no real accounts, emails, or systems were changed.

## Status
**Completed — tabletop control mapping and response plan documented.**
