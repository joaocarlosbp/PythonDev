filmsTuple = ("Top Gun","hulk","Avatar","Titanic","Sonic")
print(type(filmsTuple))

#buscar os dois primeiros elementos
print(filmsTuple[0:2])

#buscar o ultimo elemento
print(filmsTuple[-1])

#3- buscar filmes ate uma determinada posiçao
print(filmsTuple[:3])

#4- buscar filmes a partir de uma determinada posiçao
print(filmsTuple[2:])

#5- buscar filmes pelo nome
print(filmsTuple.index("Avatar"))