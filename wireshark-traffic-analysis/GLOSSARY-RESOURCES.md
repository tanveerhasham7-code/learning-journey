# Glossary and Learning Resources

## Glossary
- **ARP:** resolves a local IPv4 next-hop address to a MAC address.
- **BPF:** Berkeley Packet Filter syntax used by many capture tools.
- **Beaconing:** repeated communication at intervals; can be benign or malicious.
- **Capture filter:** filter applied before packets are saved.
- **Display filter:** Wireshark expression that controls which saved packets are shown.
- **Conversation:** packets exchanged between endpoints.
- **DHCP:** automatic IP configuration protocol.
- **DNS:** distributed naming system.
- **Encapsulation:** adding protocol headers as data moves down network layers.
- **Exfiltration:** unauthorized movement of data out of an environment.
- **Flow:** summary of communication between endpoints.
- **Handshake:** protocol exchange to establish connection/security parameters.
- **ICMP:** network control and error-reporting protocol.
- **PCAP/PCAPNG:** packet capture file formats.
- **Retransmission:** re-sending data when delivery is not acknowledged or is considered missing.
- **SYN/ACK/FIN/RST:** important TCP flags.
- **TShark:** Wireshark command-line packet analyzer.
- **TLS:** protocol providing encryption and integrity for network connections.

## Official resources
- Wireshark User Guide: https://www.wireshark.org/docs/wsug_html_chunked/
- Display Filter Reference: https://www.wireshark.org/docs/dfref/
- Official downloads: https://www.wireshark.org/download.html
- TShark manual: https://www.wireshark.org/docs/man-pages/tshark.html
- Wireshark Wiki: https://wiki.wireshark.org/
- Sample captures: https://wiki.wireshark.org/SampleCaptures
- NIST incident handling publication: https://csrc.nist.gov/pubs/sp/800/61/r2/final

## Study advice
Do not memorize filters without understanding their fields. Ask what a filter tests, what it hides and what conclusion it can or cannot support. Learn normal traffic before investigating suspicious patterns.