# Active Directory Security for SOC Analysts

**Level:** Beginner to Intermediate  
**Track:** SOC Analyst / Blue Team  
**Purpose:** Learn Active Directory identity services, authentication, Windows security telemetry, detection engineering and SOC investigation step by step.

This module follows the same individual-topic notebook structure as the other learning sections in this repository. Study the topics in order. The companion practical project is in the Projects repository:

[Active Directory SOC Monitoring Lab](https://github.com/tanveerhasham7-code/projects-/tree/main/active-directory-soc-monitoring-lab)

## Step-by-step topics

1. [Active Directory fundamentals and architecture](01-active-directory-fundamentals.md)
   - AD DS purpose, architecture, domains, forests, trees, schema, global catalog and naming.
2. [Domain controllers and AD DS components](02-domain-controllers-and-ad-ds.md)
   - Domain controllers, NTDS.dit, SYSVOL, DNS, replication and FSMO roles.
3. [Users, groups, computers and organizational units](03-users-groups-and-organizational-units.md)
   - User and computer accounts, security groups, group scopes, OUs and SOC use cases.
4. [Group Policy](04-group-policy.md)
   - Group Policy objects, processing order, security configuration and monitoring.
5. [LDAP and directory queries](05-ldap-and-directory-queries.md)
   - LDAP purpose, ports, distinguished names, search filters and defensive controls.
6. [Kerberos authentication](06-kerberos-authentication.md)
   - Kerberos flow, KDC, TGT, service tickets, SPNs and SOC indicators.
7. [NTLM authentication](07-ntlm-authentication.md)
   - NTLM challenge-response, legacy dependencies and defensive monitoring.
8. [Windows domain security events](08-windows-domain-security-events.md)
   - Windows Security event IDs, logon types, key fields and audit prerequisites.
9. [Privileged identities and access monitoring](09-privileged-identities-and-access-monitoring.md)
   - Privileged accounts, least privilege, defensive controls and monitoring checklist.
10. [Common Active Directory threat patterns](10-common-active-directory-threat-patterns.md)
   - Password spraying, brute force, Kerberoasting, AS-REP roasting, credential replay, DCSync, ticket abuse, GPO abuse and lateral movement.
11. [Detection engineering for Active Directory](11-detection-engineering.md)
   - Detection lifecycle, hypotheses, examples, triage logic and quality checklist.
12. [SOC investigation workflow and response](12-soc-investigation-and-response.md)
   - Alert triage, evidence handling, response options and case closure.
13. [Practical lab plan](13-practical-lab-plan.md)
   - Proposed isolated lab components, safety rules, planned exercises and evidence standards.
14. [Knowledge check](14-knowledge-check.md)
   - Fifteen review questions and a SOC investigation scenario.
15. [Glossary and learning references](15-glossary-and-learning-references.md)
   - Essential AD/SOC glossary and authoritative learning links.

## How to study this module

1. Study one topic at a time in the listed order.
2. Write short notes in your own words.
3. Complete the matching practical exercise in the companion project when ready.
4. Save sanitized screenshots, event exports and investigation notes.
5. Mark a practical task verified only after you have performed it and checked the evidence.

**Portfolio status:** Individual theory topic files are published. Practical exercises remain pending until you complete them and upload real evidence.
