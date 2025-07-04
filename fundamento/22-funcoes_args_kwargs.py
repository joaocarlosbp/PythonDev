"""
*args- utilizamos quando nao temos certeza de quantos argumentos queremos ter  numa funçao, os argumentos sao  passados por uma tupla

"""
def sum (*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print(f"soma é: {sumTotal}")
sum(7)
sum(8,9)
sum(7,9,10,11)

"""**kwargs - utilizamos quando queremos passar argumentos nomeados, os argumentos sao passados por um dicionario
"""
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos: ")
presentation(nome="Python", categoria="backend", level="iniciante")
presentation(nome="JavaScript", categoria="frontend", level="intermediario")
presentation(nome="Java", categoria="backend", level="avancado")
