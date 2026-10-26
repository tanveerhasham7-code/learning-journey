#!/usr/bin/env python3
"""PhishGuard: a local, educational phishing-URL heuristic analyzer.

This program never opens URLs or makes network requests.
It reports indicators, not a definitive verdict.
"""

from __future__ import annotations

import argparse
import ipaddress
import sys
from dataclasses import dataclass
from urllib.parse import urlsplit


SUSPICIOUS_KEYWORDS = (
    "login",
    "verify",
    "verification",
    "password",
    "account",
    "signin",
    "secure",
    "update",
    "wallet",
    "billing",
    "recover",
)

COMMON_SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly",
    "ow.ly",
    "shorturl.at",
}

@dataclass(frozen=True)
class Finding:
    """One security indicator and its contribution to the heuristic score."""

    message: str
    points: int


@dataclass(frozen=True)
class AnalysisResult:
    """Analysis summary for a URL."""

    url: str
    hostname: str
    score: int
    level: str
    findings: tuple[Finding, ...]


def _hostname_is_ip(hostname: str) -> bool:
    """Return True if hostname is an IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(hostname)
        return True
    except ValueError:
        return False


def analyze_url(url: str) -> AnalysisResult:
    """Analyze a URL string without contacting the destination."""
    candidate = url.strip()
    findings: list[Finding] = []

    if not candidate:
        return AnalysisResult(candidate, "", 0, "INVALID", (
            Finding("URL is empty.", 0),
        ))

    # Accept a URL pasted without a scheme for convenience, but flag it.
    parse_target = candidate if "://" in candidate else f"//{candidate}"
    try:
        parts = urlsplit(parse_target)
        hostname = (parts.hostname or "").rstrip(".").lower()
        scheme = parts.scheme.lower()
        # Accessing .port can raise ValueError for malformed ports.
        _ = parts.port
    except ValueError:
        return AnalysisResult(candidate, "", 0, "INVALID", (
            Finding("URL could not be parsed (check its hostname or port).", 0),
        ))

    if not hostname:
        return AnalysisResult(candidate, "", 0, "INVALID", (
            Finding("No hostname was found. Include a valid domain or IP address.", 0),
        ))

    score = 0

    def add(message: str, points: int) -> None:
        nonlocal score
        findings.append(Finding(message, points))
        score += points

    if not scheme:
        add("URL has no explicit scheme (http:// or https://).", 5)
    elif scheme not in {"http", "https"}:
        add(f"URL uses an uncommon scheme: {scheme}.", 20)

    if scheme == "http":
        add("URL uses HTTP instead of encrypted HTTPS.", 15)

    if "@" in parts.netloc:
        add("URL contains '@' in its authority section; this can obscure the real hostname.", 25)

    if _hostname_is_ip(hostname):
        add("Hostname is an IP address instead of a typical registered domain.", 25)

    # IDNs may be legitimate, but homograph-style domains deserve careful review.
    if hostname.startswith("xn--") or ".xn--" in hostname:
        add("Hostname contains an internationalized (punycode) label; inspect it carefully.", 15)

    labels = [label for label in hostname.split(".") if label]
    if len(labels) >= 5:
        add("Hostname has many subdomain labels.", 10)

    if hostname in COMMON_SHORTENERS:
        add("Hostname belongs to a URL-shortening service; the final destination is hidden.", 15)

    lower_url = candidate.lower()
    matched_keywords = [word for word in SUSPICIOUS_KEYWORDS if word in lower_url]
    if matched_keywords:
        shown = ", ".join(matched_keywords[:4])
        add(f"URL contains potentially sensitive keywords: {shown}.", 10)

    if len(candidate) > 120:
        add("URL is unusually long.", 10)

    if candidate.count("-") >= 4:
        add("URL contains many hyphens, which can be used in deceptive addresses.", 5)

    if parts.port is not None and parts.port not in {80, 443}:
        add(f"URL specifies a non-standard web port ({parts.port}).", 10)

    score = min(score, 100)
    if score >= 50:
        level = "HIGH"
    elif score >= 25:
        level = "MEDIUM"
    else:
        level = "LOW"

    if not findings:
        findings.append(Finding("No configured indicators were detected; this does not establish trustworthiness.", 0))
    elif score < 25:
        findings.append(Finding("Only a small number of configured indicators were found; still verify the destination.", 0))

    return AnalysisResult(candidate, hostname, score, level, tuple(findings))


def format_result(result: AnalysisResult) -> str:
    """Format an analysis result for terminal output."""
    lines = [
        f"URL: {result.url}",
        f"Hostname: {result.hostname or '(not available)'}",
        f"Risk level: {result.level}",
        f"Risk score: {result.score}/100",
        "Findings:",
    ]
    lines.extend(f"  - {finding.message}" for finding in result.findings)
    lines.append("Note: heuristic result only; PhishGuard does not visit the URL.")
    return "\n".join(lines)


def read_urls(path: str) -> list[str]:
    """Read non-empty, non-comment lines from a UTF-8 text file."""
    with open(path, "r", encoding="utf-8") as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.lstrip().startswith("#")
        ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Analyze URL patterns locally for educational phishing indicators."
    )
    parser.add_argument("url", nargs="?", help="URL to analyze (quote it if it contains shell-special characters)")
    parser.add_argument("--file", dest="file_path", help="Read URLs from a UTF-8 text file, one URL per line")
    args = parser.parse_args(argv)

    if bool(args.url) == bool(args.file_path):
        parser.error("provide exactly one URL or use --file PATH")

    try:
        urls = read_urls(args.file_path) if args.file_path else [args.url]
    except OSError as exc:
        print(f"Could not read input file: {exc}", file=sys.stderr)
        return 2

    for index, url in enumerate(urls):
        if index:
            print("\n" + "-" * 60)
        print(format_result(analyze_url(url)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
