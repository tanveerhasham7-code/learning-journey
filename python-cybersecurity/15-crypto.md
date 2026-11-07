# 15 — Hashing, HMAC and Cryptography

## Hashing
A cryptographic hash maps data to a fixed-length digest. SHA-256 is commonly used to compare file integrity. Hashing is not encryption and is not designed to be reversed.

~~~python
import hashlib
from pathlib import Path

def sha256_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

print(sha256_file("data/sample.txt"))
~~~

A matching digest indicates matching bytes relative to a trusted reference. It does not prove origin or safety.

## HMAC
HMAC combines a hash function with a secret key to authenticate a message.

~~~python
import hashlib
import hmac

key = b"lab-only-demo-key"
message = b"sample event"
tag = hmac.new(key, message, hashlib.sha256).hexdigest()
print(tag)
~~~

The key is demonstration-only. Real applications must protect keys and use hmac.compare_digest when verifying tags.

## Password storage
Do not store passwords using plain SHA-256 or reversible encryption. Use a dedicated password-hashing scheme such as Argon2id, scrypt or PBKDF2 with unique salts and suitable parameters, through a vetted library and current guidance.

## Encryption
Symmetric encryption uses one shared key. Asymmetric cryptography uses a public/private key pair. TLS combines cryptographic techniques to protect network sessions. Do not invent your own cryptography.

## Exercise
Hash a test file, change one byte in a copy and compare digests. Explain why the digest changes and why a hash alone does not prove safety.
