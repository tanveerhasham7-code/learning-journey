# 12 — Automation Rules and Logic Apps Playbooks

## 1. Automation in Sentinel
Automation rules help manage incident workflows, such as assigning an owner, changing status, adding tags or triggering a playbook. Playbooks are commonly built with Azure Logic Apps to connect services and perform workflow actions.

## 2. Safe automation principles
- Human approval for disruptive or high-impact actions.
- Least-privilege managed identity or connector permissions.
- Input validation and allowlists.
- Idempotency and duplicate-event handling.
- Error handling, logging and rollback planning.
- Secrets stored securely, never in source code.
- Testing in a non-production environment.

## 3. Example workflow
New incident → automation rule applies a tag and assigns a queue → playbook enriches an IP using an approved source → analyst reviews the result → authorized responder decides next action.

Enrichment is safer than automatically blocking or disabling accounts.

## 4. Automation rule versus playbook
An automation rule controls Sentinel incident workflow and can invoke a playbook. A playbook is the Logic Apps workflow that performs defined steps. Exact triggers and supported actions depend on current service capabilities.

## 5. Design checklist
Document trigger, input schema, permissions, actions, external dependencies, error path, audit trail, human approval, test cases and disable/rollback procedure.

## 6. Practical task
Draw a non-destructive playbook that enriches an incident with asset owner and reputation context, then adds a note for analyst review. Do not implement automatic containment.

## 7. Knowledge check
1. Difference between automation rule and playbook?
2. Why use least privilege?
3. What does idempotency help prevent?
4. Which actions should require human approval?