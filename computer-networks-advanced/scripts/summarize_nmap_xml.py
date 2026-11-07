#!/usr/bin/env python3
"""Summarize an Nmap XML report from an authorized lab scan; no network activity."""
import argparse
import xml.etree.ElementTree as ET


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml_file", help="Nmap XML file from your authorized lab")
    args = parser.parse_args()
    try:
        root = ET.parse(args.xml_file).getroot()
    except (OSError, ET.ParseError) as exc:
        parser.error(f"cannot read XML: {exc}")

    for host in root.findall("host"):
        status = host.find("status")
        state = status.get("state", "unknown") if status is not None else "unknown"
        addresses = [item.get("addr", "") for item in host.findall("address")]
        names = [item.get("name", "") for item in host.findall("./hostnames/hostname")]
        print(f"Host: {', '.join(addresses) or 'address unknown'} | state={state}")
        if names:
            print(f"  Names: {', '.join(names)}")
        for port in host.findall("./ports/port"):
            state_node = port.find("state")
            service = port.find("service")
            port_state = state_node.get("state", "unknown") if state_node is not None else "unknown"
            service_name = service.get("name", "unknown") if service is not None else "unknown"
            product = service.get("product", "") if service is not None else ""
            version = service.get("version", "") if service is not None else ""
            print(f"  {port.get('protocol')}/{port.get('portid')}: {port_state} — {service_name} {product} {version}".rstrip())
    print("\nReminder: discovered services require validation; an open port is not proof of vulnerability.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
