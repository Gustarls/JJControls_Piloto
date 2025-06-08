import sqlite3
import tkinter as tk
from tkinter import messagebox

# ====== BANCO DE DADOS DE USUÁRIOS ======
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    nivel TEXT NOT NULL
)
""")
conn.commit()

# Usuário padrão (admin) - será inserido apenas se não existir
cursor.execute("SELECT * FROM usuarios WHERE nome = 'admin'")
if not cursor.fetchone():
    cursor.execute("INSERT INTO usuarios (nome, senha, nivel) VALUES (?, ?, ?)", ('admin', 'admin123', 'admin'))
    conn.commit()

# ====== TELA DE LOGIN ======
def abrir_login(callback_ao_logar):
    login_win = tk.Tk()
    login_win.title("Login - J&JControls")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack(pady=5)
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack(pady=5)

    tk.Label(login_win, text="Senha:").pack(pady=5)
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack(pady=5)

    def tentar_login():
        nome = entry_usuario.get()
        senha = entry_senha.get()
        cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
        user = cursor.fetchone()
        if user:
            login_win.destroy()
            callback_ao_logar(user)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    tk.Button(login_win, text="Entrar", command=tentar_login).pack(pady=20)
    login_win.mainloop()
