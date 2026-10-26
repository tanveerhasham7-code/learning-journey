# PhishGuard — Phishing URL Analyzer 🔐

A beginner-friendly Python cybersecurity project that analyzes URLs for suspicious patterns. It is designed for learning URL structure, basic threat indicators, Python functions, command-line tools, and unit testing.

> **Important:** PhishGuard is an educational heuristic tool. It does not prove that a URL is safe or malicious. It does not visit URLs, make network requests, or submit URLs to third-party services.

## Features

- Checks URL format and hostname structure
- Flags plain HTTP URLs
- Detects IP addresses used as hostnames
- Flags user-info syntax (such as `trusted.example@other.example`)
- Looks for suspicious words in the URL
- Flags URL shortener domains
- Checks for unusually long URLs and excessive subdomains
- Produces a risk score and explains each finding
- Supports a single URL or a text file of URLs
- Includes unit tests using Python's built-in `unittest`

## Requirements

- Python 3.9 or newer
- No third-party packages required

## Run it

From this directory, analyze one URL:

```bash
python url_analyzer.py "http://example.com/login"
```

Analyze the included examples:

```bash
python url_analyzer.py --file sample_urls.txt
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## Example output

Exact scores depend on the indicators detected.

```text
URL: http://192.0.2.10/secure-login
Risk level: HIGH
Risk score: 65/100
Findings:
  - URL uses HTTP instead of HTTPS.
  - Hostname is an IP address rather than a typical domain name.
  - URL contains a potentially suspicious keyword: login.
```

The IP address above is from a documentation range and is used only as an example.

## What the score means

- **LOW (0–24):** Few indicators were found.
- **MEDIUM (25–49):** Review the URL carefully.
- **HIGH (50–100):** Multiple or higher-weight indicators were found.

The score is a simple teaching aid, not a statistically validated probability. A low score does not mean a URL is trustworthy, and legitimate websites can trigger warnings.

## How it works

1. Parse the URL using Python's `urllib.parse`.
2. Normalize the hostname for analysis.
3. Check for a set of suspicious patterns.
4. Add weighted points for each finding, capped at 100.
5. Print the score and human-readable explanations.

## Project structure

```text
phishguard-url-analyzer/
├── README.md
├── url_analyzer.py
├── sample_urls.txt
└── tests/
    └── test_url_analyzer.py
```

## Safe-use guidelines

- Test with sample URLs or URLs you are authorized to analyze.
- Do not open suspicious links just to check them.
- This program does not fetch website content, verify certificates, or query reputation services.
- Never enter passwords or other private information into suspicious sites.
- For real incidents, follow your organization's security procedures.

## Skills practiced

Python • URL parsing • Security indicators • Command-line interfaces • Unit testing • Defensive security

## Future improvements

- Add a configurable rules file
- Export results to JSON or CSV
- Add more tests for internationalized domain names
- Integrate a reputable URL reputation API only with explicit configuration and privacy review

---

Created as a hands-on learning project by **Tanveer Hassham**, cybersecurity student.
