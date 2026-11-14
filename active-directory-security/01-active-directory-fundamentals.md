# Active Directory fundamentals and architecture


### 1.1 What is Active Directory?

Active Directory (AD) is Microsoft's directory service used by many organizations to centrally manage identities and resources in a Windows environment. It stores information about objects such as users, computers, groups and services. It also supports authentication and access-control decisions.

Imagine a university with hundreds of students, teachers, computers and shared folders. Without centralized identity management, each computer might need separate local accounts. Managing access and disabling a former employee's access would become difficult. A domain directory gives administrators a central place to manage identities and many security settings.

**Important distinction:** Active Directory is not the same thing as Microsoft Entra ID (formerly Azure Active Directory). Traditional AD DS is commonly deployed on Windows Server and uses domain controllers. Microsoft Entra ID is Microsoft's cloud identity service. Hybrid organizations may use both.

### 1.2 Why SOC analysts need to understand AD

A compromised identity can be used to access email, file shares, servers, business applications and administrative tools. Many serious incidents involve misuse of legitimate accounts rather than an obvious malware alert.

A SOC analyst therefore asks:

- Which identity authenticated?
- From which device and source address?
- At what time?
- Was the logon successful or unsuccessful?
- Which service or resource was accessed?
- Was the account privileged?
- Did the account's permissions or group memberships change?
- Does the activity match the user's normal role and behavior?

### 1.3 Logical structure

- **Object:** A directory entry, such as a user, computer, group or printer.
- **Domain:** An administrative and replication boundary containing directory objects.
- **Tree:** One or more domains in a contiguous DNS namespace.
- **Forest:** The top-level AD logical structure. A forest can contain one or more domain trees and shares a schema, configuration and global catalog.
- **Schema:** Defines the types of objects and attributes that can exist in the directory.
- **Global Catalog (GC):** Helps users and applications search for directory information across a forest. It holds a partial, searchable replica of objects from the forest.
- **Site:** Represents the physical network structure used to optimize replication and client access.

A small organization may use one domain in one forest. A large organization may use multiple domains and sites. More domains do not automatically mean better security; design should follow operational and security requirements.

### 1.4 Naming examples

A domain might be named `corp.example.test`. A user could have a User Principal Name (UPN) such as `alex@corp.example.test` and a distinguished name (DN) such as:

`CN=Alex Khan,OU=Finance,DC=corp,DC=example,DC=test`

The DN describes the object's path in the directory. The UPN is a logon-style name that resembles an email address, but it is not necessarily a working email address.

---
