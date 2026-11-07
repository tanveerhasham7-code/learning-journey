# 07 — Wireless Networking and Wi-Fi Security

## 1. Wi-Fi fundamentals
Wi-Fi is a family of IEEE 802.11 wireless LAN standards. A client communicates with an access point (AP) over radio frequencies. The AP may bridge traffic into wired VLANs and enforce authentication and policy.

Important concepts: SSID (network name), BSSID (radio/AP identifier), channels, channel width, 2.4/5/6 GHz bands, roaming, signal strength and interference.

## 2. Authentication and encryption
- **WPA2-Personal:** commonly uses a pre-shared passphrase with AES-CCMP.
- **WPA3-Personal:** uses SAE to improve resistance to offline password guessing compared with traditional PSK handshakes.
- **Enterprise Wi-Fi:** commonly uses 802.1X/EAP with a RADIUS authentication server and per-user/device identity.
- **Open Wi-Fi:** provides no link-layer authentication/encryption unless enhanced open mechanisms such as OWE are used; application-layer HTTPS remains important.

Use modern supported security modes. Avoid WEP and obsolete WPA/TKIP configurations.

## 3. Enterprise wireless design
Separate staff, guest, IoT and management devices. Map SSIDs to appropriate VLANs or policy groups. Guest access should be isolated from internal systems. IoT devices should have only the services they need.

## 4. Common risks
- Weak or reused passphrases
- Rogue or evil-twin access points
- Misconfigured guest isolation
- WPS exposure on devices that support it
- Unpatched AP firmware and insecure management
- Poor certificate validation in enterprise EAP deployments
- Unmonitored unmanaged wireless devices

## 5. Defensive controls
Use WPA3 or WPA2-AES where WPA3 is unavailable; use 802.1X for enterprise identity; validate server certificates; disable unnecessary WPS; patch APs; restrict AP management; use guest isolation; inventory APs; monitor for rogue devices; and review authentication logs.

## Practical lab
In a home lab you own, inspect the router's security configuration without attempting to access networks belonging to others. Record SSID security mode, firmware version, guest isolation and management exposure. In a simulator, design staff/guest/IoT wireless segments and document allowed flows.

## Security analyst view
A wireless alert needs context: AP identity, channel, signal, client association, authentication result, DHCP lease and subsequent network activity. A duplicate SSID by itself is not proof of an evil twin.
