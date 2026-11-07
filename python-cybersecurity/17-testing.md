# 17 — Testing, Debugging and Code Quality

Security scripts influence decisions. Test normal, invalid, empty and unusually large inputs. Incorrect parsing can miss detections or create false alarms.

## Assertions
~~~python
def is_valid_port(port):
    return isinstance(port, int) and 1 <= port <= 65535

assert is_valid_port(443)
assert not is_valid_port(70000)
~~~

## Unit tests
~~~python
import unittest

def classify_attempts(count):
    return "review" if count >= 5 else "normal"

class TestClassification(unittest.TestCase):
    def test_threshold(self):
        self.assertEqual(classify_attempts(5), "review")

    def test_below_threshold(self):
        self.assertEqual(classify_attempts(4), "normal")

if __name__ == "__main__":
    unittest.main()
~~~

The label review is intentional; a threshold is not proof of an attack.

## Debugging and logging
Read the traceback to identify the exception and line. Use logging levels DEBUG, INFO, WARNING, ERROR and CRITICAL. Never log passwords, tokens, private keys or sensitive personal data.

## Code quality
Use descriptive names, small functions, type hints where useful, docstrings, consistent formatting, tests and a README. Pin dependencies and document supported Python versions.

## Exercise
Test a port validator and log parser with valid, invalid, missing-field and malformed-line cases. Deliberately introduce a bug, observe a failing test and then fix it.
