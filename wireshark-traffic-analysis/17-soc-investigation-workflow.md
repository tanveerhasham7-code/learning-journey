# 17 — SOC Investigation Workflow and Evidence Handling

## 1. From alert to investigation
A network alert is a starting point. A SOC analyst should validate the alert, scope affected assets, preserve evidence and communicate clearly.

## 2. Triage questions
- What triggered the alert and which rule generated it?
- Which source and destination are involved?
- What time window and timezone apply?
- Is the asset known and who owns it?
- Is the traffic allowed, blocked or partially successful?
- Is there endpoint or identity evidence?
- Is there a known business reason?

## 3. Build a timeline
Normalize timestamps to a common timezone (often UTC in SOC platforms). Example structure:
| Time (UTC) | Source | Event | Evidence |
|---|---|---|---|
| 10:00:01 | Client A | DNS query | Packet 42 |
| 10:00:02 | Resolver | DNS answer | Packet 45 |
| 10:00:04 | Client A | TCP connection | Packets 50–52 |
| 10:00:08 | Firewall | Session allowed | Log event ID |

The table is illustrative. Use actual event data for a real report.

## 4. Correlation sources
- PCAP: packet-level sequence and protocol details
- DNS logs: queries and answers
- DHCP logs: address-to-client lease mapping
- Firewall: policy decision and session metadata
- NetFlow/IPFIX: communication volume and direction
- Endpoint EDR: process, user and host activity
- Identity logs: authentication and account context
- Asset inventory: owner and expected role

## 5. Evidence integrity
Preserve original files according to organizational policy. Record source, collection time, collector, timezone, file size and cryptographic hash. Analyze a working copy. Restrict access and retention. A hash helps detect later file changes; it does not prove that the original capture was complete or truthful.

## 6. Reporting observations vs conclusions
- **Observation:** “The host sent 120 DNS queries to the resolver in five minutes.”
- **Hypothesis:** “The pattern may be consistent with automated lookup behavior.”
- **Conclusion:** only after corroborating evidence and scope are assessed.

Include confidence and limitations. Avoid declaring compromise from a single packet.

## 7. Incident response handoff
Provide affected assets, time range, indicators, packet numbers, relevant filters, actions already taken, business impact, confidence and recommended next steps. Follow organizational escalation and containment policy.

## Practical lab
Create a timeline from a supplied synthetic event set or your own generated lab traffic. Correlate a DHCP lease, DNS query, TCP session and firewall decision. State what can and cannot be concluded.
