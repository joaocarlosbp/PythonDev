#name = input("nome do filme: ")
#ano = int(input("ano de lançamento: "))
#nota = float(input("nota do filme: "))

# Verifica se o filme é recomendado
#if nota >= 8.0 and ano >= 2010:
  #  print(f"{name} é um filme recomendado!")
#else:
 #   print(f"{name} não é um filme recomendado.")

 # outro exemplo condicional
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
operation=input("Digite a operação (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erro: Divisão por zero não é permitida."
else:
    result = "Operação inválida."
print(f"O resultado da operação é: {result}")