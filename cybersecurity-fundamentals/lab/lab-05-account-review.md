# Practical 05 — Account Review

**Status:** In progress — initial account listing recorded; account privilege level not yet verified  
**Assessment type:** Local account review (user-reported observation)  
**Privacy:** No account names, email addresses, SIDs, or other identifiers are included.

## Objective

Review the accounts visible on the learner's own Windows device and determine whether access is assigned as Administrator or Standard User. The purpose is to understand least privilege and avoid unnecessary administrator access.

## Observation recorded

The learner opened **Settings → Accounts → Other users** and reported that **one account** was visible in that section.

This is a user-reported count only. It does not establish the total number of Windows accounts on the device, and it does not identify the account's role. The account could be an Administrator or a Standard User; this has not yet been checked.

## Security interpretation

- Keeping the number of accounts limited can make access easier to review, but the count alone does not prove that access is secure.
- Administrator access should be limited to accounts that genuinely need it.
- A standard account is generally preferable for everyday work; administrative actions can be performed with approved elevation when required.
- Account names and personal identifiers are intentionally excluded from this public report.

## Verification still required

The local account role cannot be inspected remotely from this GitHub workflow. On the Windows device, open **Settings → Accounts → Your info** and check whether the account is labelled **Administrator**. Alternatively, in PowerShell, run:

```powershell
whoami /groups
```

Look for the local Administrators group entry; group membership details should be interpreted carefully, and no usernames or full command output need to be published. A safer summary to record here is only the role label: **Administrator** or **Standard User**.

## Conclusion

The initial listing observation has been documented, but this practical is **not marked complete** because the account's privilege level has not been verified. No account configuration was changed, and no credentials or personal identifiers were collected.

## Evidence

No screenshot was supplied for this practical. The account count above is recorded from the learner's message; role verification remains pending.
