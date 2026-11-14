# 06 — SPL Commands: stats, table, dedup and sort

## Objectives
Summarize events and display useful investigation fields.

## 1. stats
Calculates aggregates.
    index=security EventCode=4625
    | stats count by user

This counts matching events grouped by user, if the field exists.

## 2. table
Selects fields for display.
    index=security
    | table _time host user EventCode

Use it to create a focused view, but do not discard fields needed for later pivots.

## 3. sort
Orders results.
    index=security
    | sort - _time

The minus sign requests descending order.

## 4. dedup
Removes duplicate values for selected fields according to the command behavior and result order. It can help create unique lists, but may hide repeated behavior. Do not use it early when event frequency matters.

## 5. Other commands
- fields: include or exclude fields.
- head: show an initial subset.
- top / rare: common or uncommon values.
- rename: rename a result field.
- eval: calculate a field.
- where: filter using an expression.

## Practical exercises
    index=security EventCode=4625
    | stats count by user
    | sort - count

    index=security
    | stats count by host sourcetype
    | sort - count

    index=security
    | table _time host user src action
    | sort - _time
    | head 25

Adapt field names to your data. Plausible syntax is not the same as a tested query.

## Analyst interpretation
A high count may be normal for a busy service or shared system. Compare with baseline, asset role, user behavior, and related events.

## Knowledge check
1. What does stats count by user produce?
2. Why can dedup hide brute-force evidence?
3. When is table useful?
4. How would you find the most common source IPs?

## References
- [SPL command reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/)
