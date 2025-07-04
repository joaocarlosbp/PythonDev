filmInception = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8,
    }
print(type(filmInception))
# 1- buscar o tamanho do dicionario
print(len(filmInception))
# 2- buscar o valor de uma chave
print(filmInception["title"])
print(filmInception.get("director"))

#3- buscar apenas as chaves
print(filmInception.keys())

#4- buscar apenas os valores
print(filmInception.values())

#5- buscar os itens do dicionario
print(filmInception.items())

#6- adicionar um novo item
filmInception["box_office"] = 836800000
print(filmInception)

#7- atualizar um item existente
filmInception["rating"] = 9.0
print(filmInception)

#8- remover um item
del filmInception["year"]
print(filmInception)

#9- verificar se uma chave existe
if "director" in filmInception:
    print("Director exists in the dictionary.")

#10- limpar o dicionario
filmInception.clear()
print(filmInception)

#11- atualizar o dicionario com outro dicionario
filmInception["year"] = 2010
filmInception.update({"year": 2012, "rating": 8.5})
print(filmInception)

#12- remover e retornar um item
filmInception.pop("rating")
print(filmInception)

