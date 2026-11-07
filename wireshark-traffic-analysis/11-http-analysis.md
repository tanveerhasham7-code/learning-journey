# 11 — HTTP and Web Traffic Analysis

## 1. HTTP overview
HTTP is an application protocol used for web communication. A request commonly includes a method, path, headers and optional body. A response includes status code, headers and optional body.

Common methods: GET, POST, PUT, PATCH, DELETE, HEAD and OPTIONS. Common status groups: 2xx success, 3xx redirection, 4xx client-side error and 5xx server-side error.

## 2. HTTP fields
In a permitted plaintext test capture, inspect:
- Request method and URI
- Host header
- User-Agent
- Status code
- Content-Type and Content-Length
- Redirects and timing
- Request/response body, if present

Do not capture real credentials or private user sessions. Plain HTTP may expose sensitive content.

## 3. Filters
```text
http
http.request
http.response
http.request.method == "GET"
http.response.code >= 400
http.host
http.request.uri
```
Field names and protocol decoding can depend on Wireshark version and traffic.

## 4. Follow HTTP stream
Use Follow → TCP Stream to see the conversation where the payload is visible. This is useful for understanding request/response order, but it may expose passwords, tokens, cookies or personal data. Use only synthetic lab requests.

## 5. HTTPS and limitations
Most modern websites use HTTPS. A capture typically reveals IPs, ports, timing, packet sizes and some handshake metadata, but not the encrypted HTTP path or body. Do not assume absence of readable HTTP means no web activity.

## 6. Security investigation clues
Potentially relevant observations include unexpected HTTP to a sensitive host, unusual methods, repeated errors, suspicious redirects, unusual upload volume and cleartext authentication. These are leads, not proof. Validate with proxy, server and endpoint logs.

## Practical lab
Start a local HTTP server in a lab VM and request a harmless test page from another VM. Capture the request and response. Identify method, path, host and status. Do not use real passwords or session tokens.
