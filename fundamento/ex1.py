name1 = input("Primeiro nome: ")
name2 = input("segundo nome: ")
nomeTodo = name1 + " " + name2
print(f"seu nome ao contrario:",name2 + " " + name1)
print(f"Seu nome completo é: {nomeTodo}")
print(f"Seu nome tem {len(nomeTodo)} caracteres")
print(f"Seu nome invertido é: {nomeTodo[::-1]}")
def namePalindromo():
    if name1 == name1[::-1]:
        print(f"{name1} é um palíndromo")
    else:
        print(f"{name1} não é um palíndromo")
namePalindromo()
    
# end def