from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import hashlib
import hmac
import os

class EncryptionUtils:
    @staticmethod
    def generate_salt():
        return os.urandom(16)

    @staticmethod
    def derive_key(password, salt):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return kdf.derive(password.encode())

    @staticmethod
    def encrypt_symmetric_key(symmetric_key):
        # Generate a secret key for Fernet encryption
        secret_key = Fernet.generate_key()
        cipher_suite = Fernet(secret_key)
        encrypted_key = cipher_suite.encrypt(symmetric_key)
        return secret_key + b'|' + encrypted_key  # Store secret key along with encrypted key

    @staticmethod
    def create_hmac(data, salt):
        secret = os.urandom(32)  # Replace with your actual secret key
        return hmac.new(secret, data + salt, hashlib.sha256).digest()

    @staticmethod
    def verify_hmac(password_hash, salt, hmac_value):
        # Replace 'your_secret' with your actual secret key
        secret = os.urandom(32)
        computed_hmac = hmac.new(secret, password_hash + salt, hashlib.sha256).digest()
        return hmac.compare_digest(computed_hmac, hmac_value)
