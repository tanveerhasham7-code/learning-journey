# 14 — HTTP, APIs and Web Security Basics

HTTP is an application-layer protocol used by web clients and servers. Learn methods such as GET, POST, PUT, PATCH and DELETE; status codes; headers; cookies; request bodies and HTTPS.

## requests example
Install requests in your virtual environment from its trusted project source.

~~~python
import requests

response = requests.get("https://example.com", timeout=10)
print(response.status_code)
print(response.headers.get("content-type"))
~~~

Use only services you are allowed to access. Set timeouts, handle exceptions and respect terms and rate limits.

## APIs and secrets
APIs let systems exchange data, often as JSON. Read provider documentation. Never hardcode API keys in source code or commit .env files. Use a secure secret manager or protected local configuration; rotate keys accidentally exposed.

## TLS
Do not disable certificate verification to fix errors. Investigate system time, hostname, certificate chain and trusted CA configuration.

## Web security concepts
Study input validation, output encoding, authentication, authorization, session management, CSRF, SQL injection, SSRF and secure headers defensively. Use intentionally vulnerable local training applications only within their prescribed lab.

## Exercise
Send one GET request to example.com with a timeout. Record status and content type, handle network exceptions and do not scrape aggressively.
