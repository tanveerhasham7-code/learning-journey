# 02 — Accounts, Groups and Authentication

## Local accounts
A local account is stored on one Windows computer. It has an identity, credentials and group memberships. A standard user performs everyday tasks with limited rights. An administrator can make system-wide changes and should be used only when necessary.

## Groups
Groups make access management easier. Examples include Users, Administrators, Remote Desktop Users and Event Log Readers. Membership in Administrators grants powerful privileges, so review it regularly.

~~~powershell
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember -Group "Administrators"
whoami /groups
~~~

Some commands need an elevated PowerShell session or a supported Windows edition.

## Authentication methods
- Password: a secret known by the user; use unique, long passwords.
- Windows Hello: PIN or biometric sign-in tied to a device.
- Smart card/certificate: cryptographic identity.
- MFA: combines different factor types.
- Kerberos: ticket-based authentication commonly used in AD domains.
- NTLM: older challenge-response authentication; modern environments should reduce legacy use where possible after compatibility review.

A Windows Hello PIN is not simply the same as an account password; it is designed to be device-bound.

## Password and lockout policy
Organizations may configure password length, history and account lockout. Combine good password practices with MFA and secure password managers. Avoid arbitrary policy changes without understanding their effect.

~~~powershell
net accounts
~~~

## Practical lab
Create a standard test account using Settings → Accounts → Other users. Do not add it to Administrators. Sign in as the test account and observe which tasks require elevation. Inspect local groups, record findings and remove the test account after the lab.

Never publish passwords, password databases, hashes or recovery codes.

## Check yourself
Why are groups easier to manage than individual permissions? What is the high-level difference between Kerberos domain authentication and a local account sign-in?
