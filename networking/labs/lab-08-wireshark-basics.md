# Lab 08 — Wireshark Basics: Packet Capture and Analysis

**Date performed:** 16 November 2026  
**Status:** Completed — practical capture and screenshot evidence documented  
**Tool:** Wireshark on Windows, capturing from the Wi-Fi interface  
**Capture file:** `lab-08-network-traffic.pcapng` (saved locally by the learner; the PCAPNG file itself was not uploaded to this repository)

## 1. Objective

Capture traffic generated during the learner's own network activity and use Wireshark display filters to inspect ICMP, DNS, and TCP packets. Identify packet addresses, protocol fields, and TCP control flags.

## 2. Capture environment

- Capture interface: Wi-Fi
- Local IPv4 address visible in the capture: `192.168.1.10`
- ICMP test destination: `8.8.8.8`
- DNS resolver visible in the capture: `192.168.1.1`

The capture also contains ordinary background traffic from the active Wi-Fi connection. The analysis below focuses on the selected protocol packets and avoids treating unrelated background packets as part of the test.

## 3. ICMP packet analysis

The learner generated four ping requests to `8.8.8.8` using:

```cmd
ping 8.8.8.8 -n 4
```

The command prompt screenshot records four replies and **0% packet loss**. Wireshark's `icmp` display filter shows Echo Request packets from `192.168.1.10` to `8.8.8.8`, followed by Echo Reply packets in the reverse direction.

The packet details show:
- Echo Request type: **8**
- Echo Reply type: **0**
- Code: **0**
- The request packet's IPv4 TTL: **128**
- The reply packets' TTL shown in the packet list: **118**

### ICMP evidence

**Screenshot 1 — Live Wi-Fi capture before applying a protocol filter**

![Live Wi-Fi packet capture](screenshots/lab-08/Screenshot%202026-11-16%20195633.png)

**Screenshot 2 — Wi-Fi capture with additional traffic visible**

![Wi-Fi capture traffic](screenshots/lab-08/Screenshot%202026-11-16%20200043.png)

**Screenshot 3 — Successful ping test to 8.8.8.8 (4 replies, 0% loss)**

![Ping test output](screenshots/lab-08/Screenshot%202026-11-16%20200103.png)

**Screenshot 4 — ICMP display filter showing Echo Requests and Echo Replies**

![ICMP packet list](screenshots/lab-08/Screenshot%202026-11-16%20200217.png)

**Screenshot 5 — ICMP Echo Request details, including Type 8 and Code 0**

![ICMP Echo Request details](screenshots/lab-08/Screenshot%202026-11-16%20200425.png)

**Screenshot 6 — ICMP packet details and sequence information**

![ICMP sequence details](screenshots/lab-08/Screenshot%202026-11-16%20200714.png)

**Screenshot 7 — IPv4 details showing TTL 128 and ICMP Echo Request**

![IPv4 TTL and ICMP details](screenshots/lab-08/Screenshot%202026-11-16%20200855.png)

## 4. DNS packet analysis

The learner applied the `dns` display filter and inspected DNS traffic between the local host `192.168.1.10` and resolver `192.168.1.1`.

The screenshots show DNS queries and responses for names including `clients4.google.com`, `www.googleapis.com`, and `web.whatsapp.com`. One visible DNS response for `www.googleapis.com` has the response code **Refused**; other visible responses include returned records, such as a CNAME and an A record for `clients4.google.com`. Therefore, this capture demonstrates DNS packet inspection, but it does not establish that every DNS query succeeded.

### DNS evidence

**Screenshot 8 — DNS display filter and DNS query/response packets**

![DNS packet list](screenshots/lab-08/Screenshot%202026-11-16%20201040.png)

**Screenshot 9 — DNS response details showing the Refused response code**

![DNS response details](screenshots/lab-08/Screenshot%202026-11-16%20201153.png)

## 5. TCP packet analysis

The learner applied the `tcp` display filter and then inspected TCP control flags with:

```text
tcp.flags.syn == 1
tcp.flags.ack == 1
```

The packet list includes a TCP SYN, a corresponding SYN-ACK, and ACK traffic for a connection involving `52.123.128.14:443`. Other SYN retransmissions are also visible in the capture; these are recorded as observed and are not described as successful connections.

The three-way handshake is:
1. **SYN** — client requests a TCP connection.
2. **SYN-ACK** — server acknowledges the request and sends its SYN.
3. **ACK** — client acknowledges the server's SYN.

### TCP evidence

**Screenshot 10 — TCP display filter and TCP packets**

![TCP packet list](screenshots/lab-08/Screenshot%202026-11-16%20201516.png)

**Screenshot 11 — SYN filter showing SYN packets, SYN-ACK traffic, and retransmissions**

![TCP SYN flag filter](screenshots/lab-08/Screenshot%202026-11-16%20201648.png)

**Screenshot 12 — ACK filter showing TCP acknowledgement packets**

![TCP ACK flag filter](screenshots/lab-08/Screenshot%202026-11-16%20201749.png)

## 6. Key learning outcomes

- Started a live capture on the Wi-Fi interface.
- Used the `icmp`, `dns`, and `tcp` display filters.
- Distinguished ICMP Echo Request and Echo Reply packets.
- Identified source and destination IPv4 addresses.
- Inspected the IPv4 TTL field.
- Read DNS query and response information, including a Refused response.
- Recognized TCP SYN, SYN-ACK, ACK flags and retransmission entries.
- Saved the capture as `lab-08-network-traffic.pcapng` locally.

## 7. Security and privacy note

Only the learner's own Wi-Fi traffic was captured for this exercise. A live capture may include unrelated background network metadata, so capture files and screenshots should be reviewed for personal information before sharing. Do not capture or inspect other people's traffic without permission.

## 8. Conclusion

The learner completed a beginner Wireshark exercise by capturing Wi-Fi traffic and examining ICMP, DNS, and TCP packets. The screenshots provide evidence of the filters and protocol fields inspected. The DNS evidence includes both returned records and a Refused response, while the TCP capture includes retransmissions as well as handshake-related flags. The original PCAPNG file was saved locally; it is not included in this repository.
