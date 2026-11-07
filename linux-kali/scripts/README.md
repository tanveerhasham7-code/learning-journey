# Linux Lab Scripts

Scripts in this directory are educational examples for systems you own or are authorized to administer.

## system_inventory.sh
Collects basic OS, kernel, user, network interface, route, listening socket, disk and memory information.

Run:
```bash
chmod +x system_inventory.sh
./system_inventory.sh
```

The script is read-only apart from normal command execution. Review its output before sharing: hostnames, usernames and IP addresses may be sensitive in some environments.

Do not add passwords, API keys, private keys or other secrets to scripts or repository history.
