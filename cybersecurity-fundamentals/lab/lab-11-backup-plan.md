# Practical 11 — Backup Plan

**Status:** Assistant-prepared reference plan; actual backup and restore test by learner remain pending  
**Date prepared:** 2026-11-17  
**Suggested environment:** Personal Windows 11 Pro laptop (user-reported)

## 1. Objective

Create a simple backup plan for non-sensitive study materials and explain how to test that a backup can be restored. A backup is useful only when the files can be recovered.

## 2. Assets to protect

The following are suggested file categories based on the learning workflow. They are planning examples, not a verified inventory of files currently stored on the laptop.

| Data category | Examples | Suggested priority |
|---|---|---|
| Study notes | University notes, lecture summaries, revision material | High |
| Cybersecurity work | Lab reports, scripts, project documentation | High |
| Evidence | Sanitized lab screenshots and diagrams | Medium–High |
| Personal configuration | Non-secret project configuration and learning checklists | Medium |

Do not back up or publish passwords, API keys, access tokens, private keys, identity documents, or confidential third-party data as part of this exercise.

## 3. Backup strategy — 3-2-1 rule

Use the 3-2-1 principle:

- Keep **3 copies** of important data: the working copy and two backups.
- Store copies on **2 different types of storage or platforms** where practical.
- Keep **1 copy off-site**, such as a trusted cloud storage account or a drive stored in a separate secure location.

Example arrangement:

1. Working copy on the laptop.
2. Backup copy on an external USB drive, disconnected safely after backup.
3. Off-site copy in a reputable cloud storage service with multi-factor authentication.

This is a recommended design, not a claim that these backups have been created.

## 4. Backup schedule

| Data | Suggested frequency | Reason |
|---|---|---|
| Active lab reports and study notes | After each meaningful work session or daily | Reduces loss of recent work |
| Screenshots and project folders | Weekly, and after completing a lab | Preserves evidence and milestones |
| Full review of backup contents | Monthly | Detects missing or outdated folders |
| Restore test | Monthly or after changing backup method | Confirms recoverability |

The schedule should be adjusted to how often files change and how much data loss is acceptable.

## 5. Safe backup procedure on Windows

1. Choose a folder containing only non-sensitive study files.
2. Connect a trusted external drive or use an approved cloud backup location.
3. Copy the selected folder to a clearly named backup folder, for example `Cybersecurity-Study-Backup`.
4. Include the backup date in the folder name, for example `2026-11-17`.
5. Wait for the copy to finish and check that the expected files and folders are present.
6. If using an external drive, use Windows **Safely Remove Hardware / Eject** before disconnecting it.
7. Keep the external backup disconnected when it is not being used, reducing exposure to ransomware or accidental deletion.
8. Confirm that cloud backup is complete and that multi-factor authentication is enabled on the account.

Do not overwrite the only good copy of a file. Avoid syncing accidental deletions or corrupted files as the sole backup strategy; version history or a separate offline copy can help.

## 6. Restore test procedure

A restore test should use a harmless sample file, not an important original.

1. Create a small text file in a test folder, such as `backup-restore-test.txt`, with harmless text.
2. Copy it into the backup location using the procedure above.
3. Create a separate restore-test folder.
4. Copy the backed-up file from the backup location into the restore-test folder.
5. Open the restored copy and confirm that its content matches the original.
6. Optionally compare SHA-256 hashes of the original and restored copies using PowerShell:

```powershell
Get-FileHash "$env:USERPROFILE\Desktop\backup-restore-test.txt" -Algorithm SHA256
Get-FileHash "$env:USERPROFILE\Desktop\Restore-Test\backup-restore-test.txt" -Algorithm SHA256
```

Matching hashes indicate that the two files have identical contents with extremely high confidence. They do not prove that the backup process will recover every file or that the file itself is safe.

7. Record the date, files tested, result, and any problems. Remove the harmless test files when finished if they are no longer needed.

## 7. Recovery checklist

- [ ] Identify which files or folders are missing or damaged.
- [ ] Choose the newest known-good backup.
- [ ] Scan the computer and address malware concerns before reconnecting backup media if compromise is suspected.
- [ ] Restore files to a separate location first when possible.
- [ ] Check file names, sizes, contents, and hashes where appropriate.
- [ ] Confirm important applications can open the restored files.
- [ ] Copy restored files back to their normal location only after verification.
- [ ] Record the recovery date and any files that could not be restored.

## 8. Risks and safeguards

| Risk | Safeguard |
|---|---|
| External drive lost or stolen | Encrypt the drive and store it securely |
| Ransomware encrypts connected backups | Keep an offline or immutable backup copy |
| Cloud account takeover | Use a unique password and MFA |
| Backup silently fails | Review backup status and test restores |
| Accidental deletion syncs to backup | Use version history and a separate offline copy |
| Backup contains sensitive information | Minimize data, restrict access, and encrypt it |

## 9. Result and limitations

This document provides a backup design, safe copy procedure, restore-test method, and recovery checklist. No files were copied, no external drive or cloud account was accessed, and no restore operation was performed by the assistant.

**Practical 11 remains assistant-prepared reference material, not learner-completed.** To record hands-on completion, the learner must perform a backup of non-sensitive study material and successfully restore one harmless test file.

## 10. Conclusion

A good backup plan has more than one copy, separates at least one copy from the primary device, protects sensitive data, follows a schedule, and includes regular restore testing. A backup that has never been tested should not be assumed recoverable.
