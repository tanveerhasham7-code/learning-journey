# Linux Lab 5 — Processes and Services

**Status: Completed — learner confirmed practice on 18 November 2026.**

## 1. Objective

Learn how to start, identify, inspect and safely stop a harmless Linux process, then inspect a systemd service without changing service configuration.

Run these commands only in your own Kali Linux VM.

## 2. Start a harmless test process

Open a terminal and run:

```bash
sleep 300 &
```

The shell should print a process ID (PID). Record that number. The process simply waits for five minutes; it does not change files or system settings.

## 3. Identify the process

Run:

```bash
pgrep -a -x sleep
ps -C sleep -o pid,ppid,user,stat,cmd
```

Find the PID for the `sleep 300` process you started. If another sleep process already exists, distinguish yours by its command and PID.

To inspect one specific PID, replace `<PID>` with your recorded number:

```bash
ps -p <PID> -o pid,ppid,user,stat,etime,cmd
```

Do not type the angle brackets; substitute the actual number.

Record:
- PID
- Parent PID (PPID)
- Owner
- Process state (STAT)
- Command

## 4. Stop the test process gracefully

Replace `<PID>` with the PID you recorded:

```bash
kill -TERM <PID>
```

Verify that it has stopped:

```bash
ps -p <PID> -o pid,stat,cmd
pgrep -a -x sleep
```

If the exact PID no longer appears, the test process has ended. Do not use `kill -9` unless there is a genuine reason; this lab should normally finish with SIGTERM.

## 5. Inspect a systemd service

Inspect NetworkManager, a common Kali networking service:

```bash
systemctl status NetworkManager --no-pager
```

Record the service name and the actual Active state shown (for example, active (running), inactive, or not-found). Do not assume the expected state is the actual state.

You can also list loaded service units:

```bash
systemctl list-units --type=service --no-pager
```

This is an inspection-only exercise. Do not stop, disable, enable or restart services for this lab.

## 6. Expected learning outcomes

After successful execution, you should be able to:
- Explain that a process is a running instance of a program.
- Explain that a PID identifies a process.
- Use `ps` and `pgrep` to locate processes.
- Read basic process details such as owner, parent PID and state.
- Send SIGTERM to end your own harmless test process.
- Explain that systemd manages services and `systemctl status` inspects their state.

These are the intended learning outcomes. The learner confirmed practicing the lab, but exact terminal output was not supplied for independent verification.

## 7. Evidence checklist

Save screenshots or a terminal transcript showing:
- [ ] The `sleep 300` process started and its PID.
- [ ] `ps` / `pgrep` output identifying the process and owner.
- [ ] The graceful termination command and verification that the process ended.
- [ ] The actual `systemctl status NetworkManager` output.

Before publishing, review screenshots for usernames, hostnames, IP addresses or other information you do not want public.

## 8. Completion criteria

Mark this lab **Completed** only after the learner has:
1. Started the harmless test process.
2. Identified and recorded its actual PID and owner.
3. Terminated it gracefully and verified it ended.
4. Inspected a systemd service and recorded its actual state.
5. Saved evidence or explicitly confirmed the observed results.

**Completion note:** The learner confirmed completing the practice on 18 November 2026. No screenshots or exact terminal output were supplied; this report records learner-confirmed completion and does not claim independent verification of VM observations.
