# 06 — Package and Software Management

## What is a package?
A package is a software bundle containing program files, metadata and dependency information. A package manager installs, updates and removes packages while tracking dependencies.

Debian, Ubuntu and Kali use APT with .deb packages. Fedora commonly uses DNF/RPM. This guide focuses on APT.

## APT commands
```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
sudo apt install curl
apt show curl
dpkg -l curl
sudo apt remove curl
sudo apt autoremove
```
- apt update refreshes repository metadata; it does not upgrade installed packages.
- apt upgrade installs available upgrades.
- apt install installs a package.
- apt show displays package details.
- dpkg -l queries installed packages.

## Repositories and trust
Repositories provide packages and metadata. Package managers verify repository signatures and package integrity using configured trust keys. Add repositories only from trusted official sources. Avoid random scripts that add repositories or replace package sources.

## Update strategy for a learning VM
1. Take a VM snapshot.
2. Confirm Internet connectivity.
3. Review configured repositories.
4. Run sudo apt update.
5. Review pending upgrades.
6. Apply updates and read errors.
7. Reboot if a kernel or critical component update requires it.
8. Verify the system and services afterward.

Kali is a rolling distribution. Follow its official upgrade guidance and do not mix Ubuntu or Debian repositories into Kali.

## Software inventory
```bash
apt list --installed
dpkg -l
which python3
command -v wireshark
```
Maintain an inventory of tools you install and why they are needed.

## Lab
Install a small utility such as tree in your Ubuntu VM, inspect package information, verify the command exists, then remove it. Explain the difference between updating repository metadata and upgrading software.

## Security connection
Unpatched software is a common attack path. Unsupported packages, untrusted repositories and unnecessary applications increase risk. Maintain an update process and remove software that is not required.
