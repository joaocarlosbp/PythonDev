filmsSet = {"Top Gun","hulk","Avatar","Titanic","Sonic"}
print(type(filmsSet))

# 1- buscar o tamanho do set
print(len(filmsSet))

#2-  true e 1 sao o mesmo valor
print(True == 1)
exempleSet = {1,2.8,"sonic 2",True,}
print(exempleSet)

#3- add item de outro set
filmsSet.update(exempleSet)
print(filmsSet)

#4- remove um item do set
filmsSet.remove("Top Gun")
print(filmsSet)