# 11 — Useful Networking Commands

Run commands only on your own devices or authorized lab systems. Some commands require administrator/root privileges.

## Windows
```powershell
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /flushdns
ping 192.168.1.1
tracert example.com
nslookup example.com
arp -a
route print
netstat -ano
```
- `ipconfig /all`: IP, gateway, DNS and adapter details.
- `ping`: basic reachability test.
- `tracert`: path discovery.
- `netstat -ano`: connections/listeners with process IDs.

## Linux
```bash
ip addr
ip link
ip route
ip neigh
ping -c 4 192.168.1.1
traceroute example.com
tracepath example.com
ss -tulpen
ss -tunap
dig example.com
nslookup example.com
resolvectl status
sudo tcpdump -i any -nn
```
- `ip addr`: addresses on interfaces.
- `ip route`: routing table.
- `ss`: sockets and listening services.
- `tcpdump`: command-line packet capture; capture only authorized traffic.

## Cisco IOS-style verification
```text
show ip interface brief
show interfaces status
show vlan brief
show interfaces trunk
show mac address-table
show ip route
show running-config
show access-lists
```

## A disciplined troubleshooting sequence
1. Confirm link/interface.
2. Check local IP and subnet mask.
3. Check gateway and route.
4. Test loopback, own IP, gateway, then remote IP.
5. Test DNS separately from IP connectivity.
6. Check firewall and service listener.
7. Capture packets if the cause is still unclear.

Command availability and syntax can vary by OS and network-device model.
