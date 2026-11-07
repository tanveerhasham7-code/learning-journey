# Detection Rule Specification Template

## Identification
- Rule name:
- Rule ID:
- Owner:
- Version:
- Status:
- Created / reviewed date:

## Threat hypothesis
What suspicious behavior should this rule identify? Why does it matter to the organization?

## Data requirements
- Sources:
- Required fields:
- Collection prerequisites:
- Known coverage gaps:

## Logic
- Query / pseudocode:
- Evaluation schedule:
- Time window:
- Grouping keys:
- Threshold and rationale:

## Alert metadata
- Severity:
- Confidence:
- Priority guidance:
- ATT&CK mapping (if evidence supports it):

## Triage guidance
1. Validate raw events and parsing.
2. Identify affected user, host, and asset criticality.
3. Review surrounding activity and benign explanations.
4. Correlate with other telemetry.
5. Document facts, hypotheses, and unknowns.
6. Escalate or close under approved procedure.

## False positives and exceptions
- Expected benign activity:
- Narrow exclusions:
- Exception owner:
- Expiry/review date:

## Test plan
- Positive test:
- Benign lookalike:
- Missing field:
- Duplicate event:
- Boundary threshold:
- Delayed ingestion:
- Expected outcome:

## Operations
- Routing / case owner:
- Dependencies:
- Monitoring / health check:
- Change history:
- Retirement criteria:
