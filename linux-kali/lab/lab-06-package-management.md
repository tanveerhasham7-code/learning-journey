# Linux Lab 6 — Package Management with APT

**Status: Reference prepared — learner execution and evidence pending.**

## 1. Objective

Learn how Kali Linux uses APT to refresh package metadata, inspect a package, install software, verify installation and remove the test package safely.

Use your own Kali Linux VM. Package operations may require internet access and administrator privileges.

## 2. Understand APT update vs upgrade

- `sudo apt update` downloads refreshed package information from configured repositories. It does **not** install package upgrades.
- `sudo apt upgrade` installs available upgrades for installed packages, subject to APT's upgrade rules. It changes installed software and may take time.

For this lab, we will refresh package metadata but will **not** run a full system upgrade.

## 3. Refresh package metadata

Run:

```bash
sudo apt update
```

Enter your Kali password if prompted. Linux does not display password characters while you type; this is normal.

Wait for the command to finish. Record whether it completed successfully or showed repository/network/signature errors. Do not proceed as though it succeeded if it reported errors.

## 4. Inspect the test package

We will use `tree`, a small command-line utility that displays directory contents as a tree.

Run:

```bash
apt show tree
```

Review the package description, version, and installation size. The exact version and size can change.

## 5. Install the package

Run:

```bash
sudo apt install tree
```

Read the confirmation prompt. If APT proposes installing the `tree` package and its required dependencies, enter `Y` to continue. If it proposes unexpected removals or unrelated changes, stop and review rather than accepting.

## 6. Verify installation

Run:

```bash
tree --version
command -v tree
dpkg -s tree | grep -E '^(Status|Version):'
```

Check that the command exists and that package status reports it is installed. Record the actual version shown.

## 7. Remove the test package

Run:

```bash
sudo apt remove tree
```

Review the proposed changes before confirming with `Y`. This removes the package but may leave configuration files behind.

Verify removal:

```bash
dpkg -s tree
command -v tree
```

A package-not-installed message and no command path are expected after successful removal. If APT reports that the package is not installed, record that actual result.

Do not run `apt autoremove` as part of this lab; it is unnecessary for the basic exercise and may propose removing other packages.

## 8. Questions to answer

1. What does `apt update` refresh?
2. Does `apt update` itself upgrade installed software?
3. What does `apt upgrade` do?
4. Which command did you use to install `tree`?
5. How did you verify that `tree` was installed?
6. What did APT report when you removed it?

## 9. Evidence checklist

Save screenshots or a terminal transcript showing:
- [ ] Successful or failed result of `sudo apt update`.
- [ ] Package details from `apt show tree`.
- [ ] Installation result from `sudo apt install tree`.
- [ ] Verification output from `tree --version` and package status.
- [ ] Removal result and verification after removal.

Review evidence for private information before uploading it publicly.

## 10. Completion criteria

Mark this lab **Completed** only after the learner has:
1. Refreshed package metadata and recorded the actual result.
2. Inspected the `tree` package.
3. Installed and verified the package.
4. Removed it and checked the resulting state.
5. Answered the APT update/upgrade questions.
6. Saved evidence or explicitly confirmed the observed results.

**Current result:** This is a prepared procedure. No APT commands have been executed on the learner's Kali VM by the assistant; package versions, installation state and command results have not been observed.
