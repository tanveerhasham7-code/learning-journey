# 01 — Linux Fundamentals and Architecture

## What is Linux?
Linux is an open-source, Unix-like operating-system kernel. A complete Linux operating system combines the kernel with system utilities, libraries, package management and applications. Such a complete system is called a distribution (distro).

Examples:
- Ubuntu and Debian: general-purpose systems commonly used on desktops and servers.
- Fedora: community distribution with modern technologies.
- Red Hat Enterprise Linux: enterprise-focused distribution.
- Kali Linux: Debian-based distribution for penetration testing, security research and digital forensics.
- Linux Mint: desktop-oriented distribution.

Kali is not automatically the best system for learning administration. Learn general Linux administration on Ubuntu or Debian, then use Kali as a specialized security workstation.

## Kernel, shell and terminal
- **Kernel:** core component managing CPU, memory, devices, processes and system calls.
- **Shell:** command interpreter; Bash is a common example.
- **Terminal emulator:** application window that displays a terminal session.
- **User space:** programs and services running outside the kernel.
- **System call:** controlled interface through which programs request kernel services.

A terminal and a shell are not the same thing: the terminal displays the session; the shell interprets commands.

## Simplified architecture
Hardware → Linux kernel → system libraries and services → shell and applications → user.

## User accounts
- Root is the superuser account with broad system authority.
- A standard user has limited permissions.
- sudo allows approved users to run specific commands with elevated privileges.

Use a standard account for daily work. Elevate privileges only when needed.

## Boot process overview
1. BIOS/UEFI firmware initializes hardware.
2. A bootloader such as GRUB loads the Linux kernel and initramfs.
3. The kernel initializes devices and mounts the initial root filesystem.
4. The init system (commonly systemd) starts services and targets.
5. A login prompt or graphical desktop appears.

## Identify your system
```bash
whoami
id
hostname
uname -a
cat /etc/os-release
uptime
date
```

## Why this matters in cybersecurity
Linux is common in servers, cloud systems, containers, network appliances and security tools. A defender needs to understand accounts, permissions, processes, sockets and logs to investigate suspicious activity.

## Practice questions
1. Difference between Linux kernel and Linux distribution?
2. Difference between terminal and shell?
3. Why should daily work not be performed as root?
4. Describe the main Linux boot stages.
5. Why is Linux knowledge useful to a SOC analyst?
