# Lab Evidence and Portfolio Safety Guide

## What to capture
For each lab, keep:
- Lab number and title.
- Date performed and timezone.
- Lab environment and software versions.
- Objective and exact steps.
- Sanitized screenshots or synthetic sample records.
- Queries or configuration created by you.
- Observations and interpretation.
- Limitations, errors, and lessons learned.

## What not to publish
Never commit passwords, API keys, tokens, cookies, private certificates, recovery codes, personal email addresses, real customer data, HR/health/financial data, or unredacted security logs. Review screenshots carefully; terminals and dashboards often expose usernames, hostnames, public IP addresses, and secrets.

## Evidence quality
- Label generated records as synthetic.
- Distinguish a screenshot of configuration from proof that a detection worked.
- Include the test input and expected result.
- Include actual result and explain any difference.
- Record tool/version and relevant settings.
- Avoid editing evidence in a way that changes its meaning; redact sensitive details and disclose redaction.

## Suggested folder structure
    soc-analyst-siem/
      evidence/
        lab-01/
          README.md
          screenshot-01.png
          sample-events-sanitized.csv
        lab-02/
          README.md

## Git hygiene
Review files before commit. Use a secret scanner where available. If a secret is accidentally committed, revoke/rotate it immediately; deleting the line in a later commit does not make the secret safe. Follow the organization's incident process for exposed data.

## Evidence note template
- Lab:
- Date:
- Environment:
- Evidence filenames:
- What the evidence demonstrates:
- What it does not demonstrate:
- Redactions made:
- Lessons learned:
