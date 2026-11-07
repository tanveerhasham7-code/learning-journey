# Supporting Scripts

These small scripts are optional helpers for organizing your own lab notes. They are not scanners and do not contact external systems.

## Requirements
- Python 3.9+
- Standard library only

## Scripts
- `validate_ipv4_plan.py`: validate IPv4 addresses and CIDR networks in a small CSV plan.
- `summarize_nmap_xml.py`: summarize an Nmap XML file created from an explicitly authorized lab scan.

## Safe use
Use synthetic or sanitized lab data. Nmap XML may disclose internal hostnames, addresses and service details; do not publish it without review. These scripts do not prove that a network is secure.
