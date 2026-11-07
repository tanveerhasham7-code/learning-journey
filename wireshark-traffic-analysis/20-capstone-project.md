# 20 — Capstone: Investigate a Simulated Network Security Event

## Scenario
A fictional employee workstation triggers an alert for unusual outbound communication. The SOC receives a short packet capture plus synthetic DHCP, DNS and firewall logs. Determine what the evidence supports, what remains unknown and what should happen next.

## Scope and safety
Use synthetic data, a trusted training PCAP or traffic generated in an isolated lab. Do not create malware, exfiltrate real data, access third-party systems or publish sensitive captures.

## Deliverables
1. **Case definition:** alert source, time range/timezone, in-scope assets, capture point, authorization and limitations.
2. **Traffic overview:** Protocol Hierarchy, Endpoints and Conversations. Identify top talkers, protocols and unusual destinations.
3. **Protocol analysis:** inspect DNS, TCP/UDP, TLS and ICMP. Record packet numbers, timestamps, addresses, ports, flags, response codes and visible TLS metadata.
4. **Hypothesis testing:** compare at least two explanations. For example, repeated connections may be a legitimate updater or suspicious beacon-like behavior.
5. **Correlation:** use synthetic DHCP lease data to map IP to device at the event time; correlate DNS and firewall records.
6. **Timeline:** normalize times to UTC and cite source/event/evidence for each entry.
7. **Findings:** separate observed facts, hypotheses, conclusions and unknowns. Assign confidence and explain it.
8. **Recommendations:** propose proportionate next steps such as endpoint review, asset-owner validation, DNS/firewall checks and monitoring improvements.

## Final report
1. Executive summary
2. Scope and authorization
3. Evidence inventory and integrity
4. Network overview
5. Packet-level analysis
6. Correlated timeline
7. Findings and alternative explanations
8. Impact assessment
9. Recommendations
10. Limitations and lessons learned

## Portfolio standard
Upload your own sanitized report, topology, filter notes and screenshots after completing the project. Label synthetic data and simulated results clearly. Never claim this scenario was a real-world incident.