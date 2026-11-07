# 08 — Bash Scripting and Automation

## Why automate?
Bash scripts combine commands into repeatable workflows. Administrators use them for inventory, backups, checks and routine maintenance. Scripts should be readable, tested and safe.

## First script
Create hello.sh:
```bash
#!/usr/bin/env bash
echo "Hello, cybersecurity learner"
```
Run:
```bash
chmod +x hello.sh
./hello.sh
```
The shebang selects the interpreter. Execute permission allows the file to run as a program.

## Variables and input
```bash
#!/usr/bin/env bash
student="Linux learner"
printf 'Welcome, %s\n' "$student"
read -r -p "Enter your lab name: " lab
printf 'Lab selected: %s\n' "$lab"
```
Quote variables to avoid unintended word splitting and wildcard expansion.

## Conditions
```bash
#!/usr/bin/env bash
if [[ -f /etc/os-release ]]; then
  echo "Linux release information exists"
else
  echo "File not found"
fi
```
Common tests: -f regular file, -d directory, -r readable, -x executable, -eq numeric equality and == string equality.

## Loops
```bash
for item in /etc /var/log /home; do
  if [[ -d "$item" ]]; then
    printf 'Directory: %s\n' "$item"
  fi
done
```
A while loop repeats while its condition remains true:
```bash
count=1
while [[ "$count" -le 3 ]]; do
  echo "Check $count"
  ((count+=1))
done
```

## Functions and exit status
```bash
show_date() {
  date
}
show_date
echo "Exit status: $?"
```
Exit status 0 usually means success; non-zero means an error or special condition. Check command status rather than assuming success.

## Safe system inventory script
A working example is provided in scripts/system_inventory.sh. It collects hostname, OS, kernel, identity, network addresses, routes, listening sockets, disk and memory information. Run as a normal user first and review output before sharing.

## Safer scripting habits
- Quote variables, for example "$path".
- Validate input before using it.
- Avoid running downloaded scripts blindly.
- Use absolute paths for critical automation.
- Never hard-code passwords or tokens.
- Understand set -u, set -e and pipeline error behavior before relying on them.
- Test on disposable data and review scripts before running with elevated privileges.

## Lab
Write an inventory script that records hostname, date, OS version, IP addresses, routes, disk usage and listening TCP/UDP sockets to a report file. Add error handling and a short README. Do not collect credentials or private data.
