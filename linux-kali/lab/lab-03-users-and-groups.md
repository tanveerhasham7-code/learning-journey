# Lab 3 — Users and Groups

**Status:** Completed  
**Environment:** Kali Linux VM  
**Date:** 18 November 2026

## Objective

Create temporary test users and a shared group, configure a group-owned directory with least-privilege access, verify that both group members can create files, inspect ownership, and clean up the test accounts and resources.

## Procedure and commands

### 1. Inspect the current account and existing users

```bash
whoami
id
cut -d: -f1 /etc/passwd
```

The learner confirmed running these commands to inspect the current identity and local account list.

### 2. Create a group and two test users

```bash
sudo groupadd labgroup
getent group labgroup

sudo useradd -m labuser1
sudo useradd -m labuser2
getent passwd labuser1
getent passwd labuser2
```

The group and both temporary user accounts were created.

### 3. Add both users to the shared group

```bash
sudo usermod -aG labgroup labuser1
sudo usermod -aG labgroup labuser2
groups labuser1
groups labuser2
```

The learner confirmed both users were listed as members of `labgroup`. The `-aG` options append the supplementary group without replacing existing supplementary memberships.

### 4. Create and configure the shared directory

```bash
sudo mkdir /shared-lab
sudo chown :labgroup /shared-lab
sudo chmod 2770 /shared-lab
ls -ld /shared-lab
```

The directory was assigned to group `labgroup` and configured with mode `2770`.

- Owner permissions: read, write and execute.
- Group permissions: read, write and execute.
- Other-user permissions: none.
- Setgid bit: new files and subdirectories inherit the directory's group.

The expected directory permission display is `drwxrws---`.

### 5. Test directory access as both users

```bash
sudo -u labuser1 touch /shared-lab/user1-file.txt
sudo -u labuser2 touch /shared-lab/user2-file.txt
ls -l /shared-lab
```

Both file-creation commands completed successfully. Because the directory grants access to its owner and group but no access to others, successful creation by both test users demonstrates that both could use the shared directory.

### 6. Inspect ownership and test reading a file

```bash
stat -c '%n | Owner: %U | Group: %G | Permissions: %A' /shared-lab/*
sudo -u labuser2 sh -c 'echo "Shared group access test" > /shared-lab/user2-file.txt'
sudo -u labuser1 cat /shared-lab/user2-file.txt
```

The learner confirmed the ownership-inspection command and successful display of the test text when reading as `labuser1`.

**Evidence limitation:** The exact permission bits reported by `stat` were not retained in the conversation. Therefore, the successful read proves that the file was readable by `labuser1`, but does not by itself prove that read access was granted specifically by the group rather than by an "other" permission bit. The shared-directory file-creation test is the stronger confirmation of group-based directory access.

### 7. Final verification and cleanup

The learner confirmed running the final checks:

```bash
getent group labgroup
groups labuser1
groups labuser2
ls -ld /shared-lab
ls -l /shared-lab
```

After verification, temporary resources were removed:

```bash
sudo rm -r /shared-lab
sudo userdel -r labuser1
sudo userdel -r labuser2
sudo groupdel labgroup
```

The learner confirmed each cleanup step. The temporary shared directory, test users and test group were removed.

## Key concepts learned

1. `/etc/passwd` contains local account records; `getent` queries account and group databases.
2. `useradd -m` creates a user and its home directory.
3. `groupadd` creates a group.
4. `usermod -aG` adds a supplementary group membership.
5. `chown :group` changes a directory's group owner.
6. `chmod 2770` applies owner/group access, denies access to others, and enables setgid group inheritance on the directory.
7. `stat` displays ownership and permission metadata.
8. Temporary test accounts and resources should be removed when the exercise is finished.

## Security lesson

Use groups to grant shared access to only the people who need it. Avoid giving access to "others" when a controlled group is sufficient. The setgid bit on a shared directory helps keep new items associated with the intended group. Always verify actual file permission bits before concluding that a cross-user read was allowed specifically through group permissions.

## Evidence and limitations

The learner confirmed completion of the commands and checks step by step. No screenshots or saved terminal transcript were supplied for this lab, so this report records learner-confirmed execution and the known results without claiming independent screenshot verification.

## Completion

The users-and-groups exercise was completed and the temporary test accounts, group and shared directory were cleaned up. No permanent user accounts or system security settings were intentionally changed.
