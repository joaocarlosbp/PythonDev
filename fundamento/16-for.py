#lista de filmes
movielist = ["sonic", "mario", "batman", "superman", "thor"]

#1 iterando com for
for movie in movielist:
    print(movie)

#2 quando a condiçao for atentidada o loop é incerrupto
for movie in movielist:
    if movie == "batman":
        print("Encerrando")
        break
    print(movie)

    # 3 quando a condiçao for atentidade o loo vai para a proxima iteraçao
for movie in movielist:
    if movie == "batman":
        print("Pular")
        continue
    print(movie)

    #avaliaçao do filme
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliaçoes deseja fazer: "))

total = 0
for i in range(movieRating):
    rating = int(input(f"Digite a nota do filme : "))
    total += rating

    if movieRating >= 0 :
        average = total / movieRating
    else:
        average = 0
print(f"A média de avaliação do filme {movieName} é: {average:.2f}")