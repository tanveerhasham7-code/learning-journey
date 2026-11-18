# Lab 11 — Kali-to-Ubuntu Lab Connection

**Status: Reference prepared — learner execution and evidence pending.**  
This guide provides a complete procedure for building and verifying an isolated connection between your own Kali and Ubuntu virtual machines. It has not been executed on the learner's VMs. Record actual interface names, IP addresses, and results; do not treat example values as observed results.

## 1. Objective

Connect Kali Linux and Ubuntu to the same isolated virtual network, assign or confirm addresses in one subnet, test two-way connectivity, and inspect neighbor (ARP) information.

## 2. Safety and preparation

- Use only VMs you own or are authorized to administer.
- Prefer a Host-only network so the lab machines can communicate with each other without being exposed directly to the physical LAN.
- Take VM snapshots before changing network settings.
- Keep access to each VM's console.
- Do not bridge the lab VMs to a public or untrusted network for this exercise.
- Example addresses below are illustrative. First inspect your actual VMware Host-only subnet and avoid conflicts with DHCP or other devices.

## 3. Configure VMware networking

1. Power off both Kali and Ubuntu VMs.
2. Open each VM's **Settings → Network Adapter**.
3. Select the same **Host-only** network (for example, the same VMnet host-only network) for both VMs.
4. Ensure both adapters are connected and set to connect at power on.
5. Do not select different VMnet networks for the two VMs.
6. Start Ubuntu and Kali.

The exact VMware menu labels may differ by product/version. If you use an Internal Network in another hypervisor, select the same internal network name on both VMs.

## 4. Inspect addresses and interfaces

On both VMs, run:

```bash
ip -br link
ip -br addr
ip route
```

Identify the active Ethernet interface (often `eth0`, `ens33`, or similar). Record:
- VM name and operating system
- Interface name and state
- IPv4 address and prefix
- Route information

Do not assume the interface is named `eth0`.

## 5. Addressing plan

If the VMware Host-only network provides DHCP, you may use the assigned addresses as long as both VMs are in the same subnet and no address conflict exists.

If you need static addresses, use the actual Host-only subnet. Example only:

| VM | Example address |
|---|---|
| Kali | `192.168.56.20/24` |
| Ubuntu | `192.168.56.30/24` |

Before assigning static addresses, check VMware's Host-only network configuration and DHCP range. Choose unused addresses outside the DHCP pool, or reserve them appropriately. Do not use these example addresses if they do not match your network.

For a temporary test on a disposable VM, NetworkManager's `nmcli` can configure an existing connection profile. First inspect profiles:

```bash
nmcli connection show
nmcli device status
```

If you are not confident which connection profile is active, do not modify it; use DHCP or ask for help with the actual output. Persistent network configuration varies by distribution and profile.

## 6. Test Kali to Ubuntu

On Ubuntu, find and record its actual IPv4 address from `ip -br addr`.

On Kali, replace the placeholder with that actual address:

```bash
ping -c 4 <UBUNTU_IP>
```

Record transmitted, received, and packet-loss values. If ping fails, do not immediately assume the network is broken: verify both VMs are on the same Host-only network, addresses/subnet masks match, interfaces are up, and the target permits ICMP.

## 7. Test Ubuntu to Kali

On Kali, identify its actual IPv4 address. On Ubuntu, run:

```bash
ping -c 4 <KALI_IP>
```

Record the actual result. A successful test in one direction does not automatically prove the reverse direction works.

## 8. Inspect neighbor (ARP) tables

After pinging, run on both VMs:

```bash
ip neigh
```

Look for the peer's actual IP address and a resolved link-layer address (MAC). States such as `REACHABLE`, `STALE`, or `DELAY` can occur depending on timing; an entry may change state after some time.

Optional legacy command, if installed:

```bash
arp -n
```

## 9. Troubleshooting

- **No IPv4 address:** check adapter connection, DHCP service, and `ip -br addr`.
- **Different subnets:** confirm both adapters use the same Host-only network and compatible prefixes.
- **Wrong VMware network:** power off both VMs and select the same Host-only VMnet.
- **Interface DOWN:** inspect `ip -br link`; check the VM adapter connection and network manager.
- **Ping fails:** verify the destination IP, subnet, interface state, and local firewall/ICMP policy.
- **No neighbor entry:** ping the peer first, then run `ip neigh` again.
- **Address conflict:** stop and choose unique addresses; do not continue with duplicate IPs.

Do not disable the firewall globally just to make ping work. If a firewall rule needs adjustment, use a narrow, temporary rule on your own lab VM and document the change.

## 10. Evidence checklist

Save screenshots or sanitized terminal output from:
- VMware network adapter settings for both VMs (showing the same Host-only network).
- `ip -br addr` and `ip route` on Kali.
- `ip -br addr` and `ip route` on Ubuntu.
- Kali-to-Ubuntu ping result.
- Ubuntu-to-Kali ping result.
- `ip neigh` output on both VMs.

Redact unrelated public addresses, usernames, host details, and other sensitive information before publishing.

## 11. Questions

1. What is a Host-only network?
2. Why must both VMs use the same virtual network?
3. What does the `/24` prefix indicate?
4. Why is a default gateway not required for two hosts communicating within the same subnet?
5. What is ARP used for on an IPv4 local network?
6. Why should each VM have a unique IP address?
7. Why can ping fail even when both VMs have valid IP addresses?

## 12. Completion criteria

Mark this lab **Completed** only after you:
- Configure both VMs on the same isolated virtual network.
- Record actual interface names, addresses, and routes.
- Test connectivity in both directions and record actual results.
- Inspect and explain neighbor table entries.
- Resolve or document any issues.
- Save sanitized evidence and answer the review questions.

**Current repository status:** Reference prepared only. No VMware settings or VM network configurations were changed by the assistant, and no connectivity tests were run on the learner's VMs.
