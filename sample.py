import base64
import hashlib
from cryptography.fernet import Fernet

SECRET_TEXT = ""

def get_cipher():
    key = hashlib.sha256(SECRET_TEXT.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key)
    return Fernet(fernet_key)

def encrypt(text):
    return get_cipher().encrypt(text.encode()).decode()

def decrypt(token):
    return get_cipher().decrypt(token.encode()).decode()


if __name__ == "__main__":
    enc = encrypt("")
    print("Encrypted:", enc)
    print("Decrypted:", decrypt(enc))
