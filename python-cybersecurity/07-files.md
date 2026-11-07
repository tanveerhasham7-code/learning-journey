# 07 — Files, Paths and Exceptions

## Read files safely
Use with so files close automatically.

~~~python
from pathlib import Path

sample = Path("data/sample.txt")
text = sample.read_text(encoding="utf-8")
print(text)
~~~

For large logs, process line by line:

~~~python
with open("data/sample.txt", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
~~~

## Paths and evidence
Use pathlib rather than manually joining path strings. Validate user-supplied paths and restrict processing to an intended base directory. Work on copies of evidence, preserve originals and write reports to a separate output folder.

## Exceptions
Common errors include FileNotFoundError, PermissionError, UnicodeDecodeError and ValueError.

~~~python
from pathlib import Path

try:
    content = Path("data/sample.txt").read_text(encoding="utf-8")
except FileNotFoundError:
    print("Sample file not found")
except PermissionError:
    print("Permission denied")
~~~

Do not use a bare except to hide errors. Report useful diagnostics without leaking secrets.

## Exercise
Create a sample file, read it line by line, handle a missing-file error and write a summary to output/summary.txt. Confirm the original is unchanged.
