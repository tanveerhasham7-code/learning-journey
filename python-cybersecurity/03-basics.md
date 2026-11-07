# 03 — Syntax, Variables and Data Types

Python uses indentation to define blocks. Use four spaces consistently. A colon starts blocks after if, for, while, def and class.

~~~python
if True:
    print("Indented block")
~~~

## Variables and types
~~~python
analyst = "student"       # str
attempts = 3              # int
risk_score = 7.5          # float
authorized = True         # bool
missing_value = None      # NoneType
raw_bytes = b"ABC"         # bytes
~~~

Strings store text, integers whole numbers, floats decimals, booleans true/false values and bytes raw byte data.

## Conversion and validation
~~~python
port_text = "443"
port = int(port_text)
print(port + 1)
~~~

Invalid conversions can raise ValueError. Validate untrusted input before using it in paths, shell commands, SQL or network requests.

## Operators
Arithmetic: + - * / // % **
Comparison: == != < > <= >=
Logical: and, or, not
Membership: in, not in

Do not confuse assignment = with equality ==.

## Input and output
~~~python
hostname = input("Lab hostname: ").strip()
print(f"Selected lab host: {hostname}")
~~~

Input is untrusted. Validate format and permitted range before acting on it.

## Exercise
Ask for a port, convert it safely and reject values outside 1–65535. Test letters, negative values, zero and 65536. Do not connect to the host.
