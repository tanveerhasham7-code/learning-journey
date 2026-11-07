# 04 — Conditions and Loops

## Conditions
~~~python
failed_attempts = 6
if failed_attempts >= 5:
    print("Review this activity")
elif failed_attempts > 0:
    print("Some failures recorded")
else:
    print("No failures in this sample")
~~~

A threshold is an investigation lead, not proof of an attack. Consider time window, account, source and surrounding events.

## For loops
~~~python
ports = [22, 53, 80, 443]
for port in ports:
    print(f"Observed port: {port}")
~~~

A for loop processes each item in a sequence. range(5) produces 0 through 4.

## While loops
~~~python
count = 0
while count < 3:
    print(count)
    count += 1
~~~

Ensure the condition eventually changes or a while loop may never stop. break exits; continue skips to the next iteration.

## Defensive use cases
Count events in a sample log, validate CSV rows, compare approved hashes or summarize lab assets.

## Exercise
Create a list of synthetic event dictionaries. Count records whose event_type is login_failed. Explain why the count alone cannot confirm malicious activity.
