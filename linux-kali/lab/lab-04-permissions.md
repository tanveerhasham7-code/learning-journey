# Lab 4 — Linux File Permissions

**Status:** Reference prepared — learner execution pending  
**Environment:** Kali Linux VM (planned)  
**Execution evidence:** Not yet supplied

## Objective

Understand Linux owner, group and other permission classes by safely testing permission modes `600`, `640` and `644` on a practice file. Restore a restrictive final mode and remove the practice file.

## Safety and scope

- Work only in a dedicated directory under your home folder.
- Do not change permissions on system files or directories.
- Do not use `sudo` for this exercise.
- The commands below are a procedure for the learner to execute; they have not been run on the learner's VM by the assistant.

## Theory

Linux permission bits are grouped into three classes:

- **Owner (u):** the file's owning user.
- **Group (g):** users who belong to the file's owning group.
- **Others (o):** all other users.

Each class can receive read (`r` = 4), write (`w` = 2) and execute (`x` = 1) permissions. Numeric modes add these values for each class.

| Mode | Owner | Group | Others | Meaning |
|---|---|---|---|---|
| `600` | 6 = rw- | 0 = --- | 0 = --- | Owner can read/write; group and others have no access |
| `640` | 6 = rw- | 4 = r-- | 0 = --- | Owner can read/write; group can read; others have no access |
| `644` | 6 = rw- | 4 = r-- | 4 = r-- | Owner can read/write; group and others can read |

For a regular text file, execute permission is not needed merely to read or edit its contents.

## Procedure for the learner

### 1. Create an isolated practice file

```bash
mkdir -p ~/lab4-permissions
cd ~/lab4-permissions
printf '%s\n' 'Linux permissions practice file' > permission-test.txt
id
ls -l permission-test.txt
```

Record the current username and primary group from `id`. Confirm that the file is inside `~/lab4-permissions`.

### 2. Apply mode 600

```bash
chmod 600 permission-test.txt
stat -c '%A (%a) | Owner: %U | Group: %G | File: %n' permission-test.txt
```

Expected permission string: `-rw-------`

Interpretation: only the owner has read and write permission.

### 3. Apply mode 640

```bash
chmod 640 permission-test.txt
stat -c '%A (%a) | Owner: %U | Group: %G | File: %n' permission-test.txt
```

Expected permission string: `-rw-r-----`

Interpretation: the owner can read/write; members of the owning group can read; others have no permissions.

### 4. Apply mode 644

```bash
chmod 644 permission-test.txt
stat -c '%A (%a) | Owner: %U | Group: %G | File: %n' permission-test.txt
```

Expected permission string: `-rw-r--r--`

Interpretation: the owner can read/write; group members and others can read, but cannot write.

### 5. Verify file content and restore a restrictive mode

```bash
cat permission-test.txt
chmod 600 permission-test.txt
stat -c '%A (%a) | Owner: %U | Group: %G | File: %n' permission-test.txt
```

Expected final mode: `600` (`-rw-------`). This is a suitable restrictive mode for this simple private practice file.

### 6. Clean up

After recording the results:

```bash
rm permission-test.txt
cd ~
rmdir ~/lab4-permissions
```

The cleanup commands remove only the practice file and the empty practice directory.

## Expected observations

| Mode | Owner can read/write | Group can read | Others can read | Group/others can write |
|---|---|---|---|---|
| 600 | Yes | No | No | No |
| 640 | Yes | Yes | No | No |
| 644 | Yes | Yes | Yes | No |

These are expected permission semantics, not observations captured from the learner's VM.

## Troubleshooting

- If `chmod` reports permission denied, confirm that the file is in your own practice directory and that you own it. Do not solve this by applying `sudo` to unrelated paths.
- If `stat` is unavailable, use `ls -l permission-test.txt` to inspect the symbolic permission string.
- If the file or directory already exists, inspect it before overwriting or deleting anything.

## Security relevance

Correct file permissions help protect configuration files, scripts, logs and user data. Mode `600` is useful for private files; `640` can support controlled group reading; `644` makes a file readable by all local users. Choose the least permissive mode that still supports the required task.

## Evidence checklist

- [ ] Screenshot or sanitized terminal transcript showing mode 600.
- [ ] Screenshot or sanitized terminal transcript showing mode 640.
- [ ] Screenshot or sanitized terminal transcript showing mode 644.
- [ ] Final verification showing mode 600 restored.
- [ ] Practice file and directory cleaned up.

## Completion criteria

Mark this lab **Completed** only after the learner executes the procedure, checks the actual permission output, restores mode `600`, cleans up the practice directory and supplies the evidence or confirms the observed results. Until then, this document is a prepared reference, not proof of execution.
