# Linux Lab 8 — Bash System Inventory Script

**Status: Reference prepared — learner execution and evidence pending.**

## 1. Objective

Create and run a Bash script that collects a basic inventory of your own Kali Linux VM. The script records:
- Hostname and collection date/time
- Linux distribution information
- Kernel version
- Current user
- Network interface addresses
- Routing table
- Filesystem disk usage
- Listening TCP/UDP sockets

This is a read-only inventory exercise. It does not change network settings, install software, alter firewall rules or stop services.

## 2. Create a practice folder

Open a Kali terminal and run:

```bash
mkdir -p ~/lab8-inventory
cd ~/lab8-inventory
```

## 3. Create the script

Open a text editor:

```bash
nano system-inventory.sh
```

Paste this script:

```bash
#!/usr/bin/env bash

# Read-only system inventory for the Linux Lab 8 exercise.
# Run as a normal user; root privileges are not required.

set -u

REPORT="inventory-report-$(date +%Y%m%d-%H%M%S).txt"

{
    echo "======================================"
    echo "       LINUX SYSTEM INVENTORY"
    echo "======================================"
    echo
    echo "Collection date: $(date)"
    echo "Hostname: $(hostname)"
    echo "Current user: $(whoami)"
    echo

    echo "----- OPERATING SYSTEM -----"
    if [[ -r /etc/os-release ]]; then
        cat /etc/os-release
    else
        echo "OS release information is unavailable."
    fi
    echo

    echo "----- KERNEL -----"
    uname -r
    echo

    echo "----- NETWORK INTERFACES -----"
    ip -br addr
    echo

    echo "----- ROUTING TABLE -----"
    ip route
    echo

    echo "----- DISK USAGE -----"
    df -h
    echo

    echo "----- LISTENING TCP/UDP SOCKETS -----"
    ss -tuln
    echo

    echo "======================================"
    echo "Inventory collection finished."
    echo "======================================"
} > "$REPORT"

echo "Inventory report saved to: $REPORT"
```

In nano, save with **Ctrl+O**, press **Enter**, then exit with **Ctrl+X**.

## 4. Review and run the script

Check the script contents:

```bash
cat system-inventory.sh
```

Make it executable:

```bash
chmod u+x system-inventory.sh
```

Run it as your normal Kali user (do not use sudo):

```bash
./system-inventory.sh
```

The script should print the report filename. The report is saved in the current practice folder.

## 5. Read the generated report

List the files:

```bash
ls -lh
```

Read the report. Replace the wildcard with the actual generated report filename if more than one report exists:

```bash
cat inventory-report-*.txt
```

If multiple reports exist, use `ls -1 inventory-report-*.txt` and then `cat` the specific file you want to inspect.

## 6. Understand the script

- `#!/usr/bin/env bash` selects Bash using the environment.
- `REPORT=...` creates a timestamped report filename.
- `$(command)` runs a command and inserts its output.
- `{ ... } > "$REPORT"` groups the inventory output and redirects it to the report file.
- `ip -br addr` summarizes network interfaces and addresses.
- `ip route` displays routes known to the kernel.
- `df -h` reports filesystem space in readable units.
- `ss -tuln` lists listening TCP/UDP sockets numerically.

## 7. Security and privacy review

Inventory reports can reveal details about your device and network, including usernames, hostnames, private IP addresses, filesystem layout and listening ports.

Before uploading a report or screenshot to a public GitHub repository:
1. Open and review the report.
2. Remove or mask any information you do not want public.
3. Never include passwords, tokens, private keys or other credentials.
4. Do not publish details about systems or networks you do not own or have permission to assess.

For this exercise, you can submit sanitized screenshots of the terminal and a redacted report rather than uploading the raw report.

## 8. Troubleshooting

- **Permission denied when running:** confirm you are in the lab folder and run `chmod u+x system-inventory.sh`.
- **Command not found:** check for typing errors. Kali normally includes `ip`, `df`, `uname`, `hostname` and `ss`; record any missing command rather than installing packages without reviewing the need.
- **Empty or incomplete output:** run the relevant command separately to see its error, then record the actual result.
- **No listening sockets:** this can be a valid result; do not create a service just to make the list non-empty.

## 9. Evidence checklist

Save screenshots or a terminal transcript showing:
- [ ] Script source in the editor or displayed with `cat`.
- [ ] Executable permission and successful script execution.
- [ ] Generated report filename.
- [ ] Sanitized report contents showing the collected sections.

## 10. Questions to answer

1. What is a Bash script?
2. Why did we use `chmod u+x`?
3. What does `$(date)` do in the script?
4. Why is the report filename timestamped?
5. What information can `ip -br addr` and `ip route` provide?
6. Why should an inventory report be reviewed before publishing?

## 11. Completion criteria

Mark this lab **Completed** only after the learner has:
1. Created the script in the lab folder.
2. Reviewed the script and made it executable.
3. Run it successfully as a standard user.
4. Opened and reviewed the generated report.
5. Answered the review questions and checked the report for sensitive information.
6. Saved evidence or explicitly confirmed the observed results.

**Current result:** This guide and script template are prepared. The assistant has not executed the script on the learner's Kali VM, and no generated report or runtime output is claimed.
