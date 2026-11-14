# 02 — Azure Fundamentals for Sentinel Analysts

## 1. Why Azure knowledge matters
Sentinel operates in Microsoft Azure. Analysts need enough Azure knowledge to understand where resources live, how access is controlled, how billing works and how data is connected.

## 2. Core terms
- **Tenant:** a dedicated Microsoft Entra ID directory instance for an organization.
- **Subscription:** billing and management boundary for Azure resources.
- **Resource group:** logical container for related Azure resources.
- **Resource:** an individual Azure service or object, such as a workspace.
- **Region:** geographic Azure deployment area.
- **Microsoft Entra ID:** identity and access management service.
- **RBAC:** role-based access control that assigns permissions at defined scopes.
- **Azure Monitor:** platform for collecting and analyzing monitoring data.
- **Azure Policy:** governance service for evaluating or enforcing resource standards.

## 3. Resource hierarchy

~~~text
Microsoft Entra tenant
       |
Azure subscription
       |
Resource group
       |
Log Analytics Workspace
       |
Microsoft Sentinel solution
~~~

A workspace and Sentinel configuration are Azure resources associated with a subscription and resource group. Exact resource relationships and supported deployment options should be checked in current documentation.

## 4. Identity and access
Use least privilege. Give analysts only the permissions required for their duties. Separate administration from investigation where possible, use multifactor authentication and review privileged role assignments.

Common role concepts include Reader, Contributor, Log Analytics Reader and Sentinel-specific roles. Names, scopes and capabilities can evolve; confirm current built-in role definitions before assigning access.

## 5. Azure portal orientation
Learn how to:
1. Select the correct tenant and subscription.
2. Locate the resource group.
3. Open the Log Analytics Workspace.
4. Open Microsoft Sentinel for the workspace.
5. Review access control (IAM), activity logs and resource health.
6. Identify the region and billing context.

## 6. Cost awareness
Sentinel-related costs may include data ingestion, retention, analytics tiers, search jobs, automation and connected services. Do not assume every trial or free allowance covers every feature. Review the official pricing page and configure budgets/alerts where available.

## 7. Practical exercise
Without creating resources, draw the tenant → subscription → resource group → workspace relationship. Identify which account and permissions would be required in an authorized training subscription. Do not share tenant IDs or subscription identifiers publicly.

## 8. Knowledge check
1. Difference between tenant and subscription?
2. What does a resource group do?
3. Why use RBAC and least privilege?
4. Why check region and pricing before deployment?