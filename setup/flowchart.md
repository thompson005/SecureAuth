# User Registration and Verification System

## Overview
This system allows users to register with a username and password and verifies their credentials upon login. The implementation uses a MySQL database for storage, encryption techniques for securing sensitive data, and HMAC for ensuring data integrity.

## Flowchart

```plaintext
+--------------------+
| Start              |
+--------------------+
          |
          v
+--------------------+
| User registers     |
| (register_user)    |
+--------------------+
          |
          v
+--------------------+
| Generate salt      |
+--------------------+
          |
          v
+--------------------+
| Derive password    |
| hash using PBKDF2  |
+--------------------+
          |
          v
+--------------------+
| Generate symmetric  |
| key (32 bytes)     |
+--------------------+
          |
          v
+--------------------+
| Encrypt symmetric   |
| key                |
+--------------------+
          |
          v
+--------------------+
| Generate HMAC      |
+--------------------+
          |
          v
+--------------------+
| Store user details |
| in the database    |
+--------------------+
          |
          v
+--------------------+
| User logs in       |
| (verify_user)      |
+--------------------+
          |
          v
+--------------------+
| Retrieve stored    |
| user data from     |
| database           |
+--------------------+
          |
          v
+--------------------+
| Derive password    |
| hash using PBKDF2  |
+--------------------+
          |
          v
+--------------------+
| Verify HMAC        |
+--------------------+
          |
          v
+--------------------+
| Compare derived     |
| hash with stored    |
| hash               |
+--------------------+
          |
          v
+--------------------+
| Login successful    |
| (or fail)          |
+--------------------+
          |
          v
+--------------------+
| End                |
+--------------------+
