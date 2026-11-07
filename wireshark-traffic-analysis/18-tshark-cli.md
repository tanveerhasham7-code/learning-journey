# 18 — TShark Command-Line Analysis

## 1. What is TShark?
TShark is Wireshark's command-line packet analyzer. It is useful for repeatable analysis, automation and remote/headless systems. It uses the same core dissection engine and display-filter language.

## 2. Basic commands
Check installation:
```bash
tshark --version
```
Read a capture:
```bash
tshark -r lab.pcapng
```
Apply a display filter:
```bash
tshark -r lab.pcapng -Y "dns"
```
Show selected fields:
```bash
tshark -r lab.pcapng -Y "dns" -T fields -e frame.time -e ip.src -e ip.dst -e dns.qry.name
```
List interfaces (platform permissions apply):
```bash
tshark -D
```

## 3. Capture from an interface
Live capture requires appropriate permissions and authorization. Example structure:
```bash
tshark -i <YOUR_LAB_INTERFACE> -f "udp port 53" -a duration:30 -w dns-lab.pcapng
```
Use only your own lab interface. A 30-second automatic stop is included to limit collection. Do not run broad captures on networks you do not own.

## 4. Export packet fields
```bash
tshark -r lab.pcapng -Y "tcp.flags.syn == 1" -T fields -e frame.number -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
```
Use CSV output options when appropriate and protect exported data like the original capture.

## 5. Useful command options
- `-r`: read capture file
- `-w`: write capture file
- `-Y`: display filter
- `-f`: capture filter
- `-T fields`: structured field output
- `-e`: choose output field
- `-a duration:30`: stop after duration
- `-q`: quiet output in suitable workflows

Check `tshark --help` and the official documentation for your installed version.

## 6. Automation caution
When using scripts, validate input paths, handle errors, protect output and avoid logging sensitive packet fields. Do not treat parser output as a security verdict.

## Practical lab
Use TShark to read a lab PCAP, extract DNS query names and TCP SYN metadata, save output to a local CSV, then compare the result with the Wireshark GUI.
