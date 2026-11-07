# 11 — Group Policy

## What is Group Policy?
Group Policy manages Windows user and computer settings. In a domain, administrators apply Group Policy Objects (GPOs) through Active Directory. Local Group Policy can configure one supported computer.

## Scope and processing
Domain GPOs can be linked to sites, domains and Organizational Units. Processing order, inheritance, security filtering and WMI filters affect which settings apply. Conflicting settings require investigation.

## Local policy tools
Open gpedit.msc on supported editions. Use gpresult to inspect resultant policy.

~~~powershell
gpresult /r
gpresult /h "$env:USERPROFILE\Desktop\gpresult.html"
~~~

The report may contain usernames, domain and organization details; sanitize it before sharing.

## Security policy areas
Examples include password and lockout policy, User Rights Assignment, Windows Defender Firewall, Windows Update, Audit Policy, removable storage, Defender Antivirus and interactive logon settings. Availability and names vary by edition and administrative templates.

## Safe lab
Use a VM snapshot. Inspect account, audit and Defender policy areas. Change one low-risk setting only after recording its original state. Run gpresult, verify the result and restore the setting.

## Troubleshooting
Check GPO scope, links, inheritance, security filtering, replication, client connectivity and policy-processing logs. A missing policy may be due to edition limitations or scope.

## Check yourself
What is a GPO? Why verify resultant policy instead of assuming a setting applied?
