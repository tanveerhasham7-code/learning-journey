# 07 — Process Creation and Command-Line Monitoring

## 1. Process telemetry
A process is a running instance of a program. Monitoring helps establish which executable ran, under which account, with what arguments and from which parent process.

## 2. Important sources
- **Security 4688:** process creation when relevant audit policy is enabled. Command-line inclusion requires the corresponding policy setting.
- **Sysmon 1:** detailed process creation, including process identifiers, image, command line, parent information and configured hashes.
- **EDR:** may add behavioral context and process lineage.

## 3. Fields to review
Image/path, command line, user, process ID and ProcessGuid, parent image and command line, integrity level, hashes and timestamp.

## 4. Parent-child relationships
A parent launches a child process. An unusual relationship may deserve review, but updaters, management tools and legitimate scripts can create uncommon process trees.

## 5. Detection ideas
- Script interpreters launched by unexpected parents.
- Office applications spawning command interpreters.
- Executables launched from temporary or user-writable directories.
- Unusual command lines on sensitive servers.
- A new process followed by suspicious network or file activity.

These are leads, not conclusions. Tune for host role and validate safely.

## 6. Query example

~~~powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id = 4688
    StartTime = (Get-Date).AddHours(-4)
} -ErrorAction SilentlyContinue |
Select-Object TimeCreated, Id, Message
~~~

## 7. Investigation workflow
1. Confirm event and host.
2. Identify user, image and command line.
3. Inspect parent process and lineage.
4. Compare with normal host activity.
5. Search related file, registry, PowerShell and network events.
6. Validate business purpose.
7. Record evidence and uncertainty.

## 8. Practical task
Find a benign process event. Explain executable, parent, user, timestamp and why expected. If command-line data is unavailable, document which policy or source may be needed.

## 9. Knowledge check
1. What does parent-child context show?
2. Why may 4688 lack command-line information?
3. Why are process names alone weak signals?
4. What telemetry enriches process investigation?