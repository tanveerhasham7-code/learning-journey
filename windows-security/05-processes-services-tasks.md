# 05 — Processes, Services and Task Scheduler

## Processes and threads
A process is a running program with its own virtual address space and resources. A thread is an execution path within a process. Analysts examine process name, executable path, publisher/signature, parent process, command line, network activity and behavior.

~~~powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, Id, CPU
Get-CimInstance Win32_Process | Select-Object Name, ProcessId, ParentProcessId, ExecutablePath
~~~

A familiar process name alone does not prove that a file is safe. Validate its path, signature and context.

## Services
Services run in the background and may start automatically, manually or be disabled. Examples include Windows Update and Event Log.

~~~powershell
Get-Service
Get-CimInstance Win32_Service | Select-Object Name, State, StartMode, StartName, PathName
~~~

Service accounts and executable paths are important security details. Do not disable an unfamiliar service without research; it may be essential.

## Scheduled tasks
Task Scheduler launches programs or scripts based on triggers such as time, logon or system events. Review the task name, action, path, arguments, trigger and run-as identity.

~~~powershell
Get-ScheduledTask | Select-Object TaskName, TaskPath, State
~~~

## Defensive investigation
For a suspicious process or service, record the time, inspect path and signature, check parent process and command line, review related events and compare with a known-good baseline. Follow incident procedures before containment.

## Safe lab
Use Task Manager and Services to inspect three expected services. Record their purpose, state and startup type. Create a harmless scheduled task to open Notepad, verify it and remove it. Do not stop critical services.

## Check yourself
How does a process differ from a service? Why is disabling every unfamiliar service unsafe?
