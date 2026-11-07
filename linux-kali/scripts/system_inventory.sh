#!/usr/bin/env bash
# Basic Linux system inventory for a lab VM.
# Run as a normal user; review output before sharing publicly.
set -u

section() {
  printf '\n===== %s =====\n' "$1"
}

section "DATE"
date -Is

section "HOST"
hostname

section "OPERATING SYSTEM"
if [[ -r /etc/os-release ]]; then
  cat /etc/os-release
else
  echo "OS release file not available"
fi

section "KERNEL"
uname -a

section "CURRENT USER"
id

section "NETWORK INTERFACES"
ip -br addr 2>&1 || true

section "ROUTES"
ip route 2>&1 || true

section "LISTENING SOCKETS"
ss -tuln 2>&1 || true

section "DISK SPACE"
df -h 2>&1 || true

section "MEMORY"
free -h 2>&1 || true

echo
echo "Inventory complete. Review and redact sensitive details before publishing."
