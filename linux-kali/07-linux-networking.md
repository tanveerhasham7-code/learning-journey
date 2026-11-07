# 07 — Linux Networking Administration

## Network interfaces and addresses
```bash
ip link
ip addr
ip -br addr
ip route
ip neigh
hostname -I
```
ip link shows interfaces; ip addr shows addresses; ip route shows the routing table; ip neigh displays neighbor/ARP cache.

## Connectivity checks
```bash
ping -c 4 192.168.56.1
tracepath example.com
traceroute example.com
curl -I https://example.com
```
Ping uses ICMP and may be blocked. A failed ping alone does not prove a host is offline. Test the required service separately.

## DNS
```bash
getent hosts example.com
resolvectl status
dig example.com
nslookup example.com
```
DNS resolves names to records such as A and AAAA. A DNS failure can make a working IP connection appear broken.

## Listening sockets and ports
```bash
ss -tulpen
ss -tan
sudo lsof -i -P -n
```
-t means TCP, -u UDP, -l listening, -p process and -n numeric output. A listening port is not necessarily exposed externally; interface binding and firewall policy matter.

## Host firewall overview
Ubuntu commonly uses UFW as a simpler frontend to the underlying packet-filtering framework.
```bash
sudo ufw status verbose
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status numbered
```
Before enabling a firewall on a remote server, ensure your management connection is allowed or you may lock yourself out. Practice in a VM console first.

## SSH client basics
```bash
ssh username@192.168.56.10
ssh -v username@192.168.56.10
scp report.txt username@192.168.56.10:/home/username/
```
SSH provides encrypted remote administration. Verify host keys and do not disable host-key checking as a routine workaround.

## Lab
1. Record the VM interface and address.
2. Check the route and neighbor table.
3. Ping another VM in your isolated subnet.
4. Resolve a domain using dig.
5. Inspect listening sockets with ss.
6. Identify which service owns each expected listening port.
7. Enable UFW only after allowing the lab's required management service.
8. Document expected versus observed traffic.

## Security connection
Network interfaces, routes, DNS configuration, listening ports and firewall rules are essential evidence during incident response and system hardening.
