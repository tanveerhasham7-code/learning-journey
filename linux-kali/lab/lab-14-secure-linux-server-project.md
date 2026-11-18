# Lab 14 — Final Project: Secure a Linux Server

**Status: Project blueprint prepared — implementation and evidence pending.**  
This guide is a structured capstone for a learner-owned Ubuntu Server VM. It provides a safe sequence, commands, report requirements and validation criteria. The assistant has not accessed or modified the learner's VMs, run scans, changed firewall/SSH settings, or generated real findings. All results must come from the learner's own lab.

## 1. Scenario and objective

You are responsible for a small Ubuntu server used by a fictional organization. Your task is to establish a baseline, review its security, apply carefully selected hardening measures, and verify the results.

The project combines Linux administration, networking, account security, permissions, services, firewall rules, SSH, logs, Nmap and evidence-based reporting.

## 2. Scope, authorization and safety rules

- Use only an Ubuntu VM that you own or are explicitly authorized to administer, plus your own Kali VM.
- Keep both VMs on an isolated VMware Host-only or Internal network. Do not expose the lab server to the public internet.
- Record the actual network mode and IP addresses; example addresses in this guide are placeholders.
- Take a VMware snapshot before changing accounts, SSH or firewall settings.
- Keep console access to Ubuntu available throughout the project. Do not rely only on SSH while changing firewall or SSH settings.
- Do not scan or test any third-party system.
- Do not disable services or change security settings without understanding their purpose and having a rollback plan.
- Do not publish passwords, private keys, tokens, personal data, or unredacted sensitive logs/screenshots.

## 3. Project architecture and IP plan

Use two VMs:
- Ubuntu Server: the system being secured.
- Kali Linux: the authorized assessment workstation.

On each VM, run:

```bash
hostname
ip -br addr
ip route
```

Record the actual interface, IP address, subnet and gateway (if any). Confirm both VMs share the intended isolated virtual network. Draw a simple diagram showing Kali, Ubuntu, their interface names, IP addresses and virtual network type.

Do not assign an example IP blindly. If static addresses are needed, first inspect the VMware host-only subnet and DHCP range to avoid conflicts.

## 4. Establish the baseline inventory

On Ubuntu, collect:

```bash
cat /etc/os-release
uname -r
hostnamectl
whoami
id
uptime
free -h
df -h
ip -br addr
ip route
```

Record:
- Distribution and release.
- Kernel version and architecture.
- Hostname and current account.
- Uptime and resource/storage summary.
- Network interfaces and routes.

Inventory installed packages using the package manager:

```bash
apt list --installed
```

For a more compact report, save the output locally and summarize relevant security and server packages. Do not upload an unnecessarily large package dump or private machine details.

## 5. Accounts and least privilege review

Inspect local accounts and groups:

```bash
getent passwd
getent group
id
getent group sudo
```

Review which human accounts can administer the server. Explain the difference between a normal user and a user with sudo privileges.

If the VM has only a default lab account, do not create or remove accounts just to make the report look complete. If you do need a separate administrator account for the exercise:
1. Confirm console access and take a snapshot.
2. Create a named account using `sudo adduser <ADMIN_USER>`.
3. Grant sudo only if required using `sudo usermod -aG sudo <ADMIN_USER>`.
4. Verify membership with `id <ADMIN_USER>`.
5. Test the account from a separate session before changing or removing any existing administrator access.

Never share passwords in the report. Remove temporary accounts only after confirming they are no longer needed.

## 6. Project directory permissions review

Create a harmless project directory for the exercise:

```bash
sudo mkdir -p /srv/secure-lab
sudo chown root:root /srv/secure-lab
sudo chmod 750 /srv/secure-lab
ls -ld /srv/secure-lab
stat /srv/secure-lab
```

Explain owner, group and others permissions. Mode `750` gives the owner read/write/execute, the group read/execute, and others no access. Use an appropriate owner/group for the fictional workload; do not apply this example mode blindly to system directories.

Record the actual owner, group and permission bits. If you create test files, use harmless content and remove them when finished.

## 7. Running services and listening ports

On Ubuntu, inspect listening sockets and active services:

```bash
sudo ss -tulpen
systemctl list-units --type=service --state=running --no-pager
```

For each relevant listener, identify the port, protocol, process/service and whether the organization needs it. Inspect a service with:

```bash
systemctl status <SERVICE_NAME> --no-pager
```

Do not stop or disable a service until you know its role and have confirmed it is not needed. Record unknown services as requiring investigation rather than assuming they are malicious.

## 8. Firewall policy and verification

First inspect the current firewall state:

```bash
sudo ufw status verbose
```

If UFW is not installed or active, document that fact before deciding whether to configure it. Before enabling a firewall:
- Confirm VMware console access works.
- Identify every service you need for the lab.
- If SSH administration is required, create a narrowly scoped allow rule for the trusted Kali lab IP before enabling UFW.
- Do not use a broad allow rule unless the lab requires it and the risk is understood.

Example only — replace placeholders with the actual lab values:

```bash
sudo ufw allow from <KALI_IP> to any port 22 proto tcp
sudo ufw status numbered
```

If you decide to enable UFW, do so only from the Ubuntu console after reviewing the rules:

```bash
sudo ufw enable
sudo ufw status verbose
```

Verify required connectivity from Kali and verify the active rules on Ubuntu. If anything breaks, use the VM console and your documented rollback plan. Do not run `ufw reset` as a routine troubleshooting step.

## 9. SSH configuration review and safe validation

Check whether SSH is installed and active:

```bash
systemctl status ssh --no-pager
sudo ss -tlnp
```

If SSH is not installed, record that; do not install it unless remote administration is an explicit project requirement.

