from cryptography.fernet import Fernet

# Gerar uma nova chave de criptografia
def generate_key():
    return Fernet.generate_key()

# Criptografar dados com uma chave
def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

# Descriptografar dados com uma chave
def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()
