import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Function to derive an encryption key from the master password and salt
def derive_key(master_password: str, salt: bytes):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200000,
    )

    key = kdf.derive(master_password.encode())
    fernet_key = base64.urlsafe_b64encode(key)

    return fernet_key

# Encryption using Fernet
def encrypt_text(plain_text: str, fernet: Fernet):
    return fernet.encrypt(plain_text.encode())

# Decryption using Fernet
def decrypt_text(cipher_text: bytes, fernet: Fernet):
    return fernet.decrypt(cipher_text.decode())

