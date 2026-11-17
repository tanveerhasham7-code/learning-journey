# Practical 07 — Phishing Tabletop

## Status and scope

**Prepared as an assistant-authored reference tabletop.** This document provides a complete worked example for study. The learner has not independently completed or validated this exercise, so it is not recorded as learner-completed evidence.

This is a fictional email-analysis exercise. No email was sent, no link or attachment was opened, and no real account or system was accessed.

## Objective

Recognize common phishing indicators and describe safe handling and reporting actions without interacting with a suspicious message.

## Fictional suspicious email

**From:** `IT Helpdesk <support@example-security-check.com>`  
**Subject:** URGENT: Your university account will be disabled in 30 minutes  
**Message:**

> Dear Student,  
> We detected a problem with your mailbox. Your account will be permanently disabled unless you verify it immediately.  
> Click the link below to keep your account active:  
> `https://example-security-check.com/verify`  
> Open the attached file, `Account_Verification.html`, if the link does not work.  
> Thank you,  
> IT Support Team

This example uses a reserved example domain and is not a real university notification.

## 1. Warning signs identified

| Indicator | Why it is suspicious |
|---|---|
| Urgent 30-minute deadline | Creates panic and pressures the recipient to act without checking. |
| Sender domain does not clearly match the university | The display name says IT Helpdesk, but the actual email domain is unfamiliar. |
| Threat of account disablement | Uses fear to make the recipient follow instructions. |
| Request to verify through an email link | May lead to a fake sign-in page designed to steal credentials. |
| Unexpected HTML attachment | HTML files can open deceptive pages or redirect users; an unexpected attachment should not be opened. |
| Generic greeting | Does not identify the recipient or provide a verifiable support ticket. |

No single indicator proves an email is malicious. The combination makes this message suspicious and requires verification through a trusted channel.

## 2. Safe handling steps

1. Do not click the link.
2. Do not open or download the attachment.
3. Do not reply with passwords, verification codes, or personal information.
4. Do not forward the message casually to other people.
5. Use the university's known official website, helpdesk number, or previously verified support channel to confirm whether the message is genuine. Do not use contact details supplied in the suspicious email.
6. Report the message using the organization's approved phishing-reporting button or IT/security helpdesk process.
7. Keep the original message available for the security team if policy requires it; do not alter or delete potential evidence unless instructed.

## 3. If the recipient already clicked or entered credentials

- Report the incident to the official IT/security team immediately.
- From a trusted device and using the official site, change the affected password.
- Ask the security team to revoke active sessions and review account sign-in activity.
- If the same password was reused elsewhere, change it on those services too.
- Enable or verify multi-factor authentication where available.
- Preserve the email, approximate click time, and any warning or browser page details. Do not revisit the suspicious link to collect evidence.

Changing a password alone may not end existing sessions; session revocation and log review are important.

## 4. Example report to the security team

> Subject: Suspicious email claiming university account suspension  
>
> I received an email claiming that my university account would be disabled in 30 minutes unless I verified it through an unfamiliar link. It also included an unexpected HTML attachment. I did not open the attachment or follow the link. Please review the message and confirm whether it is legitimate. I can provide the original email through the approved reporting process.

## 5. Recommended organizational controls

- **Administrative:** publish a clear phishing-reporting procedure and provide regular awareness training.
- **Technical:** deploy email filtering and authentication controls such as SPF, DKIM, and DMARC; use multi-factor authentication for accounts.
- **Detective:** monitor reported messages, suspicious sign-ins, and unusual mailbox activity.

These controls reduce risk but cannot guarantee that every phishing message will be blocked.

## 6. Learning outcome

The example demonstrates how urgency, an unfamiliar sender domain, credential-verification links, and unexpected attachments can indicate phishing. The safest response is to avoid interacting with the message, verify through an independent trusted channel, and report it.

## Evidence and limitations

- Evidence type: assistant-authored fictional tabletop and worked analysis.
- No learner screenshots or real email headers were provided.
- No live email, link, attachment, account, or security control was tested.
- This report demonstrates the analysis method; it does not prove that the learner personally performed the exercise.

## Completion note

**Reference material prepared. Learner practical completion remains pending** until the learner independently reviews a fictional or safely provided sample, identifies the warning signs, and explains the reporting steps.
