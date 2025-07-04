# sistema para cadastro de filmes

# 1 - lista para armazenar os filmes
filmes = []

# 2 - função para cadastrar filmes
def cadastrar_filme():
    name_filme = input("Digite o nome do filme: ")
    year_filme = input("Digite o ano de lançamento do filme: ")
    genre_filme = input("Digite o gênero do filme: ")

    # 3 - dicionário para armazenar os dados do filme
    filme = {"nome": name_filme, "ano": year_filme, "gênero": genre_filme}
    filmes.append(filme)
    print(f"Filme '{name_filme}' cadastrado com sucesso!")

# 4 - função para exibir os filmes cadastrados
def exibir_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.")
    else:
        print("Filmes cadastrados:")
        for i, filme in enumerate(filmes, 1):
            print(f"{i}. {filme['nome']} ({filme['ano']}) - {filme['gênero']}")
        print()

# menu de opções
def menu():
    while True:
        print("Menu:")
        print("1. Cadastrar filme")
        print("2. Exibir filmes cadastrados")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_filme()
        elif opcao == "2":
            exibir_filmes()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o menu 
menu()
