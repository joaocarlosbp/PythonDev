#lista de filmes
movielist = ["sonic", "mario", "batman", "superman", "thor"]
# iterando valores de uma lista de filmes usando while
index = 0
while index < len(movielist):
    print(movielist[index])
    index += 1

# quando a condiçao for atendida o loop é interrompido
index = 0
while index < len(movielist):
    if movielist[index] == "batman":
        print("batman encontrado")
        break
    print(movielist[index])
    index += 1
# quando a condiçao for atendida o loop é segue
index = 0
while index < len(movielist):
    if movielist[index] == "batman":
        print("batman encontrado")
        index += 1
        continue
    print(movielist[index])
    index += 1

# avaliação do filme com while
movieName = input("Digite o nome do filme: ")
movieRating = int(input("Digite quantas avaliações deseja fazer: "))
total = 0
count = 0
while count < movieRating:
    note = float(input(f"Digite a nota do filme {movieName}: "))
    total += note
    count += 1
if movieRating > 0:
    average = total / movieRating
else:
    average = 0
print(f"A média de avaliações do filme {movieName} é: {average:.2f}")