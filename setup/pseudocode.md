# Pseudocode for User Registration and Verification System

## Overview
This pseudocode outlines the logic for a user registration and verification system using a MySQL database and encryption techniques.

## Pseudocode

### Classes

#### Class: User

- **Method: __init__(database_host, database_user, database_password, database_name)**
    - Connect to the database using provided credentials
    - Call `create_table()`

- **Method: create_table()**
    - Execute SQL to create `users` table if it does not exist

- **Method: register_user(username, password)**
    - Generate salt using `EncryptionUtils.generate_salt()`
    - Derive password hash using `EncryptionUtils.derive_key(password, salt)`
    - Generate symmetric key (32 bytes)
    - Encrypt the symmetric key
    - Generate HMAC value for the symmetric key
    - Insert `username`, `password_hash`, `salt`, `encrypted_symmetric_key`, `hmac` into the `users` table

- **Method: verify_user(username, password)**
    - Execute SQL to retrieve `password_hash`, `salt`, `symmetric_key_encrypted`, `hmac` for the given `username`
    - If user not found, return False
    - Derive password hash using `EncryptionUtils.derive_key(password, stored_salt)`
    - Verify the HMAC of the symmetric key
    - If derived hash matches stored hash, return True (Login successful)
    - Else, return False (Login failed)

- **Method: close_connection()**
    - Close the database connection

#### Class: EncryptionUtils

- **Method: generate_salt()**
    - Return random 16-byte salt using `os.urandom`

- **Method: derive_key(password, salt)**
    - Initialize PBKDF2HMAC with SHA-256
    - Derive a key using the password and salt
    - Return the derived key

## Flow

1. **User Registration**
    - Create instance of `User`
    - Call `register_user(username, password)`

2. **User Verification**
    - Create instance of `User`
    - Call `verify_user(username, password)`
    - If True, notify user of successful login
    - If False, notify user of failed login

3. **Closing Database Connection**
    - Call `close_connection()` when done
