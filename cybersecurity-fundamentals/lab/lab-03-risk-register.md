# Practical 03 — Risk Register (Initial Asset Assessment)

## Objective
Begin a risk register by identifying a system asset, reviewing observable security controls, and recording realistic threats without inventing unverified vulnerabilities.

## Assessment scope
- **Asset assessed:** Personal laptop
- **Operating system:** Windows 11 Pro, Version 26H2 (as reported by the user)
- **Assessment type:** Basic, non-invasive configuration review
- **Evidence:** User-reported observations during the guided checks; no screenshots were requested or collected.

## Asset 1 — Windows 11 Pro Laptop

### Observed security controls

| Check | User-reported result |
|---|---|
| Windows Update | Up to date |
| Windows Security — Virus & threat protection | No current threats |
| Microsoft Defender real-time protection | On |
| Domain network firewall profile | On |
| Private network firewall profile | On |
| Public network firewall profile | On |

### Preliminary risk register

| Field | Assessment |
|---|---|
| Asset | Windows 11 Pro laptop |
| Threat | Malware or ransomware could attempt to compromise the device or its data |
| Vulnerability / weakness | No specific vulnerability was confirmed during these checks |
| Likelihood | Not rated yet; more information is needed |
| Impact | Potentially High because compromise could affect personal files, study work, and device availability |
| Existing controls | Windows Update reported up to date; Defender reported no current threats; real-time protection on; all three firewall profiles on |
| Proposed treatment | Keep Windows and security definitions updated; leave real-time protection and firewall enabled; review backups and account security in later checks |
| Owner | Device owner |

## Findings and limitations
- The checks indicate that several important built-in protections are enabled.
- “No current threats” means Windows Security did not report a current detected threat at the time of the check. It does not prove that the device is completely free of malware.
- An up-to-date Windows Update screen does not, by itself, prove that every application and driver is fully patched.
- Firewall profiles being on does not establish that every individual firewall rule is correctly configured.
- No confirmed vulnerability was found in this initial review. A possible threat must not be recorded as a confirmed weakness.
- Likelihood remains unrated because there is not enough evidence to make a defensible estimate.

## Status
**In progress — initial assessment of one asset documented.** The practical asks for a risk register covering three assets. Only Asset 1 has been assessed so far; the overall practical is not marked complete.

## Next work
Continue the risk register with additional assets, then review likelihood, impact, controls, and treatment consistently across all three assets.
