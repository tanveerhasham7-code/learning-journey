# 02 — Install and Configure Wireshark

## 1. What you need
- A supported Windows, macOS or Linux computer.
- Wireshark from its official download page: https://www.wireshark.org/download.html
- On Windows, the installer may offer Npcap, which provides packet capture support.
- On Linux, capture permissions may require distribution-specific setup. Avoid running the whole desktop as root simply to capture packets.

Always download installers from the official project site or trusted OS repositories. Verify package source and updates.

## 2. Installation overview
**Windows:** download the official installer, follow the setup wizard, install Npcap when needed, then launch Wireshark. Npcap installation options and permissions depend on the system.

**Ubuntu/Debian-based Linux:** install using the distribution package manager, for example:
```bash
sudo apt update
sudo apt install wireshark
```
Some distributions ask whether non-root users may capture packets. Follow the distribution's security guidance. Group membership changes may require a new login. Do not grant broad privileges without understanding them.

**macOS:** use the official package and follow its permission prompts. Capture access is controlled by macOS and the installed capture component.

## 3. First launch
You will see available interfaces, often Ethernet, Wi-Fi, loopback and virtual adapters. Activity graphs help identify interfaces currently carrying traffic.

Choose the interface that carries your test traffic. If unsure, start a brief capture on one interface, generate a DNS lookup or ping from your own device, and see which interface shows packets.

## 4. Main interface areas
- **Menu/toolbar:** open, save, start/stop capture and configure options.
- **Interface list:** choose where to capture.
- **Display filter bar:** filter packets already captured.
- **Packet list:** one row per captured packet.
- **Packet details:** decoded protocol fields for selected packet.
- **Packet bytes:** raw bytes and ASCII interpretation where printable.

## 5. Save and reopen captures
Use File → Save As to save a PCAPNG capture. Use meaningful names, such as `lab-03-dns-test.pcapng`. Do not include sensitive hostnames or personal identifiers in public filenames.

Use a separate working copy for analysis. Keep original evidence protected and read-only when handling an authorized investigation.

## 6. Interface and permission troubleshooting
If no interfaces appear:
- Check Npcap/capture component installation.
- Check interface state and OS permissions.
- Restart Wireshark after permission changes.
- Confirm a VPN or VM adapter is not the actual path for the traffic.
- Consult official OS and Wireshark documentation.

## Practical exercise
Install Wireshark, identify active interfaces, capture 30 seconds of your own lab traffic, stop, save the capture and reopen it. Record the interface name and why you selected it.

## Security note
Packet capture can expose private data. Use short captures and isolated test traffic. Never capture other people's traffic simply because your adapter makes it visible.
