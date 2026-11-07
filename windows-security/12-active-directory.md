# 12 — Active Directory Fundamentals

## What is Active Directory?
Active Directory Domain Services (AD DS) is Microsoft's directory service for centrally managing users, computers, groups and resources in a Windows domain. It supports centralized authentication and authorization.

## Core terms
- **Domain:** an administrative identity boundary, for example corp.example.test in a private lab.
- **Domain controller:** server running AD DS that authenticates users and stores directory data.
- **Forest:** top-level AD structure that can contain one or more domains.
- **Organizational Unit:** container for organizing objects, delegating administration and linking GPOs.
- **User/computer object:** directory identity for a person or machine.
- **Security group:** identity group used to assign permissions.
- **LDAP:** protocol for accessing directory information.
- **Kerberos:** ticket-based authentication commonly used in AD.
- **DNS:** essential for locating domain services and domain controllers.

## Authentication and authorization
A domain-joined computer uses DNS to locate domain services. In a typical domain logon, Kerberos obtains tickets that can be used to access domain resources. Authorization is evaluated using the user's identity and group memberships.

## Security risks to understand defensively
Study password spraying, Kerberoasting, credential theft, excessive privileged group membership, delegation misconfiguration, weak service-account passwords and lateral movement as defensive threat themes. Focus on configuration review, monitoring and remediation. Do not test against systems without explicit authorization.

## Safe lab design
Use an isolated virtual network with one Windows Server Evaluation VM as domain controller and one Windows client VM. Use a reserved example namespace such as corp.example.test. Configure lab DNS correctly and keep the domain controller off public networks. Follow Microsoft's current AD DS deployment documentation.

## Basic lab tasks
In your own lab, create an OU, test user and security group. Add the user to the group, join the client to the lab domain and verify sign-in. Explain why an OU and a security group have different purposes.

## Check yourself
What does a domain controller do? Why is DNS important to AD? What is the difference between an OU and a security group?
