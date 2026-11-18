# Linux Lab 7 — Network Diagnostics

**Status: Reference prepared — learner execution and evidence pending.**

## 1. Objective

Inspect the Kali VM's network configuration, test connectivity to an Ubuntu VM on an authorized lab network, inspect neighbor information, test DNS when available, and review listening sockets.

Only test VMs and networks you own or are authorized to use.

## 2. Prepare the lab network

1. Open your virtualization software's network settings.
2. Set both Kali and Ubuntu VMs to the same **Host-only** or **Internal Network**.
3. Start both VMs.
4. Do not change bridged/network settings on a network you do not own or administer.

A same-subnet lab connection normally does not require an internet gateway. Host-only networking may also provide internet access depending on its configuration; Internal Network usually isolates the VMs from the host and internet.

## 3. Inspect Kali's network interfaces

On Kali, run:

```bash
ip -br addr
```

Identify the active interface (for example, `eth0`) and record its IPv4 address and prefix.

Then inspect routes:

```bash
ip route
```

Record the connected subnet and any default route, if present.

## 4. Inspect Ubuntu's network details

On Ubuntu, run:

```bash
ip -br addr
ip route
```

Record the active interface, IPv4 address/prefix and connected subnet.

### IP plan

Fill this table with the actual values shown by your VMs. Do not copy the example addresses unless you have configured and verified them.

| Device | Interface | Actual IPv4/prefix | Network mode |
|---|---|---|---|
| Kali | | | Host-only / Internal |
| Ubuntu | | | Host-only / Internal |

Confirm that both addresses belong to the same subnet before attempting the ping test. If they are not in the same subnet, stop and review the VM network settings and IP configuration rather than guessing.

## 5. Test connectivity

From Kali, ping the actual Ubuntu IPv4 address:

```bash
ping -c 4 <UBUNTU-IP>
```

Replace `<UBUNTU-IP>` with the real address shown on Ubuntu. Do not type the angle brackets.

Record packet transmitted/received counts and packet loss. Four replies indicate that ICMP connectivity worked during this test. No replies do not automatically prove the VM is offline; a firewall or network configuration may block ICMP.

If the ping fails:
- Recheck that both VMs use the same Host-only/Internal Network.
- Recheck both IP addresses and subnet prefixes.
- Check that both interfaces are up.
- Do not disable firewalls blindly; inspect the lab VM's policy first.

## 6. Inspect the neighbor table

On Kali, run:

```bash
ip neigh
```

Look for the Ubuntu IP address and record the neighbor state (for example, REACHABLE, STALE, DELAY or INCOMPLETE). A neighbor entry maps a local network IP to a link-layer address where applicable. Its state can change over time.

## 7. Test DNS (if DNS is available)

Run:

```bash
getent hosts google.com
```

If `nslookup` is installed, you can also run:

```bash
nslookup google.com
```

Record the actual result. DNS may fail on an isolated Internal Network or a Host-only network without a configured resolver/internet connection. That is a useful observation, not a reason to invent a successful result.

## 8. Inspect listening sockets

On Kali, run:

```bash
ss -tuln
```

This displays listening TCP and UDP sockets with numeric addresses/ports. Record any listening ports and their local bind addresses. This command does not identify every application process; do not assume a port belongs to a particular service without further evidence.

## 9. Network diagram

Complete this simple diagram using your actual VM network name and addresses:

```text
             Host-only / Internal Network: __________________

       Kali Linux VM                         Ubuntu VM
       Interface: __________                 Interface: __________
       IP/prefix: __________                 IP/prefix: __________
              |                                     |
              +-------------------------------------+
                    Same virtual network
```

No gateway should be drawn unless one is actually configured and observed.

## 10. Evidence checklist

Save screenshots or a terminal transcript showing:
- [ ] VM network mode for both VMs.
- [ ] Kali `ip -br addr` and `ip route`.
- [ ] Ubuntu `ip -br addr` and `ip route`.
- [ ] Ping command and actual result.
- [ ] Kali `ip neigh` output.
- [ ] DNS test output (including a genuine failure, if DNS is unavailable).
- [ ] `ss -tuln` output.
- [ ] Completed IP plan and network diagram.

Review evidence for private IPs, usernames, hostnames or other details before making it public.

## 11. Questions to answer

1. What is an IP address and what does the prefix (such as /24) represent?
2. What information does `ip route` show?
3. What does a successful ping confirm, and what does it not confirm?
4. What is the purpose of the neighbor table?
5. What is DNS used for?
6. What does `ss -tuln` display?

## 12. Completion criteria

Mark this lab **Completed** only after the learner has:
1. Connected both owned VMs to the same lab network.
2. Recorded the actual interface addresses and routes.
3. Tested Kali-to-Ubuntu connectivity and recorded the result.
4. Inspected the neighbor table, DNS behavior and listening sockets.
5. Completed the IP plan and network diagram.
6. Saved evidence or explicitly confirmed the actual observations.

**Current result:** The procedure and templates are prepared. The assistant has not configured or tested the learner's VMs; no connectivity, DNS or listening-port results are claimed.
