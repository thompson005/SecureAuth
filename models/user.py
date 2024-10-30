import mysql.connector
from utils.encryption import EncryptionUtils
import os

class User:
    def __init__(self, database_host, database_user, database_password, database_name):
        self.connection = mysql.connector.connect(
            host=database_host,
            user=database_user,
            password=database_password,
            database=database_name,
        )
        self.create_table()

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE NOT NULL,
                    password_hash BLOB NOT NULL,
                    salt BLOB NOT NULL,
                    symmetric_key_encrypted BLOB NOT NULL,
                    hmac BLOB NOT NULL
                )
                """
            )
        self.connection.commit()

    def register_user(self, username, password):
        salt = EncryptionUtils.generate_salt()
        password_hash = EncryptionUtils.derive_key(password, salt)

        # Generate a symmetric key and encrypt it
        symmetric_key = os.urandom(32)  # Generating a random symmetric key
        encrypted_symmetric_key = EncryptionUtils.encrypt_symmetric_key(symmetric_key)  # Encrypt the symmetric key

        # Create an HMAC value based on the stored password hash and salt
        hmac_value = EncryptionUtils.create_hmac(password_hash, salt)

        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password_hash, salt, symmetric_key_encrypted, hmac) VALUES (%s, %s, %s, %s, %s)",
                (username, password_hash, salt, encrypted_symmetric_key, hmac_value),
            )
        self.connection.commit()

    def verify_user(self, username, password):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT password_hash, salt, symmetric_key_encrypted, hmac FROM users WHERE username = %s", (username,)
            )
            row = cursor.fetchone()
            if row is None:
                return False  # User not found
            stored_password_hash, stored_salt, stored_encrypted_symmetric_key, stored_hmac = row

            # Verify the password
            derived_password_hash = EncryptionUtils.derive_key(password, stored_salt)

            # Verify the HMAC (this should match your implementation of create_hmac)
            if not EncryptionUtils.verify_hmac(stored_password_hash, stored_salt, stored_hmac):
                return False

            return derived_password_hash == stored_password_hash  # Simple check for demonstration

    def close_connection(self):
        self.connection.close()
