# 10 — Linux Security Hardening

## What is hardening?
Hardening reduces unnecessary exposure and makes a system more resistant to misuse. It is a continuous process, not a one-time command.

## Core hardening checklist
- Keep the OS and applications supported and patched.
- Remove or disable unnecessary packages and services.
- Use standard accounts for daily tasks.
- Apply least privilege with sudo.
- Use strong authentication and MFA where supported.
- Restrict SSH access and use key-based authentication where appropriate.
- Enable and test a host firewall.
- Apply secure file permissions and ownership.
- Protect backups and sensitive configuration.
- Centralize logs and synchronize system time.
- Monitor listening ports and unexpected processes.
- Review changes regularly.

## SSH hardening
Common configuration file: /etc/ssh/sshd_config (some systems also use included configuration directories).

Settings to understand:
- PermitRootLogin
- PasswordAuthentication
- PubkeyAuthentication
- AllowUsers or AllowGroups
- MaxAuthTries

Do not blindly paste settings. First confirm console access and a working alternate admin session. Validate configuration with sudo sshd -t before reloading the service. A bad SSH configuration can lock out remote administrators.

## Firewall
Use a default-deny inbound policy where appropriate, then allow only required services from approved sources. Document each rule's purpose. Test allowed and denied traffic.

## Review special permissions and writable directories
```bash
sudo find / -xdev -type f -perm -4000 -ls 2>/dev/null
sudo find / -xdev -type f -perm -2000 -ls 2>/dev/null
find / -xdev -type d -perm -0002 -ls 2>/dev/null
```
These commands can return legitimate system files and may take time. Review results; do not delete files simply because they have special permissions.

## Audit accounts and services
```bash
getent passwd
getent group sudo
systemctl --type=service --state=running
ss -tulpen
```
Check whether accounts, services and ports are expected for the system's role.

## Backups and recovery
Keep backups separate from the host, protect access, test restoration and document recovery steps. A backup that has never been tested may not be usable.

## Lab: harden an Ubuntu VM
1. Snapshot the VM.
2. Apply updates.
3. Create a non-root admin account.
4. Review installed packages and running services.
5. Configure UFW for only the services needed in your lab.
6. Review SSH settings without risking lockout.
7. Inspect listening ports and file permissions.
8. Review authentication logs.
9. Repeat inventory and compare before/after.
10. Write a report listing changes, verification and rollback plan.

Security controls can affect availability. Test changes, maintain a rollback path and document configuration before modifying production systems.
