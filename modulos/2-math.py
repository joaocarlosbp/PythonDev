import math

#1-acessar numero pi
print(math.pi)
print(f"{math.pi:.2f}")

#acessar numero de euler
print(math.e)
print(f"{math.e:.2f}")

#3 arredondando numero para cima e para baixo
num = 10.5
print(math.ceil(num)) #arredonda para cima
print(math.floor(num)) #arredonda para baixo

#4-calcular a fatorial de um numero
num2 = int(input("Digite um numero: \n"))
print(math.factorial(num2))

#5 potencia de numeros
print(math.pow(5,5))

#6 raiz quadrada de numeros
print(math.sqrt(25))

#- mdc
mdc = math.gcd(10,5)
print(mdc)

#logaritmo
print(math.log(10))

