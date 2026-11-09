# 13 — Backup, Business Continuity and Disaster Recovery

Business continuity helps an organization continue essential operations during disruption. Disaster recovery focuses on restoring IT systems, applications, and data.

## RPO and RTO
- Recovery Point Objective (RPO): maximum acceptable data loss measured in time. A four-hour RPO means the target restore point is no more than four hours before disruption.
- Recovery Time Objective (RTO): target time to restore a service. An eight-hour RTO means the service target is restoration within eight hours.

These are business-approved targets, not guarantees.

## Backup types
Full backups copy selected data. Incremental backups copy changes since the previous backup. Differential backups copy changes since the last full backup. Protect backups from unauthorized access and ransomware, and test restoration regularly. An untested backup is not proven reliable.

## Practical
Create a backup plan for non-sensitive study files. Define location, frequency, access protection, and a restore test. Record the actual result; do not upload private files.
