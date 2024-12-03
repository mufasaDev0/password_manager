import tkinter as tk
from tkinter import simpledialog, messagebox
from storage import save_passwords, load_passwords
from auth import validate_master_password, setup_master_password

def show_login_window():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Solicitar senha mestre
    password = simpledialog.askstring("Login", "Digite a senha mestre:", show='*')

    if not validate_master_password(password):
        messagebox.showerror("Erro", "Senha mestre incorreta!")
        return

    # Carregar a interface principal
    show_main_window(password)

def show_main_window(master_password):
    root = tk.Tk()
    root.title("Gerenciador de Senhas")

    tk.Label(root, text="Lista de Senhas:").pack()
    password_list = tk.Listbox(root)
    password_list.pack()

    def add_password():
        new_password = simpledialog.askstring("Nova Senha", "Digite a nova senha:")
        # Adicionar lógica de salvar senhas
        # ...

    tk.Button(root, text="Adicionar Senha", command=add_password).pack()
    root.mainloop()
