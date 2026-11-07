# 11 — CSV and JSON

## CSV
Use the csv module rather than splitting on commas; quoted fields can contain commas.

~~~python
import csv

with open("data/events.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row.get("username"), row.get("event_type"))
~~~

## JSON
JSON objects map to dictionaries and arrays map to lists.

~~~python
import json
from pathlib import Path

data = json.loads(Path("data/event.json").read_text(encoding="utf-8"))
print(data.get("event_type", "unknown"))
~~~

Validate required fields and types. Handle malformed or unexpectedly large input safely.

## Security use cases
Parse SIEM exports, normalize events, compare asset snapshots, store test IOCs and produce reports. Do not export credentials, tokens, personal data or internal identifiers.

## Exercise
Create a synthetic CSV with timestamp, username, event_type and source. Count event types and export a JSON summary. Verify the output in a text editor.
