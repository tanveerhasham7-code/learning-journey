# 14 — Linux and Kali Troubleshooting Handbook

## Command not found
Possible causes: package not installed, executable not in PATH, typo or different command name.
```bash
command -v toolname
echo "$PATH"
apt search package-name
```
Install software only from trusted repositories.

## Permission denied
```bash
whoami
id
ls -l filename
namei -l /full/path/to/file
```
Do not immediately use sudo or chmod 777. Identify the exact permission or ownership issue and grant the minimum required access.

## Disk full
```bash
df -h
df -i
du -xhd1 /var 2>/dev/null
```
A filesystem can run out of inodes even when space remains. Do not delete unknown system files or logs blindly.

## Network unavailable
```bash
ip -br link
ip -br addr
ip route
ip neigh
ping -c 3 <lab-gateway>
getent hosts example.com
```
Check link, address, route, gateway, DNS and firewall separately. A failed ping can be caused by ICMP filtering.

## APT errors
Check Internet connectivity, repository configuration, system time and full error details. Run sudo apt update and read the output. Do not fix repository errors by disabling signature checks or adding untrusted sources.

## Service fails to start
```bash
systemctl status service-name
journalctl -u service-name --since "30 minutes ago"
```
Read the exact error, validate configuration and check whether the required port is already in use.

## SSH connection fails
Check target IP, network mode, whether the SSH server is installed/running, firewall rules, port and authentication configuration. Use VM console access to recover from a bad SSH configuration.

## Kali VM is slow
Check host resources, assigned RAM/CPU, disk space, running processes and desktop effects. Avoid allocating all host resources to the VM.

## Troubleshooting method
1. Define the symptom.
2. Identify affected host and scope.
3. Record recent changes.
4. Gather command output and logs.
5. Form one testable hypothesis.
6. Make one controlled change.
7. Retest and document.
8. Roll back if the change worsens the system.

Do not publish passwords, private keys, personal data or sensitive logs in reports.
