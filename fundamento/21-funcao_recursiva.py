#1 - fatorial de um numero:
#1-> 1*1 1
#2-> 2*1 2
#3-> 3*2*1 6
def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))
number= int(input('Digite um numero: '))
print(f'O fatorial de {number} é {fatorial(number)}')


#2 - soma total de um numero:
def soma_total(num):
    if num == 0:
        return 0
    else:
        return (num + soma_total(num - 1))
numb = int(input('Digite um numero: '))
print(f'A soma total de {numb} é {soma_total(numb)}')

