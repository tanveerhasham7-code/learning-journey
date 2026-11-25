# Lab 2 — Local Accounts and Groups

## Lab details

- **Lab:** 02 — Local Accounts and Groups
- **Date performed:** 25 November 2026
- **Platform:** Learner's Windows endpoint
- **Objective:** Review local Windows users and groups, inspect local Administrators membership, create and verify a temporary standard user, and remove the test account after the exercise.
- **Scope:** Local account administration on the learner's own Windows computer.

## Objective and theory

Local accounts identify users who can sign in to a Windows computer. Local groups make it easier to assign permissions to a set of users. The built-in **Users** group normally contains standard accounts, while membership in **Administrators** grants elevated administrative privileges.

For SOC analysts, reviewing local accounts and privileged group membership helps identify unexpected accounts and excessive privileges. Temporary test accounts should be removed when no longer needed.

## Procedure performed

The learner performed the following PowerShell checks:

1. Listed local accounts:

   ```powershell
   Get-LocalUser
   ```

2. Listed local groups:

   ```powershell
   Get-LocalGroup
   ```

3. Reviewed members of the local Administrators group:

   ```powershell
   Get-LocalGroupMember -Group "Administrators"
   ```

4. Prepared a secure password for a temporary lab account:

   ```powershell
   $Password = Read-Host "Enter a password" -AsSecureString
   ```

5. Created a temporary local account named `SOC_TestUser`:

   ```powershell
   New-LocalUser -Name "SOC_TestUser" -Password $Password -FullName "SOC Lab Test User" -Description "Temporary SOC lab account"
   ```

6. Verified the account details:

   ```powershell
   Get-LocalUser -Name "SOC_TestUser"
   ```

7. Reviewed membership of the standard Users and Administrators groups:

   ```powershell
   Get-LocalGroupMember -Group "Users"
   Get-LocalGroupMember -Group "Administrators"
   ```

8. Checked selected account properties:

   ```powershell
   Get-LocalUser -Name "SOC_TestUser" | Select-Object Name, Enabled, PasswordRequired, LastLogon
   ```

9. Removed the temporary account and ran a final existence check:

   ```powershell
   Remove-LocalUser -Name "SOC_TestUser"

   if (Get-LocalUser -Name "SOC_TestUser" -ErrorAction SilentlyContinue) {
       "SOC_TestUser still exists"
   } else {
       "SOC_TestUser successfully removed"
   }
   ```

## Results and analysis

- The learner ran the local-user, local-group and Administrators-membership inventory commands.
- A temporary account named `SOC_TestUser` was created after the learner reopened PowerShell with administrator privileges and re-entered the secure password variable.
- The learner ran account-detail and group-membership checks to review the temporary account.
- The learner ran the account-removal command and a final check for the test account.
- Exact account counts, full membership lists and command output values are not transcribed in this report; the uploaded screenshots are retained as the practical evidence.

## Troubleshooting notes

| Issue | Cause | Resolution |
|---|---|---|
| `New-LocalUser` returned **Access denied** | PowerShell was not running with elevated administrator privileges | Reopened PowerShell using **Run as administrator** and verified elevation with `net session` |
| `$Password` was null | The secure-string variable was created in the earlier PowerShell session and was not available in the new elevated session | Re-created the variable with `Read-Host -AsSecureString` in the elevated session |
| Description length validation failed | The first description exceeded the cmdlet's 48-character limit | Used the shorter description `Temporary SOC lab account` |

## Practical evidence

The screenshots below are embedded directly in this report. They are stored separately in the Lab 02 evidence folder.

### Screenshot 1 — Initial local account inventory

![Lab 02 screenshot 1 — local account inventory](../screenshort/lab-02/Screenshot%202026-11-25%20145048.png)

### Screenshot 2 — Local groups and group review

![Lab 02 screenshot 2 — local groups](../screenshort/lab-02/Screenshot%202026-11-25%20145332.png)

### Screenshot 3 — Administrators group membership

![Lab 02 screenshot 3 — Administrators group review](../screenshort/lab-02/Screenshot%202026-11-25%20145419.png)

### Screenshot 4 — Account creation and elevation troubleshooting

![Lab 02 screenshot 4 — account creation workflow](../screenshort/lab-02/Screenshot%202026-11-25%20150303.png)

### Screenshot 5 — Elevated PowerShell workflow

![Lab 02 screenshot 5 — elevated PowerShell](../screenshort/lab-02/Screenshot%202026-11-25%20150316.png)

### Screenshot 6 — Temporary account workflow

![Lab 02 screenshot 6 — temporary account](../screenshort/lab-02/Screenshot%202026-11-25%20150400.png)

### Screenshot 7 — Account and group verification

![Lab 02 screenshot 7 — account verification](../screenshort/lab-02/Screenshot%202026-11-25%20150546.png)

### Screenshot 8 — Lab cleanup and final account check

![Lab 02 screenshot 8 — cleanup](../screenshort/lab-02/Screenshot%202026-11-25%20150654.png)

## Security observations

- Review local Administrators membership regularly and investigate accounts that do not have a clear business need for elevated access.
- Use standard accounts for everyday work and reserve administrative privileges for tasks that require them.
- Use temporary accounts only for controlled testing and remove them after the exercise.
- Never publish passwords, password hints, recovery information or other account secrets in screenshots or repository files.

## Cleanup and rollback

The learner ran `Remove-LocalUser -Name "SOC_TestUser"` and a follow-up existence check. The test account was intended to be temporary; do not remove any personal or built-in Windows accounts as part of this exercise.

## Learning reflection

This lab practiced basic local identity administration with PowerShell. It demonstrated how to enumerate users and groups, review privileged group membership, create a temporary local account, verify its properties and remove it after testing. It also provided troubleshooting practice with elevation requirements and PowerShell session variables.

## Status

- [x] Planned
- [x] Performed
- [x] Evidence uploaded
- [x] Reviewed
- [x] Published

**Evidence note:** The learner confirmed running the commands and uploaded eight screenshots to the repository. Exact command output values are not reproduced here unless visible in the saved evidence.
