from cryptography.fernet import Fernet


def generateKey():
    key = Fernet.generate_key()
    return key


def encrypt_text(plain_text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(bytes(plain_text, "UTF-8"))
    return encrypted_text.decode()


def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    return f.decrypt(bytes(encrypted_text, "UTF-8")).decode()

if __name__ == "__main__":
    print(generateKey())