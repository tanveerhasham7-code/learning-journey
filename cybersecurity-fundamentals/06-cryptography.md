# 06 — Cryptography Fundamentals

## Encryption
Encryption transforms plaintext into ciphertext using an algorithm and key. Decryption recovers plaintext. Encryption protects confidentiality but does not automatically prove authenticity or integrity.

- Symmetric encryption uses the same secret key for encryption and decryption. It is efficient for large data; protect and share the key securely.
- Asymmetric cryptography uses related public/private keys. It supports key establishment and digital signatures and is commonly combined with symmetric encryption.

## Hashing
A cryptographic hash creates a fixed-length digest. It is designed to be one-way and to make it difficult to find another input with the same digest. Hashing is not encryption. Uses include integrity checks and digital signatures.

For passwords, use a dedicated password-hashing scheme such as Argon2id, bcrypt, or scrypt with unique salts and suitable parameters. A fast general-purpose hash alone is unsuitable for password storage.

## Salting
A salt is a unique random value stored with a password hash. It helps prevent identical passwords from producing identical stored hashes and weakens precomputed lookup attacks. A salt is not secret.

## Digital signatures and certificates
A digital signature is created with a private key and verified with its public key. A certificate binds a public key to an identity through a certificate authority and validation process.

## TLS
TLS protects data in transit and can authenticate a server when its certificate is correctly validated. HTTPS does not prove a website is honest or safe; it protects the connection to that website.

## Key management
Generate keys securely, restrict access, rotate or revoke when needed, and protect backups. A lost key may make data unrecoverable; a leaked key can destroy confidentiality.

## Practical
Create a harmless text file and calculate SHA-256 using PowerShell Get-FileHash or Linux sha256sum. Change one character and calculate again. Observe the changed digest. Do not use sensitive files.
