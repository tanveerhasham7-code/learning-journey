# 16 — Defensive Security Automation

## File integrity
Create a baseline of SHA-256 hashes for a lab folder and compare later versions to identify added, removed or changed files. Protect the baseline; if both files and manifest can be changed, a simple comparison can be defeated.

## IOC matching
Indicators can include hashes, domains, IP addresses and URLs. Match supplied trusted indicators against synthetic logs. Record source, date and confidence. Indicators can become stale or refer to benign shared infrastructure.

## Log triage
Normalize timestamps, group events and summarize patterns. Do not declare an incident from one signal. Correlate endpoint, identity and network context.

## Asset inventory and alert enrichment
Collect only approved device attributes. Add context from approved internal sources or trusted intelligence services. Respect privacy, terms and API limits. Preserve original alert fields.

## Safe script design
- Define authorized scope.
- Default to read-only behavior.
- Validate all input.
- Use timeouts and bounded resource use.
- Log actions without secrets.
- Avoid shell execution with untrusted input.
- Make destructive actions opt-in and reversible.
- Test with synthetic data.
- Document false positives and limitations.

## Small IOC example
~~~python
indicators = {"bad.example", "203.0.113.10"}
observed = ["portal.example", "bad.example"]
matches = sorted(set(observed) & indicators)
print(matches)
~~~

These are documentation/test values. A match is an investigation lead, not proof of compromise.

## Exercise
Read a synthetic IOC JSON file and synthetic DNS CSV, output matching records with timestamps and explain false positives.
