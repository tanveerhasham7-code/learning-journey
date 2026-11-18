# Lab 10 — Firewall Basics (UFW)

**Status: Completed — learner-confirmed practice (18 November 2026).**  
The learner confirmed that they practiced this lab. No screenshots or terminal output were supplied in this update; therefore, completion is recorded as learner-confirmed rather than independently verified.

## 1. Objective

Learn to inspect and manage a host firewall using UFW (Uncomplicated Firewall), understand default policies, add a narrowly scoped allow rule, enable the firewall safely, verify the active rules, and restore the original state if needed.

## 2. Safety and scope

- Use only a VM you own or are authorized to administer.
- Prefer a disposable VM with a snapshot and working hypervisor console.
- Do not perform this over an SSH-only session. Enabling a firewall with the wrong policy can disconnect you.
- Record the VM's network mode and IP address before changing anything.
- Do not copy example IP addresses blindly. Use the actual trusted lab subnet.
- If UFW is already active, inspect its rules first. Do not overwrite an existing policy without understanding it.
- Never apply these commands to a production system or a remote machine you cannot recover.

## 3. Inspect the system before changes

Run:

```bash
hostname
ip -br addr
ip route
command -v ufw
sudo ufw status verbose
sudo ufw status numbered
```

If UFW is not installed, check package availability first:

```bash
apt-cache policy ufw
```

Only on a disposable lab VM, and only if you are comfortable installing a package, install it with:

```bash
sudo apt update
sudo apt install ufw
```

Installing UFW does not require enabling it. Re-check its status after installation.

Record whether UFW was already active and preserve any existing rules. If it is active and has unfamiliar rules, stop here and review them before proceeding.

## 4. Understand the intended policy

For a simple isolated lab host, a common starting policy is:
- Deny unsolicited incoming connections by default.
- Allow outgoing connections by default.
- Add only the inbound service rules that the lab actually needs.

Do not assume SSH is required. If you administer the VM through its hypervisor console and do not need SSH, do not add an SSH allow rule.

If SSH access from a second, trusted lab VM is genuinely required, identify the target VM's actual subnet and restrict the rule to that subnet. Example only:

```bash
sudo ufw allow from 192.168.56.0/24 to any port 22 proto tcp
```

Replace `192.168.56.0/24` with the actual trusted lab subnet. Do not use this example if it does not match your topology. If SSH is not required, skip this rule.

## 5. Apply the policy carefully

On a disposable VM with console access, inspect the existing policy before changing it. If this is a fresh UFW setup with no required inbound services, set the defaults:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Add only the narrowly scoped service rule you decided was necessary in Section 4. If no inbound service is needed, add no allow rule.

Before enabling, review the planned rules:

```bash
sudo ufw show added
sudo ufw status verbose
```

If the rules look correct and you have console access plus a rollback plan, enable UFW:

```bash
sudo ufw enable
```

Confirm the prompt only after reviewing the warning and ensuring you can recover through the VM console.

## 6. Verify the active configuration

Run:

```bash
sudo ufw status verbose
sudo ufw status numbered
```

Record:
- Whether the firewall reports `Status: active`.
- Default incoming and outgoing policies.
- Each active allow/deny rule and its source/destination scope.

Inspect listening services separately:

```bash
sudo ss -tuln
```

A listening port is not proof that it is reachable from another machine; the firewall policy and network path also matter.

### Optional authorized connectivity test

Only if you have a second VM on the same isolated lab network and a service intentionally listening on the target:
1. Record the target VM's real IP and service port.
2. Test only from your own second VM.
3. Compare behavior before and after the relevant UFW rule.
4. Do not scan or test public/external systems.

If no second VM or test service is available, document rule inspection as the verification performed. Do not invent a blocked/allowed test result.

## 7. Rollback

If you lose expected connectivity or the configuration is not what you intended, use the hypervisor console. To disable UFW and restore connectivity while troubleshooting:

```bash
sudo ufw disable
sudo ufw status verbose
```

Disabling UFW removes its active filtering but does not necessarily restore any previous custom rules. If you changed an existing firewall configuration, restore it from your recorded baseline or VM snapshot.

Do not run `sudo ufw reset` unless you deliberately intend to erase all UFW rules and understand the impact.

## 8. Evidence checklist

Capture screenshots or save terminal output showing:
- VM hostname, interface address and network mode (redact public/private details before sharing where appropriate).
- UFW status before changes.
- The policy/rules you planned to add.
- UFW status after enabling.
- Numbered rules and listening sockets.
- Optional authorized connectivity test, if actually performed.
- Rollback status, if you disabled UFW again.

Never include passwords, tokens, or unrelated personal information in evidence.

## 9. Questions

1. What is UFW, and what does `ufw status verbose` show?
2. What is the effect of `default deny incoming`?
3. Why should inbound rules be limited to the required source subnet?
4. Why is enabling a firewall over an SSH-only connection risky?
5. What is the difference between a listening port and a port reachable from another machine?
6. Why is a VM snapshot or console rollback plan useful?

## 10. Completion criteria

Mark this lab **Completed** only after you:
- Inspect the baseline UFW state.
- Apply a reviewed policy on your own disposable VM.
- Enable and verify the firewall safely.
- Record actual rules and results (not expected/example output).
- Complete the questions and save sanitized evidence.
- Confirm you can still administer the VM or have successfully rolled back.

**Completion note (18 November 2026):** The learner confirmed that they practiced this lab. No screenshots or terminal output were supplied in this update, so specific UFW policies, rules, firewall status or connectivity outcomes are not claimed here. The assistant did not access or change the learner's VM.
