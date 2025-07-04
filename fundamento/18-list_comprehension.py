#listando valores de 0 a 10 menores que 4
#for i in range(10):
 #   if i < 4:
 #       print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

#lista de filmes
movielist = ["sonic", "mario", "batman", "superman", "thor"]

#fimes que possuam a letra "e" no titulo
moviesWithE = [movie for movie in movielist if "e" in movie.lower()]
print(moviesWithE)

#filmes que eu assisti
moviesWatched = [movie for movie in movielist if movie != "sonic"]
print(moviesWatched)

#encontrando filmes pelo nome
while True:
    searchName = input("Digite o nome do filme para buscar (ou sair para encerrar): ")
    if searchName.lower() == "sair":
        print("Busca encerrada.")
        break
    foundMovies = [movie for movie in movielist if searchName.lower() in movie.lower()]
    if foundMovies:
        print("Filmes encontrados:")
        for foundMovies in foundMovies:
            print(foundMovies)
    else:
        print("Nenhum filme encontrado com esse nome.")