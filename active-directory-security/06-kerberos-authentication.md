# Kerberos authentication


### 6.1 What is Kerberos?

Kerberos is a network authentication protocol commonly used by AD domains. It uses tickets and a trusted Key Distribution Center (KDC), usually hosted by a domain controller, so users can authenticate to services without sending their password to every service.

### 6.2 Simplified flow

1. A user signs in and requests authentication from the KDC.
2. The Authentication Service (AS) issues a Ticket-Granting Ticket (TGT) after successful authentication.
3. The client presents the TGT to request a service ticket from the Ticket-Granting Service (TGS).
4. The client presents the service ticket to the target service.
5. The service validates the ticket and grants access according to its own authorization rules.

A ticket proves an authentication step; it does not automatically grant permission to every resource.

### 6.3 Important terms

- **KDC:** Key Distribution Center.
- **TGT:** Ticket-Granting Ticket.
- **TGS:** Ticket-Granting Service.
- **SPN:** Service Principal Name, which identifies a service instance for Kerberos.
- **Clock synchronization:** Kerberos is sensitive to time differences. Domain time configuration is therefore important.

### 6.4 SOC-relevant patterns

- Unusual volume of service-ticket requests.
- Service tickets requested for unexpected accounts or services.
- Kerberos pre-authentication failures.
- Unusual encryption-type usage compared with the organization's baseline.
- Authentication activity from unexpected hosts or at unusual times.

These patterns are investigation leads, not proof of compromise. Service accounts, legacy systems and legitimate administrative tools can produce unusual-looking activity.

---
