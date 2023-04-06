from cryptography.fernet import Fernet
import base64, hashlib

def get_key(passcode:bytes) -> bytes:
    assert isinstance(passcode, bytes)
    hlib = hashlib.md5()
    hlib.update(passcode)
    return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

def encrypt(password, token):
    f = Fernet(get_key(password))
    return f.encrypt(bytes(token))

def decrypt(password, token):
    f = Fernet(get_key(password))
    return str(f.decrypt(bytes(token))).strip('\'b')

