# 09 — Logs, Monitoring and Security Investigation

## Why logs matter
Logs record events such as logins, service starts, package changes, kernel messages and application activity. They help administrators troubleshoot systems and help defenders reconstruct activity.

Common locations:
- /var/log/: many text log files.
- /var/log/auth.log: authentication and sudo events on Debian-family systems (may vary).
- /var/log/syslog: general system messages on some Debian-family systems.
- /var/log/kern.log: kernel messages on some systems.
- /var/log/apache2/: Apache logs when installed.
- systemd journal: structured system and service logs.

## journalctl
```bash
journalctl
journalctl -b
journalctl -p warning
journalctl -u ssh
journalctl --since "1 hour ago"
journalctl -f
```
Options filter by boot, priority, service or time. Availability and retained history depend on journal configuration.

## Review traditional logs
```bash
sudo less /var/log/auth.log
sudo grep -i "failed" /var/log/auth.log
sudo tail -n 50 /var/log/syslog
```
A file may not exist on every distribution. Use ls /var/log to see what your system records.

## Authentication investigation
When reviewing a suspicious login event, record:
- Timestamp and timezone
- Account name
- Source address, if remote
- Authentication method and result
- Related sudo or session events
- Hostname and system role

Repeated failed logins may be caused by a typo, old saved password, misconfigured service or malicious activity. Correlate before concluding.

## Time and resource monitoring
```bash
timedatectl
top
free -h
df -h
uptime
ss -tulpen
ps aux --sort=-%cpu | head
```
Accurate time and timezone settings help correlate events across hosts. Establish a baseline of normal CPU, memory, disk and network behavior.

## Simple investigation workflow
1. Confirm the alert and affected asset.
2. Preserve relevant time range and logs.
3. Check user, source, process and service context.
4. Compare with normal activity and approved change records.
5. Correlate authentication, network and endpoint events.
6. Document facts separately from hypotheses.
7. Escalate according to incident-response policy.

## Lab
Generate a few failed SSH login attempts against your own VM (only if SSH is installed and configured). Inspect the relevant journal or authentication log. Identify timestamp, username and source address. Then perform a successful login and compare events. Never test passwords against third-party hosts.

## Evidence handling
Keep original logs unchanged where possible. Record collection time, host and commands used. Redact personal data and secrets before adding examples to a public repository.
