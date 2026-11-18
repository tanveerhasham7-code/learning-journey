# Lab 12 — Nmap Authorized Service Inventory

**Status: Completed — learner-confirmed practice (18 November 2026).**  
The learner confirmed that they practiced this authorized Nmap inventory lab. No screenshots or terminal output were supplied in this update, so completion is recorded as learner-confirmed rather than independently verified. No specific scan targets, ports, services or version results are claimed here.

## 1. Objective

Use Nmap from Kali Linux to:
- Confirm whether your authorized Ubuntu lab VM is reachable.
- Discover open TCP ports on that one target.
- Identify likely services and versions.
- Verify discovered services locally on Ubuntu.
- Record security observations and sensible hardening recommendations.

## 2. Authorization and safety

- Scan only the Ubuntu VM you own or are explicitly authorized to test.
- Use an isolated Host-only/Internal virtual network.
- Do not scan public IPs, university networks, workplace networks, or other devices.
- Confirm the target IP from the Ubuntu console before scanning.
- Keep the scan limited to one host. Do not use broad ranges or aggressive scripts.
- Nmap service/version detection can generate traffic and may be logged. It is appropriate here only because the target is your own lab VM.

## 3. Confirm the lab topology

On Ubuntu, run:

```bash
hostname
ip -br addr
ip route
```

On Kali, run:

```bash
hostname
ip -br addr
ip route
```

Confirm both VMs are attached to the same isolated virtual network and are in a compatible subnet. Record the actual Ubuntu IPv4 address. The address `192.168.56.30` is only an example; do not assume it is your target.

## 4. Check target reachability

From Kali, substitute the actual Ubuntu IP:

```bash
ping -c 4 <UBUNTU_IP>
```

Record packet loss and response times. If ping does not work, verify the VM network, address, subnet, interface state, and local firewall. Some systems block ICMP while still allowing specific TCP services, so ping failure alone does not prove the host is offline.

## 5. Discover whether the host is up

Run this single-host discovery scan from Kali:

```bash
nmap -sn <UBUNTU_IP>
```

This checks host discovery without performing a port scan. Record whether Nmap reports the host as up. If discovery is blocked, continue only after independently confirming the target IP and your authorization; do not expand the target scope.

## 6. Identify open TCP ports and service versions

Run a standard TCP service/version scan against the one confirmed Ubuntu target:

```bash
nmap -sV <UBUNTU_IP>
```

This scans Nmap's default set of common TCP ports and attempts to identify services and versions on discovered open ports. It is not a complete scan of every possible TCP/UDP port.

Record each result:
- Port number and protocol (for example, `22/tcp`).
- State (`open`, `closed`, or `filtered`).
- Service name reported by Nmap.
- Version/product details, if detected.
- Any uncertainty or generic/unknown fingerprint.

Do not assume a service version is perfectly accurate. Nmap reports a best-effort identification.

### Optional full TCP port inventory

Only if the lab objective specifically requires all TCP ports and the single-host standard scan has completed, you may run:

```bash
nmap -p- <UBUNTU_IP>
```

This is slower and generates more traffic. It is optional; do not run it against any other host. If you find additional ports, use a targeted `-sV -p <PORTS>` scan on those ports only.

## 7. Verify findings locally on Ubuntu

On Ubuntu, inspect listening sockets:

```bash
sudo ss -tulpen
```

For each Nmap-reported open TCP port, compare the port and process/service shown locally. If a service is managed by systemd, inspect its status, for example:

```bash
systemctl status ssh --no-pager
```

Use the correct service name for the port you actually found. Do not install or enable services just to create scan results.

## 8. Findings and hardening recommendations

Create a small inventory table in your report:

| Port/protocol | Nmap service/version | Local verification | Business need | Recommendation |
|---|---|---|---|---|
| Actual result | Actual result | Actual result | Required / unknown / not required | Evidence-based action |

For every open service:
- Determine whether it is needed.
- If not needed, consider disabling it using the Ubuntu service's normal administration process.
- If needed, restrict access with a host firewall to trusted lab sources.
- Keep the package updated through the normal update process.
- Retest after any change.

Do not disable SSH or another service that you need for administration without confirming console access and a rollback plan. Do not make changes simply because a port is open.

## 9. Troubleshooting

- **Wrong target IP:** re-check `ip -br addr` on Ubuntu.
- **Host appears down:** confirm both VMs use the same virtual network and verify the target from its console.
- **All ports filtered:** inspect Ubuntu firewall rules and network mode; do not disable the firewall blindly.
- **No open ports:** this may be a valid result. Record it and compare with `ss -tulpen`.
- **Version not detected:** some services do not disclose version information; record the uncertainty.
- **Nmap command not found:** check `nmap --version`; install Nmap on Kali only if it is missing and you are comfortable managing packages.

## 10. Evidence checklist

Save sanitized screenshots or terminal output showing:
- Ubuntu target IP and interface.
- Kali IP and interface.
- Successful/failed reachability test.
- `nmap -sn` result.
- `nmap -sV` result.
- Ubuntu `ss -tulpen` output.
- Completed service inventory and recommendations.

Before uploading, redact unrelated IP addresses, usernames, hostnames, MAC addresses, and any sensitive information. Keep only evidence relevant to the isolated lab.

## 11. Review questions

1. What is the difference between `nmap -sn` and `nmap -sV`?
2. What does an `open` TCP port indicate?
3. What does a `filtered` state usually mean?
4. Why should you verify Nmap results using `ss -tulpen` on Ubuntu?
5. Why is an open port not automatically a vulnerability?
6. Why must scanning stay within the authorized target scope?
7. What should you consider before disabling a service?

## 12. Completion criteria

Mark this lab **Completed** only after you:
- Confirm the target is your own Ubuntu VM and record its actual IP.
- Run the single-host discovery and service/version scan from Kali.
- Record actual port, state, service and version results.
- Verify listening services locally on Ubuntu.
- Write evidence-based recommendations and answer the questions.
- Save sanitized evidence and note any limitations.

**Current repository status:** Reference prepared only. No Nmap scan was run by the assistant, no learner VM was accessed, and no real scan output is claimed.


**Completion note (18 November 2026):** The learner confirmed that they practiced this lab on their authorized environment. No screenshots or terminal output were supplied with this update; therefore, actual Nmap findings are not reproduced or inferred.
