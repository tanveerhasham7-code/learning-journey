# Knowledge check


Try to answer these in your own words before checking external notes.

1. What problem does Active Directory solve in an organization?
2. What is the difference between a domain, a forest and an OU?
3. What is the role of a domain controller?
4. How is a security group different from an OU?
5. What is the purpose of Group Policy?
6. What is the high-level difference between LDAP and Kerberos?
7. What are a TGT and a service ticket?
8. Why might an organization still have NTLM traffic?
9. Which event IDs can help investigate a successful logon and a failed logon?
10. What does Event ID 4720 indicate?
11. Why should privileged group membership changes be monitored?
12. Why is a single failed logon not enough to prove an attack?
13. What evidence would you collect after an unexpected privileged-group addition?
14. What is the difference between an alert and a confirmed incident?
15. Why should an analyst document timezone and source computer?

### Short scenario

At 02:15, a domain controller records a user being added to a sensitive administrative group. The actor is a standard account. Shortly afterward, the new member account authenticates to a server it has never used before.

Write an investigation plan:

- Identify the group-change event and its actor/member fields.
- Confirm the domain controller and timestamp.
- Check whether the change was approved.
- Review the actor's recent logons and endpoint activity.
- Review the new member's authentication and subsequent access.
- Identify affected systems and preserve evidence.
- Escalate according to the incident-response policy.

Do not assume compromise until the evidence and authorization checks support that conclusion.

---
