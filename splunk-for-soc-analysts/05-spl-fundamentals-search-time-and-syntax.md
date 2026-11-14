# 05 — SPL Fundamentals: Search, Time and Syntax

## Objectives
Learn the structure of a Search Processing Language (SPL) search.

## 1. SPL basics
SPL is Splunk's search language. The pipe symbol passes results from one command to the next.

Example:
    index=security earliest=-24h

This searches the security index over the previous 24 hours. The index must exist and contain data.

## 2. Keywords and field filters
    index=security "failed"
    index=security user="alice"
    index=security src="192.0.2.10"

These are examples. Replace index and fields with those present in your own data. The IP shown is from a documentation range.

## 3. Boolean logic
- AND: both conditions must match.
- OR: either condition may match.
- NOT: exclude a condition.
- Parentheses: group conditions.

Example:
    index=security (action=failure OR status=failed)

## 4. Time range
Use the time picker or explicit earliest/latest values. A correct search with the wrong time range may return no results. Record the selected range when documenting a query.

## 5. Search workflow
1. Select the smallest relevant index.
2. Set a bounded time range.
3. Confirm events are returned.
4. Add one filter at a time.
5. Verify field names from actual events.
6. Save query purpose, output, and limitations.

## 6. Performance
Avoid searching every index over all time without a reason. Narrow searches using index, time, host, source, and known fields.

## Practical exercises
    index=security earliest=-24h
    index=security host="LAB-WIN01"
    index=security (EventCode=4624 OR EventCode=4625)
    index=security | head 20

If no data exists, explain what each query is designed to find and practice with synthetic events.

## Common mistakes
Wrong index, wrong time range, nonexistent field, unexpected data type, or assuming zero results proves the activity never occurred.

## Knowledge check
1. What does the pipe do?
2. Why narrow the time range?
3. Keyword search versus field filter?
4. Why can a query return zero events even when a source has logs?

## References
- [SPL Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/)
- [Search Tutorial](https://docs.splunk.com/Documentation/Splunk/latest/SearchTutorial/WelcometotheSearchTutorial)
