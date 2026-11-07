"""Match supplied test indicators against a synthetic CSV event file."""
import argparse
import csv
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indicators_json", help="JSON array of test indicator strings")
    parser.add_argument("events_csv", help="CSV with timestamp and observable columns")
    args = parser.parse_args()
    indicators = json.loads(Path(args.indicators_json).read_text(encoding="utf-8"))
    if not isinstance(indicators, list) or not all(isinstance(x, str) for x in indicators):
        parser.error("Indicator file must be a JSON array of strings")
    indicator_set = {item.strip().lower() for item in indicators if item.strip()}
    matches = []
    with Path(args.events_csv).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not {"timestamp", "observable"}.issubset(reader.fieldnames):
            parser.error("Events CSV requires timestamp and observable columns")
        for row in reader:
            observable = (row.get("observable") or "").strip()
            if observable.lower() in indicator_set:
                matches.append({"timestamp": row.get("timestamp", ""), "observable": observable})
    print(json.dumps({
        "matches": matches,
        "match_count": len(matches),
        "interpretation": "Matches are investigation leads, not proof of compromise."
    }, indent=2))


if __name__ == "__main__":
    main()
