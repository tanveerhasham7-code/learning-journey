# Practical 06 — SHA-256 File Integrity Check

**Status:** Completed — learner-reported test results  
**Environment:** Windows 11 PowerShell (user-reported environment)  
**Target:** Harmless text file created on the learner's Desktop  
**Privacy:** No personal file contents, account names, or hashes were published.

## Objective

Use SHA-256 to calculate a file's cryptographic digest, modify the file, and compare the new digest with the original.

## Procedure

1. Created a test file named `hash-test.txt` on the Desktop with the initial text:
   `Cybersecurity Lab 06 - Original File`
2. Calculated the original digest using PowerShell:
   ```powershell
   Get-FileHash "$env:USERPROFILE\Desktop\hash-test.txt" -Algorithm SHA256
   ```
3. Replaced the file content with:
   `Cybersecurity Lab 06 - Modified File`
4. Calculated the SHA-256 digest again using the same command.
5. Compared the original and modified digests.

## Result

The learner reported that the two SHA-256 hash values were **different** after the file content was modified.

This is the expected result. A cryptographic hash produces a fixed-length digest for the input. Even a small content change normally produces a very different digest (the avalanche effect).

## Security concepts demonstrated

- A hash can help detect whether file content has changed.
- SHA-256 is a one-way cryptographic hash function; it is not encryption and cannot be reversed to recover the original file.
- A hash is useful for integrity checking when compared against a trusted reference hash.
- A hash alone does not prove who created a file or that the file is safe. An attacker who can replace both a file and its reference hash may defeat a simple comparison.

## Limitations and evidence

The learner uploaded one screenshot as supporting evidence. It is embedded below. The exact hash strings are not transcribed into this report; the result remains recorded as learner-reported. The test used a harmless text file; no sensitive files were used.

### Screenshot evidence

![Practical 06 — SHA-256 integrity check](screenshort/lab6/Screenshot%202026-11-17%20144915.png)

*Figure 1: Screenshot uploaded by the learner for the SHA-256 integrity practical.*

## Conclusion

**Practical 06 is completed** based on the learner-reported successful comparison. The experiment demonstrated that changing file content changes its SHA-256 digest, making hashes useful for integrity verification.
