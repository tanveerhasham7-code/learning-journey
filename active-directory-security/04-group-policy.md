# Group Policy


### 4.1 What is Group Policy?

Group Policy is a Windows feature used to centrally configure user and computer settings in an AD domain. A Group Policy Object (GPO) contains policy settings and can be linked to a site, domain or OU.

Examples of security settings managed through policy:

- Password and account-lockout policy.
- Windows Defender Firewall configuration.
- Audit policy.
- Windows security options.
- Script and software deployment settings.
- Restrictions on removable storage or other device behavior.

### 4.2 Policy processing

A simplified processing order is commonly described as **Local, Site, Domain, OU** (LSDOU). Policies can be affected by inheritance, enforcement, filtering and other configuration. The effective policy should be checked on the endpoint rather than assumed from a GPO's name.

### 4.3 SOC monitoring

A suspicious policy change can weaken security across many machines. Monitor for:

- Changes to GPOs or their links.
- Unexpected modifications to scripts stored in SYSVOL.
- Changes to audit, firewall or Defender settings.
- New startup or logon scripts.
- Changes performed by an account that does not normally administer policy.

Correlate the directory-change event with the administrator's logon, endpoint activity, change ticket and the actual policy version.

---
