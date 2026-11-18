# Linux Lab 9 — Authentication Log Analysis

**Status: Reference prepared — learner execution and evidence pending.**

## 1. Objective

Learn how Linux records authentication activity and how to review those records for:
- Failed login attempts
- Successful login attempts
- Event timestamps
- Usernames
- Source addresses, when recorded

Use only your own Kali/Ubuntu VM or a lab VM you are authorized to administer. This exercise is for log review, not password guessing or testing external systems.

## 2. Important safety notes

- Do not run password-guessing tools or repeated login attempts.
- Do not test public IP addresses or third-party systems.
- Do not change SSH authentication settings just to make this lab work.
- Keep a VM console session open if you are working with SSH.
- A missing log file or missing event is not proof of a security problem; logging configuration differs between systems.

## 3. Identify the operating system and SSH service

Run:

```bash
cat /etc/os-release
```

Check whether the SSH service is installed/running. Depending on the distribution, the service may be named `ssh` or `sshd`:

```bash
systemctl status ssh --no-pager
systemctl status sshd --no-pager
```

One of these may report that the unit does not exist. That is okay. Do not install or enable SSH just for this lab unless you understand the change and have a safe VM snapshot/console recovery path.

## 4. Inspect authentication events with the system journal

On systems using systemd, try:

```bash
sudo journalctl --since "today" --no-pager | grep -Ei 'sshd|ssh|authentication|failed password|accepted'
```

If the SSH service is known to be named `ssh`, you can also try:

```bash
sudo journalctl -u ssh --since "today" --no-pager
```

If the service is named `sshd`, try:

```bash
sudo journalctl -u sshd --since "today" --no-pager
```

If no matching events appear, record that honestly. The service may not be installed, may not have run today, or the system may use a different logging configuration.

## 5. Inspect traditional authentication log files (if present)

Debian-based systems may store authentication events in `/var/log/auth.log`. Check whether it exists:

```bash
ls -l /var/log/auth.log
```

If it exists, search for common SSH success/failure messages:

```bash
sudo grep -Ei 'failed password|accepted password|accepted publickey|invalid user' /var/log/auth.log
```

For rotated/compressed logs, do not assume today's events are in an older file. You can inspect filenames with:

```bash
ls -lh /var/log/auth.log*
```

If `auth.log` is absent, use the journal commands above. Do not create a fake log or claim events occurred when they did not.

## 6. Optional controlled event generation (only on your own lab VM)

Only do this if SSH is already configured and you have console access or another safe way to recover. Do not change SSH configuration for this exercise.

1. Open a terminal on the VM itself and keep it available.
2. Confirm the VM's own address with `ip -br addr`.
3. From a second terminal on that same VM, make one login attempt to its own SSH service using a deliberately incorrect password for your own existing test account, if password authentication is already enabled.
4. Stop after one failed attempt. Do not repeat attempts.
5. If you already have a legitimate successful SSH login to compare, inspect that event too. Do not weaken authentication or enable password login just to produce a success event.

If SSH is not running, password authentication is disabled, or you do not have a safe test account, skip this section. Analyze existing events or use the sample interpretation exercise below.

## 7. How to read common SSH log messages

Exact wording varies by OpenSSH version and distribution.

- `Failed password for <user> from <address> port <number> ssh2`: an authentication attempt using a password failed. The username and source address may be shown.
- `Accepted password for <user> from <address> ...`: password authentication succeeded.
- `Accepted publickey for <user> from <address> ...`: public-key authentication succeeded.
- `Invalid user <user> from <address> ...`: an attempt used a username that the system does not recognize.
- `Connection closed` or `Disconnected`: a connection ended; by itself, it does not prove a login succeeded or failed.

A failed attempt is not automatically an attack. It could be a mistyped password or an expected test. Consider the account, source, timing, frequency and surrounding events before drawing conclusions.

## 8. Record your findings

Use this table in your report (fill it with actual observed events only):

| Timestamp | Username | Source address | Event | Result |
|---|---|---|---|---|
| Actual value | Actual value | Actual value or Not recorded | Exact message summary | Failed / Successful / Other |

If there are no events, write: **No matching authentication events found in the inspected log source and time range.** Record which commands and time range you checked.

## 9. Sample interpretation exercise (fictional examples only)

These examples are invented for learning and are not output from your VM:

```text
Nov 18 10:15:02 lab-vm sshd[1200]: Failed password for student from 192.0.2.25 port 51000 ssh2
Nov 18 10:17:41 lab-vm sshd[1215]: Accepted publickey for student from 192.0.2.25 port 51022 ssh2
```

Interpretation:
- First event: a password login for `student` failed. The recorded source is `192.0.2.25`.
- Second event: public-key authentication for `student` succeeded from the same example source.
- These two sample lines alone do not establish malicious activity. Context and authorization matter.

The address `192.0.2.25` is reserved for documentation examples; it is not a real attacker address.

## 10. Evidence checklist

Save sanitized screenshots or a terminal transcript showing:
- [ ] OS identification and SSH service status.
- [ ] Journal query and/or authentication log file check.
- [ ] Actual event lines, with private details redacted where needed, or a clear record that no matching events were found.
- [ ] Your findings table and short interpretation.

Never publish usernames, IP addresses, hostnames or other details that you do not want public. Do not upload raw authentication logs to a public repository.

## 11. Review questions

1. What is the purpose of an authentication log?
2. What is the difference between `Failed password` and `Accepted publickey`?
3. Which details can help an analyst investigate a login event?
4. Why is one failed login not enough to conclude that an attack occurred?
5. Why should raw authentication logs be sanitized before public sharing?

## 12. Completion criteria

Mark this lab **Completed** only after the learner has:
1. Checked the VM's SSH service and identified an available log source.
2. Queried the journal and/or authentication log file.
3. Recorded actual findings, including an honest "no matching events" result if applicable.
4. Explained the difference between failed and successful authentication events.
5. Saved sanitized evidence and answered the review questions.

**Current result:** This procedure and fictional interpretation example are prepared. The assistant has not accessed or inspected the learner's VM logs, generated SSH login events, or verified any actual authentication activity.
