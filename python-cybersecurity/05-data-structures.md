# 05 — Strings and Data Structures

## Strings
Useful methods include strip, lower, split, replace and startswith.

~~~python
line = "  AUTH_FAILURE,alice,lab-pc  "
parts = line.strip().split(",")
print(parts[0].lower())
~~~

Preserve original evidence and normalize a copy for analysis.

## Lists, tuples and sets
Lists are ordered and changeable. Tuples are ordered and immutable. Sets store unique values and support fast membership checks.

~~~python
ports = [22, 53, 80]
fixed_record = ("event-1", "2026-01-01T10:00:00Z")
known_hashes = {"placeholder-a", "placeholder-b"}
print("placeholder-a" in known_hashes)
~~~

The example hash strings are placeholders, not real SHA-256 values.

## Dictionaries
Dictionaries map keys to values and suit structured security events.

~~~python
event = {
    "timestamp": "2026-01-01T10:30:00Z",
    "username": "lab_user",
    "event_type": "login_failed",
    "source": "lab-workstation"
}
print(event.get("event_type", "unknown"))
~~~

Use get when fields may be missing. Do not assume every log record has every key.

## Exercise
Create five synthetic events. Use a set to find unique usernames and a dictionary to count event types. Do not use real account logs.
