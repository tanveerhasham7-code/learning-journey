# LDAP and directory queries


### 5.1 What is LDAP?

Lightweight Directory Access Protocol (LDAP) is a protocol used by clients and applications to read and, when authorized, modify directory information.

LDAP helps applications search for users, groups, computers and other directory objects. It is not itself the same as an authentication protocol, although directory operations may be part of an authentication workflow.

Common ports:

- TCP/UDP 389: LDAP (UDP is used for limited functions; most directory queries use TCP).
- TCP 636: LDAP over TLS, commonly called LDAPS.
- Global Catalog: TCP 3268; secure Global Catalog: TCP 3269.

Port use depends on configuration and the application. Do not infer that traffic is safe merely because it uses a standard port.

### 5.2 Distinguished names and search filters

An LDAP distinguished name identifies an object's location in the directory. LDAP filters select objects based on attributes.

Conceptual example:

`(&(objectCategory=person)(objectClass=user)(sAMAccountName=alex))`

This example asks for user objects whose account name is alex. It is a directory search filter, not a password or an exploit.

### 5.3 Security considerations

- Prefer encrypted directory communication where supported.
- Restrict who can read sensitive attributes and who can modify objects.
- Monitor unusual query volume or access patterns where telemetry is available.
- Investigate anonymous or unauthenticated directory access if it is not expected.
- Avoid exposing directory services directly to untrusted networks.

---
