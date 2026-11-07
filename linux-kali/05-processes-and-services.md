# 05 — Processes, Services and systemd

## Process basics
A process is a running instance of a program. Each process has a Process ID (PID), owner, state, resource use and parent process (PPID).

```bash
ps aux
ps -ef
top
htop
pgrep ssh
pstree
```
A process may be running, sleeping, stopped or a zombie. A zombie has finished execution but still has an entry awaiting collection by its parent.

## Signals and stopping processes
```bash
kill -l
kill PID
kill -TERM PID
kill -KILL PID
pkill process-name
```
SIGTERM requests a process to exit cleanly. SIGKILL forces termination and does not allow cleanup. Prefer graceful termination and verify the PID first.

## systemd services
Many Linux distributions use systemd as the init system and service manager.
```bash
systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
sudo systemctl enable ssh
sudo systemctl disable ssh
systemctl list-units --type=service
systemctl --failed
```
start/stop changes runtime state. enable/disable controls automatic startup. Service names vary: SSH server is commonly ssh on Debian/Ubuntu and may be sshd elsewhere.

## Scheduling
- cron: recurring scheduled commands.
- systemd timers: systemd-managed scheduled tasks.
- at: one-time scheduled jobs, if installed.

Inspect your own scheduled tasks with crontab -l. Never add unknown scripts to scheduled tasks.

## Resource monitoring
```bash
free -h
uptime
vmstat 1 5
df -h
du -sh /var/log
```
Observe CPU load, memory pressure, disk space and process activity. High usage is not automatically malicious; compare it with normal system behavior.

## Lab
1. Run sleep 300 in a terminal.
2. Find its PID using pgrep -a sleep or ps.
3. Stop it with SIGTERM.
4. Inspect SSH service status.
5. If SSH is not installed, document that it is absent.
6. List failed services and explain any entries.

## Security connection
Unexpected processes, unfamiliar services, unusual parent-child relationships, persistence through scheduled jobs and unexpected listening sockets can be investigation clues. Validate findings before concluding a system is compromised.
