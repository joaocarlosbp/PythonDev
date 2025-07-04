import tkinter as tk
from tkinter import messagebox

# Lista de filmes
filmes = []

# Função para cadastrar filme
def cadastrar_filme():
    nome = entry_nome.get()
    ano = entry_ano.get()
    genero = entry_genero.get()

    if not nome or not ano or not genero:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    filme = {
        "nome": nome,
        "ano": ano,
        "genero": genero
    }

    filmes.append(filme)
    atualizar_lista()
    limpar_campos()
    messagebox.showinfo("Sucesso", f"Filme '{nome}' cadastrado!")

# Atualiza a lista de filmes no campo de texto
def atualizar_lista():
    texto_filmes.delete(1.0, tk.END)
    for i, filme in enumerate(filmes, 1):
        texto_filmes.insert(tk.END, f"{i}. {filme['nome']} ({filme['ano']}) - {filme['genero']}\n")

# Limpa os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_genero.delete(0, tk.END)

# Criar a janela
janela = tk.Tk()
janela.title("Cadastro de Filmes")
janela.geometry("400x400")

# Rótulos e entradas
tk.Label(janela, text="Nome do Filme:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Ano de Lançamento:").pack()
entry_ano = tk.Entry(janela)
entry_ano.pack()

tk.Label(janela, text="Gênero:").pack()
entry_genero = tk.Entry(janela)
entry_genero.pack()

# Botão para cadastrar
btn_cadastrar = tk.Button(janela, text="Cadastrar Filme", command=cadastrar_filme)
btn_cadastrar.pack(pady=10)

# Campo para mostrar filmes cadastrados
tk.Label(janela, text="Filmes cadastrados:").pack()
texto_filmes = tk.Text(janela, height=10)
texto_filmes.pack()

# Rodar a janela
janela.mainloop()
# O código acima cria uma interface gráfica simples para cadastrar filmes usando Tkinter.
