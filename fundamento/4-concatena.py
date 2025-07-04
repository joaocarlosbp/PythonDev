# utilizando input  
name = input("Digite o nome do filme: \n")
yearLaunch = input("Digite o ano de lançamento : \n")
noteMovie =input("Digite a nota do filme: \n")

print(name)
print(yearLaunch)
print(noteMovie)
# concatenando
print("O filme " + name + " foi lançado no ano de " + str(yearLaunch) + " e obteve a nota " + str(noteMovie) + ".")
# formatando
print(f"O filme {name} foi lançado no ano de {yearLaunch} e obteve a nota {noteMovie}.")
# formatando com .format
print("O filme {} foi lançado no ano de {} e obteve a nota {}.".format(name, yearLaunch, noteMovie))