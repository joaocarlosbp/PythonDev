filmsList = ["Top Gun","hulk","Avatar","Titanic","Sonic"]

#tamanho da lista
print(len(filmsList))  # Prints the number of elements in the list

#2 recuperar um item da lista
print(filmsList.index("Avatar"))  # Prints the index of "Avatar" in the list

#3 adicionar um item na lista
filmsList.append("Matrix")  # Adds "Matrix" to the end of the list
print(filmsList)

#4- ordenar a lista
filmsList.sort()
print(filmsList)  # Prints the sorted list

#5- remover um item da lista
filmsList.remove("Avatar")  # Removes "Avatar" from the list
print(filmsList)  # Prints the list after removing "Avatar"

#6- copiar itens de uma lista para outra
filmsCopy = filmsList.copy()  # Creates a copy of filmsList
filmsCopy.remove("Sonic")  # Removes "Sonic" from the copied list
print(filmsCopy)  # Prints the copied list after removing "Sonic"

#7- limpar a lista
filmsList.clear()  # Clears all items from filmsList
print(filmsList)  # Prints the empty list