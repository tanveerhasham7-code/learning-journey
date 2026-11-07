# 04 — PowerShell for Security Administration

## What is PowerShell?
PowerShell is a command-line shell and scripting language used to administer Windows. It works with structured objects. Cmdlets commonly use Verb-Noun names such as Get-Service.

## Help and discovery
~~~powershell
Get-Help Get-Service
Get-Command *EventLog*
Get-Command -Module Microsoft.PowerShell.Management
Get-Service | Get-Member
~~~

Use Get-Help with the Examples option to learn a command. Help content may need updating on some systems.

## Pipeline and filtering
~~~powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10 Name, Id, CPU
Get-LocalUser | Select-Object Name, Enabled, LastLogon
~~~

The pipeline passes objects to the next command. Where-Object filters, Select-Object chooses properties and Sort-Object sorts results.

## Variables and loops
~~~powershell
$computer = $env:COMPUTERNAME
"Computer: $computer"

foreach ($service in (Get-Service)) {
    if ($service.Status -eq "Running") {
        $service.Name
    }
}
~~~

## Read-only system inventory example
~~~powershell
$os = Get-CimInstance Win32_OperatingSystem
[pscustomobject]@{
    CollectedAt = Get-Date
    ComputerName = $env:COMPUTERNAME
    CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
    OperatingSystem = $os.Caption
    Version = $os.Version
    LastBoot = $os.LastBootUpTime
} | Format-List
~~~

Review output for private identifiers before publishing.

## Execution policy and safety
~~~powershell
Get-ExecutionPolicy -List
~~~

Execution policy helps reduce accidental script execution but is not a complete security boundary. Do not weaken system policy globally to run unknown scripts. Read scripts first, use least privilege, validate inputs and test in a VM snapshot.

## Practical tasks
List running services, find the five highest CPU processes, export local user names to a private lab CSV and write a small inventory script. Record which commands require elevation and why.

## Check yourself
What is a PowerShell object? What does the pipeline do? Why is execution policy not a full security control?
