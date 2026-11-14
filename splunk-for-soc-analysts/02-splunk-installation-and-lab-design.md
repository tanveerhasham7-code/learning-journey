# 02 — Splunk Installation and Lab Design

## Objectives
Choose a suitable learning environment and plan a secure, low-cost lab.

## 1. Learning options
Use a permitted local Splunk deployment, an eligible trial or training environment, or sample datasets. Product editions, trial periods, ingestion limits, and eligibility can change; verify current official terms before starting.

## 2. Beginner topology
- Windows 10/11 or Windows Server evaluation VM as a log source.
- One Splunk instance on a supported host or VM.
- Optional Universal Forwarder on the Windows source.
- Private host-only or internal virtual network where practical.

A single-instance deployment is enough for initial SPL practice. Distributed architecture is an advanced topic.

## 3. Resource planning
Start with one Splunk instance and one data source. Check current system requirements for your exact version. Avoid running several resource-heavy VMs at once.

## 4. Security checklist
1. Download installers only from official sources.
2. Verify OS and version compatibility.
3. Read licensing and trial conditions.
4. Set a strong unique administrator password.
5. Keep management interfaces private.
6. Restrict inbound access to trusted lab systems.
7. Record versions and configuration changes.
8. Take a VM snapshot before major changes.

## 5. Ports and access
Splunk uses web, management, and receiving ports. Defaults may differ by product and configuration. Do not open ports just because a tutorial lists them; confirm your configuration and restrict access.

## Practical task
Prepare a lab worksheet with topology, roles, network boundary, resource allocation, version, data sources, and cost/safety checks. Do not publish passwords, tokens, or license files.

## Knowledge check
1. Why keep management ports private?
2. Why record product version and license conditions?
3. What is a VM snapshot useful for?
4. Can you learn SPL with sample data before configuring a forwarder?

## References
- [Install Splunk on Windows](https://docs.splunk.com/Documentation/Splunk/latest/Installation/InstallonWindows)
- [System requirements](https://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements)
