import unittest

from url_analyzer import analyze_url, format_result


class AnalyzeUrlTests(unittest.TestCase):
    def test_https_example_has_no_risk_indicators(self):
        result = analyze_url("https://example.com")
        self.assertEqual(result.hostname, "example.com")
        self.assertEqual(result.score, 0)
        self.assertEqual(result.level, "LOW")

    def test_http_adds_indicator(self):
        result = analyze_url("http://example.com")
        self.assertGreaterEqual(result.score, 15)
        self.assertTrue(any("HTTP" in finding.message for finding in result.findings))

    def test_ip_hostname_is_flagged(self):
        result = analyze_url("http://192.0.2.10/path")
        self.assertTrue(any("IP address" in finding.message for finding in result.findings))

    def test_at_sign_in_authority_is_flagged(self):
        result = analyze_url("https://trusted.example@other.example/path")
        self.assertTrue(any("'@'" in finding.message for finding in result.findings))
        self.assertEqual(result.hostname, "other.example")

    def test_shortener_is_flagged(self):
        result = analyze_url("https://bit.ly/something")
        self.assertTrue(any("shortening service" in finding.message for finding in result.findings))

    def test_missing_scheme_is_flagged(self):
        result = analyze_url("example.com/account")
        self.assertTrue(any("no explicit scheme" in finding.message for finding in result.findings))

    def test_empty_input_is_invalid(self):
        result = analyze_url("   ")
        self.assertEqual(result.level, "INVALID")

    def test_bad_port_is_invalid(self):
        result = analyze_url("https://example.com:bad")
        self.assertEqual(result.level, "INVALID")

    def test_output_explains_it_does_not_visit_urls(self):
        result = analyze_url("https://example.com")
        self.assertIn("does not visit the URL", format_result(result))


if __name__ == "__main__":
    unittest.main()
