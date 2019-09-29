# Security

## Encryption

### SSL

SSL functionality is provided by the web server.

### Data Encryption

AES 256 is used with a secret key set by the application administrator to encrypt Slack access tokens and display names. Avatar image links are retrieved each time they are needed and thus not stored. Stored session cookies are also encrypted to prevent session hijacking in the event of a breach.

Encryption and decryption is done by the application server.

---

## Cookies

Session cookies are marked HttpOnly and Secure to ensure they cannot be modified for XSS attacks or intercepted.