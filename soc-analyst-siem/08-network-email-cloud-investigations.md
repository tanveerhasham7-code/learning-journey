# 08 — Network, Email, Web, and Cloud Investigations

## Network investigation
Network evidence helps determine which systems communicated, when, over which protocol, and whether the communication was allowed or blocked. Common sources include firewall, DNS, proxy, VPN, DHCP, IDS/IPS, NetFlow/IPFIX, and packet capture.

### Core concepts to know
Understand IP addressing and subnetting; TCP versus UDP; ports and common services; DNS resolution; DHCP leases; NAT; routing; TLS; HTTP methods and status codes; proxies; VPNs; and the difference between packet payload and flow metadata.

### Investigation questions
- Which internal host initiated the connection?
- What destination, port, protocol, and direction were involved?
- Was the connection allowed, blocked, reset, or unanswered?
- What DNS name resolved to the destination?
- Is the destination expected for this host, user, and application?
- Was the connection preceded by suspicious process or sign-in activity?
- Is the volume, timing, or destination rare compared with baseline?

Do not treat a single unusual port or geolocation result as proof of malicious activity.

## DNS investigations
Review query name, query type, response code, answer, client, resolver, timestamp, and frequency. Investigate rare domains, unusual query bursts, high NXDOMAIN rates, suspicious subdomains, and hosts querying domains unrelated to their role. Consider software updates, content delivery networks, security tools, and internal naming systems as benign explanations.

## Web and proxy investigations
Review URL/domain, method, status code, user agent, user, source device, response size, category, and action. Look for unusual downloads, repeated authentication failures, unexpected uploads, suspicious redirects, and access to newly observed domains. URLs may contain tokens or personal data; redact before sharing.

## Email investigations
Trace sender, recipient, envelope details, message ID, authentication results (SPF/DKIM/DMARC), delivery path, attachment hashes, URLs, and user actions. Check mailbox rules, forwarding, delegated access, OAuth grants, and sign-in history after suspected phishing. Do not open suspicious attachments on a normal workstation.

## Cloud investigations
Cloud control-plane audit logs show administrative actions and API calls. Review actor identity, role, source, target resource, action, result, region, user agent, and session context. Investigate unusual role assignments, access-key creation, storage policy changes, public exposure, unusual data reads, disabled logging, and workload changes.

## Correlation example
A user clicks a phishing link, authenticates to a fake page, then a new mailbox forwarding rule appears. Correlate email trace and click telemetry, identity sign-in/MFA logs, mailbox audit events, and endpoint browser/process records. Confirm whether the rule was user-created or attacker-created before concluding compromise.

## Practical exercise
Build a synthetic investigation timeline combining DNS, proxy, firewall, email, and identity events. Mark each observation as fact, hypothesis, or unknown. State what additional source would increase confidence.

## Knowledge check
1. What can DNS logs reveal that firewall logs may not?
2. Why inspect mailbox rules after phishing?
3. Name key fields in a cloud audit event.
4. Why is a destination IP reputation result insufficient?
5. What evidence links an endpoint process to a network connection?