If SSH is in use, inspect effective settings:

```bash
sudo sshd -t
sudo sshd -T
```

Review relevant settings such as password authentication, root login, allowed users and listening port. Do not copy a hardening configuration without understanding how it affects your access.

Before editing:
1. Take a VM snapshot and confirm console access.
2. Back up the configuration file.
3. Make one change at a time.
4. Validate syntax with `sudo sshd -t`.
5. Reload the service only if validation succeeds.
6. Test a new SSH session before closing the existing working session.

Do not disable password authentication until key-based login has been configured and successfully tested. Do not lock yourself out to satisfy a checklist.

## 10. Authentication and system log review

Inspect available logs:

```bash
sudo journalctl -p warning..alert --since "24 hours ago" --no-pager
sudo journalctl -u ssh --since "24 hours ago" --no-pager
```

On systems where it exists, you may also inspect:

```bash
sudo test -f /var/log/auth.log && sudo tail -n 100 /var/log/auth.log
```

Look for authentication failures, successful logins, unexpected service errors and repeated events. Record timestamps, event type and relevant context. Do not publish usernames, public IPs or other sensitive values unnecessarily. A lack of events in a short time window is not proof that the server is secure.

## 11. Authorized Nmap inventory from Kali

Confirm Ubuntu's actual IP from its console. From Kali, verify the target is your own Ubuntu VM and run only single-host scans:

```bash
ping -c 4 <UBUNTU_IP>
nmap -sn <UBUNTU_IP>
nmap -sV <UBUNTU_IP>
```

Record open/closed/filtered TCP ports and service/version guesses. Nmap version detection is best-effort and should be verified against Ubuntu's local `sudo ss -tulpen` and service status. Do not scan broad networks, public addresses, or use aggressive scripts for this capstone.

Compare Nmap results with the Ubuntu listening-socket inventory. Explain any differences, such as firewall filtering or services bound only to localhost.

## 12. Findings, risk and remediation plan

Create a findings register based only on evidence you collected:

| ID | Evidence-based finding | Asset | Likelihood | Impact | Risk | Recommended action |
|---|---|---|---|---|---|---|
| F-01 | Actual observation | Ubuntu server | Low/Medium/High or Unknown | Low/Medium/High | Justified rating | Practical remediation |

Do not invent vulnerabilities. If no weakness is confirmed, record an observation or an item needing further investigation. Explain how you assessed likelihood and impact. Prioritize fixes that reduce exposure without breaking required operations.

For each remediation, record:
- What was changed and why.
- The exact command/configuration change (excluding secrets).
- The expected security benefit.
- Possible operational impact.
- Rollback method.

## 13. Before-and-after retesting

Repeat the relevant baseline checks after changes:
- Account and sudo membership review.
- Directory permission check with `ls -ld` / `stat`.
- Active services and listening sockets.
- UFW status and rules.
- SSH syntax/effective configuration and a safe connection test, if SSH is used.
- Relevant log review.
- Same authorized single-host Nmap scan from Kali.

Build a comparison table:

| Check | Before | Change made | After | Result |
|---|---|---|---|---|
| Listening ports | Actual baseline | Actual action | Actual retest | Improved / unchanged / issue |
| Firewall | Actual baseline | Actual action | Actual retest | Verified / not verified |
| SSH | Actual baseline | Actual action | Actual retest | Verified / not verified |
| Permissions | Actual baseline | Actual action | Actual retest | Verified / not verified |

A change is not complete until the retest confirms the intended outcome. If you cannot verify it, label it **Not verified**.

## 14. Final report structure

Save your final report as:

`linux-kali/lab/lab-14-secure-linux-server-project.md`

Use these sections:
1. Executive summary.
2. Scope, authorization and safety boundaries.
3. Environment, VM versions and network topology.
4. Baseline inventory and methodology.
5. Findings with evidence.
6. Remediation actions and rollback plan.
7. Before/after retest results.
8. Limitations and items not verified.
9. Lessons learned and next steps.
10. Evidence index with sanitized screenshot filenames.

Include a network diagram and sanitized screenshots. Keep raw logs and captures private unless carefully reviewed and necessary. Never include credentials, private keys or tokens.

## 15. Completion checklist

Mark the capstone **Completed** only when all applicable items are supported by learner-collected evidence:

- [ ] Isolated topology and actual IP plan documented.
- [ ] Ubuntu OS, kernel, package and resource inventory recorded.
- [ ] Accounts and sudo privileges reviewed.
- [ ] Project directory permissions checked.
- [ ] Services and listening ports inventoried.
- [ ] Firewall policy reviewed and safely verified.
- [ ] SSH configuration reviewed and safely validated, if SSH is in scope.
- [ ] Authentication/system logs reviewed.
- [ ] Authorized Nmap scan completed from Kali.
- [ ] Findings and risk ratings justified by evidence.
- [ ] Remediation and rollback documented.
- [ ] Before/after checks repeated and results recorded.
- [ ] Final report and sanitized evidence saved.

**Current repository status:** Project blueprint prepared. Implementation, actual findings, screenshots and retesting remain the learner's responsibility. No VM configuration has been changed by the assistant.

## 16. Review questions

1. Why should a server-hardening project begin with an asset and service baseline?
2. What does least privilege mean for administrator accounts?
3. How do Linux permission bits affect access to a directory?
4. Why should you identify required services before changing firewall rules?
5. What is the risk of disabling SSH password authentication before testing key-based login?
6. Why can Nmap and local socket inspection show different results?
7. What evidence would demonstrate that a hardening change worked?
8. Why must findings distinguish confirmed vulnerabilities from items needing investigation?
