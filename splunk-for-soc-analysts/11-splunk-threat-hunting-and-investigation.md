# 11 — Threat Hunting and Investigation with Splunk

## Objectives
Turn a security hypothesis into a reproducible hunt and evidence-based conclusion.

## 1. Threat hunting
Threat hunting is a proactive, hypothesis-led search for suspicious behavior that may not have triggered an alert. It uses knowledge of threats, assets, normal activity, and available telemetry.

## 2. Define a hypothesis
Example: an account may have been used from an unusual source after repeated authentication failures. Define target behavior, entities, required logs, time window, normal baseline, and evidence that would support or weaken the idea.

## 3. Hunt workflow
1. State the hypothesis.
2. Identify data sources and required fields.
3. Validate data quality and time coverage.
4. Run bounded searches.
5. Pivot by account, host, IP, process, and time.
6. Compare with baseline and threat intelligence.
7. Build a timeline.
8. Record evidence, gaps, and conclusion.
9. Recommend detection improvements.

## 4. SPL patterns
    index=security earliest=-7d
    | stats count by user src
    | sort - count

    index=endpoint earliest=-24h
    | table _time host user parent_process process_name command_line
    | sort _time

Adapt fields to your dataset and validate every query.

## 5. Evidence and ATT&CK
Preserve original event references, timestamps, source, host, query, and timezone. Map observed behavior to MITRE ATT&CK only when evidence supports it. A technique match does not identify a threat actor.

## Practical task
Use synthetic events for a fictional account with multiple failures, a later success, and a process event. Build a timeline and separate known facts, unknowns, and recommended next steps.

## Knowledge check
1. Hunting versus alert triage?
2. Why define a hypothesis?
3. What should a timeline preserve?
4. When should ATT&CK mapping be used?

## References
- [Splunk Security Content](https://research.splunk.com/)
- [MITRE ATT&CK](https://attack.mitre.org/)
