# 04 — Security Controls and Defense in Depth

A security control is a safeguard used to reduce risk.

## By category
- Administrative: policies, training, approvals, risk assessments.
- Technical: MFA, firewalls, endpoint protection, encryption, access control, logging.
- Physical: locks, badges, cameras, secure rooms.

## By purpose
- Preventive: aims to stop an unwanted event.
- Detective: identifies suspicious or harmful activity.
- Corrective: fixes a problem or reduces its effects.
- Deterrent: discourages unwanted behavior.
- Recovery: restores service or data.
- Compensating: provides an alternative safeguard when the preferred control is not feasible.

One control can have multiple purposes. Endpoint protection may block a threat and generate an alert.

## Defense in depth
Use multiple layers so failure of one control does not automatically cause compromise: user awareness, MFA, email filtering, endpoint protection, network segmentation, least privilege, centralized logs, backups, and incident response.

## Baselines and hardening
A baseline is an approved minimum configuration. Hardening reduces unnecessary exposure by disabling unused services, removing default credentials, patching, limiting permissions, enabling logs, and securely configuring services. Test changes and document them.

## Practical
Choose a phishing risk. List one administrative, one technical, and one detective control. Explain each control's purpose and limitation. Identify what helps if prevention fails.
