# 14 — Statistics, Conversations and Expert Information

## 1. Why statistics matter
A packet list can be overwhelming. Wireshark statistics summarize endpoints, conversations, protocols, packet lengths and traffic over time. They help prioritize investigation.

## 2. Useful menu areas
Depending on version, explore:
- Statistics → Protocol Hierarchy
- Statistics → Conversations
- Statistics → Endpoints
- Statistics → I/O Graphs
- Statistics → Flow Graph
- Analyze → Expert Information

Menu labels can differ slightly across releases.

## 3. Protocol Hierarchy
Shows how much captured traffic belongs to each decoded protocol. Use it to identify dominant protocols or unexpected protocol families. A high percentage of TLS is common in modern environments; it is not inherently suspicious.

## 4. Endpoints and Conversations
Endpoints summarize hosts and traffic. Conversations show communication pairs, often including packet and byte counts. Sort by bytes or packets to find major talkers.

A large transfer may be backup, software update, video or exfiltration. Determine asset role, destination reputation, process attribution and business context before deciding.

## 5. I/O Graphs
I/O Graphs show packet/byte rates over time. A sudden spike can correspond to a file transfer, update, scan, broadcast storm or attack. Use filters to graph selected traffic separately.

## 6. Flow Graph
A flow graph helps visualize packet order and direction between endpoints. It is useful for TCP handshake analysis, DNS exchanges and multi-step protocols.

## 7. Expert Information
Expert Information groups events such as retransmissions, malformed packets, warnings and notes. These are diagnostic hints, not a verdict. Some events are normal in imperfect networks or caused by capture artifacts.

## Practical lab
Capture a short set of normal lab activity: DNS lookup, ping and web request. Open Protocol Hierarchy, Conversations, Endpoints and I/O Graphs. Identify the busiest conversation and explain whether it is expected.

## Analyst tip
Use statistics to decide where to look next, then return to individual packets to validate the story. Summaries alone are not sufficient evidence.
