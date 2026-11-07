# 12 — TLS and HTTPS Traffic Analysis

## 1. Why TLS?
TLS provides confidentiality and integrity for data in transit and supports server authentication through certificates. HTTPS is HTTP protected by TLS (or HTTP/3 over QUIC with TLS 1.3).

TLS does not guarantee that a website is honest, that the endpoint is clean, or that the user is safe from phishing.

## 2. What a capture may reveal
Depending on TLS version, extensions and capture point, you may observe:
- Client and server IP/port
- TLS record sizes and timing
- ClientHello and ServerHello metadata
- Negotiated TLS version and cipher suite
- Certificate information in handshakes where visible
- Alerts, resets and handshake failures

Modern TLS encrypts application data. TLS 1.3 encrypts more of the handshake than older versions. Encrypted ClientHello (ECH), where deployed, can further reduce visible hostname metadata.

## 3. Certificate validation
A client should validate the certificate chain, hostname, validity period and applicable trust/revocation policy. A certificate being present does not alone establish that the destination is safe.

## 4. Useful filters
```text
tls
tls.handshake
tls.handshake.type == 1
tls.handshake.type == 2
tls.alert_message
tcp.port == 443
quic
```

## 5. Decryption and key logs
Wireshark can decrypt some TLS sessions when the analyst has an authorized key log from an endpoint under their control and configures it correctly. This is appropriate for a personal lab or approved investigation. Never obtain or publish another person's secrets. Do not share key-log files; they can expose session content.

## 6. TLS troubleshooting
Look for certificate alerts, protocol-version mismatch, handshake retransmissions, resets and timeouts. Correlate with browser/application errors, server logs, proxy and firewall events. A failed handshake may be caused by certificate trust, clock skew, inspection devices or incompatible configuration.

## Practical lab
Visit a test HTTPS endpoint from your own VM while capturing. Apply `tls.handshake`. Identify ClientHello and ServerHello when visible, negotiated version and certificate metadata if available. Explain which information remains encrypted.

## Security analyst caution
Encrypted traffic metadata can support behavior analysis, but IP, SNI (when visible), certificate and JA3/JA4-style fingerprints are not conclusive identity or malware proof. Fingerprints can be shared by benign software and change over time.
