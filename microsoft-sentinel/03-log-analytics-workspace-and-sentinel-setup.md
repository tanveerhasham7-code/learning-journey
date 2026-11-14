# 03 — Log Analytics Workspace and Sentinel Setup

## 1. Workspace purpose
A Log Analytics Workspace is the Azure Monitor Logs environment where supported telemetry is stored and queried. Microsoft Sentinel is enabled for a supported workspace. The workspace region, access model, retention and data volume affect design and cost.

## 2. Planning checklist
Before deployment, confirm:
- You have authorization to use the Azure tenant and subscription.
- Current trial/free eligibility and regional availability.
- Expected data sources and daily ingestion volume.
- Required retention and data residency needs.
- Resource group, region and naming standards.
- RBAC roles and analyst/admin separation.
- Budget, alerts and cleanup plan.

Never create resources in an employer tenant without explicit approval.

## 3. High-level setup workflow
1. Sign in to the Azure portal using an authorized account.
2. Select the intended tenant and subscription.
3. Create or select an appropriate resource group.
4. Create a Log Analytics Workspace in a supported region.
5. Review pricing, commitment tiers and retention options.
6. Open Microsoft Sentinel and add it to the workspace.
7. Assign least-privilege roles.
8. Record configuration details without exposing identifiers.
9. Confirm workspace health and that Logs can be opened.

Portal labels and setup flows can change; follow current Microsoft Learn instructions.

## 4. Validation
A workspace existing does not mean it receives security data. Confirm the workspace is selected in Logs, tables are present after ingestion, timestamps and schemas are sensible, and users have the expected access.

## 5. Common setup problems
- Wrong tenant or subscription selected.
- Unsupported region or resource configuration.
- Insufficient permissions.
- Sentinel not enabled for the intended workspace.
- Wrong workspace selected in Logs.
- Costs or retention misunderstood.
- No data connector configured yet.

## 6. Practical exercise
Create a deployment plan first. If you have an authorized eligible subscription, deploy only after checking pricing. Capture sanitized evidence of resource group, workspace region, Sentinel enablement and access model. Redact subscription and tenant identifiers.

## 7. Knowledge check
1. Is Sentinel a replacement for the workspace?
2. What must be checked before deployment?
3. Why is workspace existence not proof of ingestion?
4. Which identifiers should be redacted in public evidence?