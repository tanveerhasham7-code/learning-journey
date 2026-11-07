#!/usr/bin/env python3
"""Validate a simple CSV IPv4 plan; performs no network activity.

CSV columns: name,network,gateway
Example:
name,network,gateway
Staff,192.168.10.0/24,192.168.10.1
"""
import argparse
import csv
import ipaddress
import sys


def validate(path: str) -> int:
    errors = 0
    with open(path, newline="", encoding="utf-8") as handle:
        for line, row in enumerate(csv.DictReader(handle), start=2):
            name = (row.get("name") or "").strip() or f"line {line}"
            try:
                network = ipaddress.ip_network((row.get("network") or "").strip(), strict=True)
                gateway_text = (row.get("gateway") or "").strip()
                gateway = ipaddress.ip_address(gateway_text)
                if not isinstance(network, ipaddress.IPv4Network):
                    raise ValueError("network must be IPv4")
                if not isinstance(gateway, ipaddress.IPv4Address):
                    raise ValueError("gateway must be IPv4")
                if gateway not in network:
                    raise ValueError(f"gateway {gateway} is outside {network}")
                if gateway in (network.network_address, network.broadcast_address):
                    raise ValueError("gateway cannot be network or broadcast address")
                print(f"OK   {name}: {network}, gateway {gateway}")
            except ValueError as exc:
                errors += 1
                print(f"ERROR {name}: {exc}")
    print(f"\nValidation finished: {errors} error(s)")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="CSV containing name,network,gateway")
    args = parser.parse_args()
    try:
        return validate(args.csv_file)
    except (OSError, csv.Error) as exc:
        print(f"Could not read input: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
