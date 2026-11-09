# 05 — Identity and Access Management

## Four concepts
- Identification: a user claims an identity.
- Authentication: the system verifies the claim.
- Authorization: the system decides what that identity may do.
- Accounting/auditing: relevant actions are recorded.

Authentication does not mean a user should access every resource.

## Authentication factors
Something you know (password/PIN), something you have (security key/authenticator), and something you are (biometric). MFA uses two or more different factor types. Two passwords are not MFA. Prefer phishing-resistant methods such as FIDO2 security keys/passkeys where available.

## Password security
Use unique passwords, a password manager, and MFA. Passwords should be stored with a dedicated password-hashing scheme using unique salts and suitable work factors, never plain text or reversible encryption. Never publish passwords, recovery codes, or tokens.

## Access models
- RBAC: permissions assigned to roles.
- ABAC: decisions use attributes such as department, device status, sensitivity, and time.
- DAC: resource owner decides access.
- MAC: centrally enforced labels and rules govern access.

## Least privilege and lifecycle
Create accounts through approval, grant minimum permissions, review access, update it when roles change, and disable accounts when no longer needed. Separate daily user accounts from privileged accounts. Review service accounts too.

## Practical
Review accounts on your own computer using normal settings. Identify administrator versus standard-user access. Do not change a managed device or publish account names.
