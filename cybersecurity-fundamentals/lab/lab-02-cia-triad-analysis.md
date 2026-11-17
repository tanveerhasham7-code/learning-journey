# Practical 02 — CIA Triad Analysis

## Objective
Identify which part of the CIA Triad is affected in four fictional security scenarios and explain why.

## Concepts
- **Confidentiality:** Information is accessible only to authorized people.
- **Integrity:** Information remains accurate and is protected from unauthorized changes.
- **Availability:** Systems and information are accessible to authorized users when needed.

## Scenario analysis

### Scenario 1 — Unauthorized access to a private file
**Affected principle:** Confidentiality

**Reason:** An unauthorized person read a private file without permission. The information was exposed to someone who was not allowed to access it.

### Scenario 2 — Unauthorized change to a bank account number
**Affected principle:** Integrity

**Reason:** An attacker changed the account number from `123456` to `987654` without authorization. This makes the stored information inaccurate and untrustworthy.

### Scenario 3 — Company server becomes unavailable
**Affected principle:** Availability

**Reason:** The server went offline after an attack, so employees and customers could not access the system when they needed it.

### Scenario 4 — Downloaded installer has a different SHA-256 hash
**Affected principle:** Integrity

**Reason:** The downloaded installer's hash did not match the official reference hash. This indicates that the file may have changed or become corrupted. The reference hash must come from a trusted official source for this comparison to be meaningful.

## Results summary

| Scenario | Main CIA principle | Key reason |
|---|---|---|
| Unauthorized reading of a private file | Confidentiality | Information was viewed without permission |
| Bank account number changed without permission | Integrity | Data was modified without authorization |
| Server outage | Availability | Authorized users could not access the service |
| Installer hash differs from trusted official hash | Integrity | File contents may have changed |

## Completion and evidence note
All four scenario questions were answered correctly during the learning exercise. This report records the answers and reasoning. No screenshots were taken or uploaded, as requested; therefore, this practical has written-answer documentation only and no screenshot evidence.

## Key learning
The CIA Triad helps identify the security property affected by an incident:
- Unauthorized disclosure → **Confidentiality**
- Unauthorized or unexpected modification → **Integrity**
- Disruption that prevents access → **Availability**

