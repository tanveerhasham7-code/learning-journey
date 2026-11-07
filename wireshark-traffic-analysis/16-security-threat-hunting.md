# 16 — Security Monitoring and Threat Hunting with Traffic

## 1. Start from a hypothesis
Threat hunting asks a focused question and tests it with evidence. Examples:
- Is a workstation contacting many internal hosts on a new service?
- Is a server making repeated outbound connections at regular intervals?
- Is a client generating unusual DNS query patterns?
- Is a device transferring much more data than its baseline?

Avoid hunting by random filter alone. Define the host, timeframe, expected behavior and possible benign explanations.

## 2. Scanning indicators
Potential clues include one source contacting many destination ports or hosts, repeated SYNs without completed sessions, and sequential address/port patterns. Vulnerability scanners, inventory systems and monitoring tools can create similar traffic.

Validate source ownership, scan schedule, change tickets and endpoint process telemetry.

## 3. Beacon-like connections
Malware may periodically contact command-and-control infrastructure. Potential clues include repeated connections at regular intervals, consistent packet sizes, unusual destinations and repeated failed connections.

Legitimate agents, software update services, health checks and cloud applications also beacon periodically. Use timing analysis with DNS, endpoint process and threat-intelligence context.

## 4. DNS tunneling concepts
Tunneling can encode data in DNS labels or records. Potential signals:
- Long or high-entropy subdomains
- Unusually high query frequency
- Many unique subdomains under one domain
- Large TXT responses or unusual record usage
- Repeated queries with structured patterns

These signals also occur in legitimate services. Do not conclude exfiltration from one long query. Review volume, entropy, response sizes, resolver logs, endpoint process and approved application use.

## 5. Data exfiltration indicators
Look for unusual outbound byte volume, rare destinations, unexpected protocols, transfers outside normal hours and traffic from sensitive systems. Encryption limits payload visibility; flow records and endpoint telemetry become important.

## 6. Lateral movement clues
Potential signals include one workstation connecting to many peers over administrative protocols, unusual SMB/RDP/SSH patterns, authentication failures and new service access. Confirm with Windows/Linux event logs and identity telemetry.

## 7. C2 and threat intelligence
IP/domain reputation is context, not proof. Shared hosting, CDNs and cloud platforms can host both benign and malicious services. Validate timestamp, domain resolution, certificate, process, user and asset role.

## 8. Threat-hunting workflow
1. Define hypothesis.
2. Select time window and assets.
3. Filter relevant traffic.
4. Build endpoint/conversation summaries.
5. Identify anomalies against baseline.
6. Generate benign explanations.
7. Correlate with endpoint and server logs.
8. Record evidence and confidence.
9. Escalate according to incident policy.

## Practical lab
Use synthetic traffic or a trusted training PCAP. Find one example of a repeated connection pattern, one unusual DNS pattern and one high-volume conversation. For each, write observation, benign explanations, next evidence and conclusion confidence.

## Safety
This module is defensive analysis. Do not generate malware, command-and-control traffic, credential theft or exfiltration. Use synthetic examples and authorized captures.
