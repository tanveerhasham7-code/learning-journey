"""Summarize a synthetic CSV with timestamp, username and event_type columns."""
import argparse
import csv
from collections import Counter
from pathlib import Path

REQUIRED = {"timestamp", "username", "event_type"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", help="Synthetic or authorized CSV events")
    args = parser.parse_args()
    try:
        with Path(args.csv_file).open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or not REQUIRED.issubset(set(reader.fieldnames)):
                parser.error("CSV requires timestamp, username and event_type columns")
            counts = Counter()
            failed_by_user = Counter()
            total = 0
            for row in reader:
                total += 1
                event_type = (row.get("event_type") or "").strip().lower()
                username = (row.get("username") or "").strip()
                counts[event_type or "missing"] += 1
                if event_type == "login_failed":
                    failed_by_user[username or "unknown"] += 1
    except FileNotFoundError:
        parser.error("Input file not found")
    print(f"Records processed: {total}")
    print("Event counts:")
    for name, count in counts.most_common():
        print(f"  {name}: {count}")
    print("Failed-login review candidates (not proof of attack):")
    for username, count in failed_by_user.most_common():
        print(f"  {username}: {count}")


if __name__ == "__main__":
    main()
