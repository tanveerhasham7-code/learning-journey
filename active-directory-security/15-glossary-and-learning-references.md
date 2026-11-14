# Glossary and learning references


### Essential glossary

- **AD DS:** Active Directory Domain Services.
- **DC:** Domain Controller.
- **OU:** Organizational Unit.
- **GPO:** Group Policy Object.
- **LDAP:** Lightweight Directory Access Protocol.
- **LDAPS:** LDAP protected with TLS.
- **KDC:** Key Distribution Center.
- **TGT:** Ticket-Granting Ticket.
- **TGS:** Ticket-Granting Service.
- **SPN:** Service Principal Name.
- **UPN:** User Principal Name.
- **DN:** Distinguished Name.
- **SID:** Security Identifier.
- **SYSVOL:** Domain share used for policy and script distribution.
- **FSMO:** Flexible Single Master Operations.
- **SIEM:** Security Information and Event Management.
- **EDR:** Endpoint Detection and Response.
- **Baseline:** A documented picture of normal activity used for comparison.
- **False positive:** An alert that fires on activity that is not actually malicious.

### Authoritative learning references

Use current vendor documentation because product behavior and security recommendations can change.

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Active Directory documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/)
- [Microsoft Learn — Windows security auditing](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-policy-recommendations)
- [Microsoft Learn — Advanced security audit policy settings](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-audit-policy-settings)
- [Microsoft Learn — Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [Microsoft Learn — LDAP signing](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
- [Microsoft Learn — Group Policy overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview)
- [MITRE ATT&CK — Enterprise techniques](https://attack.mitre.org/)

---

## Completion checklist

- [ ] I can explain AD DS architecture without reading the notes.
- [ ] I can distinguish a domain, forest, OU and security group.
- [ ] I can explain the basic Kerberos ticket flow.
- [ ] I understand where LDAP and NTLM fit.
- [ ] I can identify the purpose of the key Windows event IDs in this module.
- [ ] I can investigate a privileged group change using actor, target and host context.
- [ ] I can describe at least three AD threat patterns and their defensive indicators.
- [ ] I have completed practical exercises and uploaded sanitized evidence to the companion project.
- [ ] I can explain one detection rule, its logic, limitations and triage steps.

**Portfolio status:** Theory module published. Practical completion remains dependent on your own lab work and evidence.
