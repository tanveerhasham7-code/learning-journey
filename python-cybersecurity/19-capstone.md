# 19 — Capstone: Defensive Python Triage Toolkit

## Objective
Build a read-only Python toolkit that demonstrates programming and defensive analysis using synthetic input data.

## Required features
1. File hashing: calculate SHA-256 for files in a designated sample folder.
2. Log parsing: read synthetic CSV or JSON events and validate required fields.
3. Event summary: count event types and summarize failed-login patterns as review candidates.
4. IOC matching: compare supplied test indicators with synthetic event records.
5. Report: write JSON with collection time, input names, counts, matches and limitations.
6. Tests: cover normal, empty, malformed and missing-field cases.

## Safety requirements
Read only from a dedicated sample-data directory and write to a separate output directory. Never execute log content, contact external hosts or scan networks. Do not include secrets or personal data. A match or threshold is not proof of compromise.

## Suggested layout
~~~text
defensive-triage-toolkit/
  README.md
  requirements.txt
  data/
  scripts/
    main.py
    hashing.py
    log_parser.py
    ioc_matcher.py
  tests/
  output/
  evidence/
~~~

## Deliverables
Source code, synthetic sample data, unit-test results, example JSON report, setup instructions, lab report, limitations and sanitized screenshots of your actual run.

## Evaluation
Correctness, readability, input validation, error handling, safe defaults, tests, reproducibility and honest documentation. A small reliable tool is better than a large script you cannot explain.

## Reflection
What can each rule miss? What creates false positives? How would evidence be preserved in a real incident? What must never appear in a public report?
