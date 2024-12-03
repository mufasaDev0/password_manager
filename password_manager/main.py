from auth import setup_master_password
from gui import show_login_window

if __name__ == "__main__":
    # Configurar senha mestre se necessário
    if not validate_master_password("senha_teste"):
        setup_master_password("senha_teste")

    # Iniciar a interface
    show_login_window()
