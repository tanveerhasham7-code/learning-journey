# Lab 1 — Linux System Identification

**Status:** Completed  
**Environment:** Kali Linux VM running in VMware Workstation  
**Date:** 17 November 2026

## Objective

Identify the Kali Linux distribution and release, kernel version, hostname, logged-in user, system architecture, uptime, memory, disk usage and network interface address.

## Commands performed and observations

| Command | Purpose | Observed result |
|---|---|---|
| `cat /etc/os-release` | Identify distribution and release | Kali GNU/Linux Rolling; VERSION_ID="2026.3"; VERSION="2026.3" |
| `uname -r` | Show kernel release | `7.0.12+kali-amd64` |
| `hostname` | Show system hostname | `kali` |
| `whoami` | Show current account | `kali` |
| `uname -m` | Show CPU architecture | `x86_64` (64-bit x86 architecture) |
| `uptime` | Show uptime, users and load averages | Screenshot showed approximately 5 minutes uptime, 1 user, load averages 0.08, 0.23, 0.13 |
| `free -h` | Inspect RAM and swap | 4.1 GiB RAM total; 1.1 GiB used; 3.0 GiB available; 953 MiB swap total |
| `df -h` | Inspect filesystem capacity | Root filesystem `/dev/sda1`: 79G total, 19G used, 56G available, 25% used |
| `ip -br addr` | Inspect interface state and IP address | `eth0` UP with `192.168.254.128/24`; loopback `lo` shown |

## Notes and troubleshooting

- The first attempt used `cat /etc/os-release/` with a trailing slash and returned “Not a directory”. The corrected command, `cat /etc/os-release`, worked successfully.
- The screenshots show the successful corrected command and the subsequent system-identification commands.
- The Kali VM's `eth0` interface was UP at the time of the screenshot. The observed IPv4 address was `192.168.254.128/24`.
- System resource and uptime values are point-in-time observations and can change after reboot or as workloads change.

## What I learned

1. `/etc/os-release` identifies the Linux distribution and release.
2. `uname` provides kernel and architecture information.
3. `whoami` and `hostname` identify the current account and machine name.
4. `free` and `df` report memory and filesystem capacity.
5. `ip` helps inspect network interfaces and assigned addresses.
6. A Linux distribution includes more than the kernel: it also includes user-space tools and package management.

## Evidence

### Screenshot 1 — Kali release information

![Kali release information](screenshort/lab1/Screenshot%202026-11-17%20175452.png)

*The initial command typo is visible, followed by the corrected `cat /etc/os-release` command and the Kali release details.*

### Screenshot 2 — Kernel, hostname, user, architecture, uptime, memory and disk

![System identification commands](screenshort/lab1/Screenshot%202026-11-17%20175854.png)

*Terminal evidence for the system-identification and resource-inspection commands.*

### Screenshot 3 — Network interface and IP address

![Network interface address](screenshort/lab1/Screenshot%202026-11-17%20175942.png)

*The `ip -br addr` output shows the loopback interface and active `eth0` interface.*

## Completion

The commands and screenshot evidence for Lab 1 have been reviewed and documented. No system configuration was changed.
