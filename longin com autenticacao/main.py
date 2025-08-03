import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

# Criação do banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Função de cadastro
def cadastrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if not usuario or not senha:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (usuario, senha_hash))
        conn.commit()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe.")

# Função de login
def login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    cursor.execute("SELECT password FROM usuarios WHERE username = ?", (usuario,))
    resultado = cursor.fetchone()

    if resultado and bcrypt.checkpw(senha.encode('utf-8'), resultado[0]):
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Interface gráfica
janela = Tk()
janela.title("Sistema de Login")

Label(janela, text="Usuário:").grid(row=0, column=0, padx=10, pady=10)
entry_usuario = Entry(janela)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10)
entry_senha = Entry(janela, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=10)

btn_login = Button(janela, text="Login", command=login)
btn_login.grid(row=2, column=0, padx=10, pady=10)

btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=2, column=1, padx=10, pady=10)

janela.mainloop()


