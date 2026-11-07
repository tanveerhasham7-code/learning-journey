# 11 — Kali Linux: Purpose, Installation and Safe Setup

## What is Kali Linux?
Kali Linux is a Debian-based distribution maintained by OffSec for penetration testing, security research, digital forensics and related professional workflows. It includes a curated collection of security tools.

Kali is not a magic hacking system. Installing it does not make someone a penetration tester. The important skills are networking, operating systems, scripting, security fundamentals, methodology, ethics and clear reporting.

## Kali versus Ubuntu
| Ubuntu | Kali Linux |
|---|---|
| General-purpose desktop/server distribution | Specialized security distribution |
| Good starting point for Linux administration | Useful for security-tool workflows |
| Broad everyday software ecosystem | Curated security tools and defaults |
| Suitable for normal daily computing | Best used as a dedicated security VM |

Learn administration on Ubuntu/Debian and use Kali as a separate security workstation.

## Safe installation approach
1. Download the official installer or prebuilt VM image from the Kali Linux website.
2. Verify the published checksum/signature when instructions provide one.
3. Create a VirtualBox VM with suitable RAM, CPU and disk allocation.
4. Use NAT for initial updates if required.
5. Use Host-only or Internal Network for isolated lab exercises.
6. Install and update using official Kali documentation.
7. Take a clean snapshot after setup.
8. Create a standard user and use sudo when required.

Hardware requirements depend on desktop environment and workload. Allocate resources based on your computer; avoid starving the host OS.

## First commands
```bash
cat /etc/os-release
uname -r
whoami
id
ip -br addr
ip route
sudo apt update
```
Kali is rolling-release. Read official upgrade guidance before large upgrades; do not mix repositories from other distributions.

## Package and repository safety
Use official Kali repositories and signed packages. Avoid unofficial scripts that change APT sources or install unknown tool bundles. Read commands before executing them, especially commands that use sudo.

## VirtualBox network adapter modes
- NAT: VM can generally access outbound Internet through the host; inbound access is restricted by default.
- Bridged: VM appears on the physical network. Avoid this for vulnerable targets or unauthorized testing.
- Host-only: host and VMs can communicate on a private virtual network.
- Internal Network: selected VMs communicate with each other without direct host access.

For controlled target testing, Host-only or Internal Network is usually safer.

## Responsible use
Only test systems you own or have explicit written authorization to assess. Follow the agreed scope, time window, allowed techniques and data-handling rules. Do not scan university, workplace, public Wi-Fi or public IP addresses without permission.

## Lab
Install Kali as a VM, record version and adapter mode, update it, create a snapshot, and communicate with your own Ubuntu lab VM over a host-only network. Save a topology diagram and sanitized command output.
