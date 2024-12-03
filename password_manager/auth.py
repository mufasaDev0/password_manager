import os 
from encryption import generate_key, encrypt_data, decrypt_data

MASTER_KEY_PATH = "data/master.key"

# Configurar senha mestre no primeiro uso
def setup_master_password(password):
    if not os.path.exists("data/"):
        os.makedirs("data/")

    key = generate_key()
    encrypted_password = encrypt_data(password, key)

    with open(MASTER_KEY_PATH, 'wb') as key_file:
        key_file.write(key)

    with open(f"{MASTER_KEY_PATH}.enc", 'wb') as password_file:
        password_file.write(encrypted_password)

# Validar senha mestre
def validate_master_password(input_password):
    if not os.path.exists(MASTER_KEY_PATH):
        return False

    with open(MASTER_KEY_PATH, 'rb') as key_file:
        key = key_file.read()

    with open(f"{MASTER_KEY_PATH}.enc", 'rb') as password_file:
        encrypted_password = password_file.read()

    decrypted_password = decrypt_data(encrypted_password, key)
    return decrypted_password == input_password
