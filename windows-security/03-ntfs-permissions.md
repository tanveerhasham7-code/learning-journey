# 03 — NTFS Permissions and Access Control

## Why permissions matter
Access control determines who can read, change, execute or delete information. Excessive permissions increase the damage possible after an account compromise or malware infection.

## Common NTFS permissions
- **Full Control:** broad control, including changing permissions and ownership.
- **Modify:** read, write, execute and delete.
- **Read & Execute:** view files and run permitted programs.
- **List Folder Contents:** view names inside a folder.
- **Read:** view file contents and attributes.
- **Write:** create or change files where allowed.

Permissions can be Allow or Deny. Inheritance passes permissions from a parent folder to child items. Avoid complicated Deny rules where a clear group-based Allow configuration is sufficient.

## Share versus NTFS permissions
For network access, both share permissions and NTFS permissions can apply. Effective remote access is constrained by their combination. NTFS permissions also apply to local access.

## Inspect permissions
~~~powershell
Get-Acl "C:\Users\Public" | Format-List
icacls "C:\Users\Public"
~~~

## Safe lab
1. Create C:\CyberLab\TeamFiles.
2. Create a standard test user.
3. Inspect the folder using icacls.
4. Use folder Properties → Security to grant the test user read access only.
5. Sign in as the test user and test reading and writing.
6. Record the result and remove the test folder.

Use a lab folder only. Do not change permissions on Windows system directories. Do not assume a setting worked until you test with the target account.

## Auditing
Windows can record selected file access events when the correct audit policy and object auditing are configured. Audit only what is useful; excessive logging creates noise.

## Check yourself
What is the difference between Read, Modify and Full Control? Why should permissions usually be assigned to groups?
