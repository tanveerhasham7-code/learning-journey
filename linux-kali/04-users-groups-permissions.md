# 04 — Users, Groups and Permissions

## Why accounts matter
Linux processes run with user and group identities. Separating accounts limits accidental damage and reduces the impact of a compromised account.

Important files:
- /etc/passwd: account records; normally does not contain password hashes.
- /etc/shadow: protected password hashes and password-aging data.
- /etc/group: group definitions.
- /etc/sudoers and /etc/sudoers.d/: sudo policy.

Do not edit sudo policy with a normal editor. Use visudo to validate syntax.

## Inspect identity
```bash
whoami
id
groups
getent passwd
getent group
```

## Create and manage users (Debian/Ubuntu)
```bash
sudo adduser labuser
sudo passwd labuser
sudo usermod -aG sudo labuser
id labuser
sudo deluser labuser
```
The -aG combination appends supplementary groups. Omitting -a can replace a user's supplementary group list, so take care.

## Groups
Groups make it easier to grant access to a set of users. A team may share a project directory through a dedicated group. Use groupadd, usermod -aG and getent group to manage and inspect groups.

## Permission model
Permissions apply to owner (user), group and others.
- Read (r): view file contents; for a directory, list names.
- Write (w): change a file; for a directory, create or remove entries.
- Execute (x): run a file; for a directory, traverse/search it.

Numeric values: read=4, write=2, execute=1.
- 7 = rwx
- 6 = rw-
- 5 = r-x
- 4 = r--

Example: chmod 750 script.sh means owner rwx, group r-x, others no access.

## chmod, chown and umask
```bash
chmod 640 notes.txt
chmod u+x script.sh
chmod -R 750 private-folder
sudo chown labuser:labuser notes.txt
umask
```
Use recursive permission changes carefully; they can break system directories. A common umask of 022 results in typical new file permissions of 644 and directories of 755, subject to application defaults.

## Special permissions
- SUID: executable runs with file owner's effective identity.
- SGID: executable runs with file group's effective identity; on directories, new items inherit the directory group.
- Sticky bit: on shared directories, limits who can remove/rename other users' entries (e.g. /tmp).

## sudo and least privilege
sudo allows approved users to run selected commands with elevated privileges. Prefer specific permissions over unrestricted admin access. Verify a command before running it with sudo.

## Practical lab
1. Create users analyst1 and analyst2.
2. Create group securitylab and add both users.
3. Create /srv/securitylab and assign group ownership.
4. Set permissions so group members can collaborate but other users cannot access it.
5. Log in as each user and test access.
6. Record results with ls -ld and id.
7. Remove test users after the exercise if no longer needed.

## Cybersecurity connection
Misconfigured permissions can expose sensitive files, allow unauthorized modification or enable privilege escalation. Review ownership, group membership, writable directories and unusual SUID/SGID files during defensive audits.
