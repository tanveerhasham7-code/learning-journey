# Practical 05 — Account Review

**Status:** Completed — account listing and current account role recorded  
**Assessment type:** Local account review (user-reported observation)  
**Privacy:** No account names, email addresses, SIDs, or other identifiers are included.

## Objective

Review the accounts visible on the learner's own Windows device and determine whether access is assigned as Administrator or Standard User. The purpose is to understand least privilege and avoid unnecessary administrator access.

## Observation recorded

The learner opened **Settings → Accounts → Other users** and reported that **one account** was visible in that section. The learner then checked **Settings → Accounts → Your info** and reported that the currently signed-in account is labelled **Administrator**.

These are user-reported observations. The Administrator label applies to the current signed-in account; it does **not** establish the role of the separate account listed under Other users, nor the total number of accounts on the device.

## Security interpretation

- Keeping the number of accounts limited can make access easier to review, but the count alone does not prove that access is secure.
- Administrator access should be limited to accounts that genuinely need it.
- A standard account is generally preferable for everyday work; administrative actions can be performed with approved elevation when required.
- Account names and personal identifiers are intentionally excluded from this public report.

## Review result

- Current signed-in account: **Administrator** (learner-reported from Windows Settings → Accounts → Your info).
- Other users section: **one account visible** (learner-reported); its individual role has not been checked.
- No account settings or group memberships were changed.

## Conclusion

This practical is marked **completed for the current-account privilege review**. The review confirms that the current signed-in account has Administrator privileges, so it can perform elevated system tasks. For everyday activity, a Standard User account is generally preferable where practical, with elevation used only when needed. The separate account listed under Other users remains unclassified; do not assume it is an Administrator.

No credentials or personal identifiers were collected.

## Evidence

No screenshot was supplied for this practical. Both observations are recorded from the learner's messages; no usernames or personal identifiers are included.
