import re

text = "udemy - uma plataforma com muitos cursos de programação"
#1 - indice inicial e final de palavras
#0 - r significa  uma raw string (string bruta)

match = re.search(r'plataforma',text)
print(match.start())
print(match.end())

#2- buscando o indice que possui o ponto
site = 'https://www.udemy.com'
match = re.search(r'\.',site)
print(match)

#3- nuscando uma lista de caracteres dentro de uma frase
pattern = "[g-m]"
result = re.findall(pattern,text)
print(result)

#verificado o inicio de uma strig
rule = r'^A'
phrases = ['A casa esta suja', 'O cachorro esta brincando', 'a lua esta brilhando', 'a lua esta cheia']
for f in phrases:
    if re.match(rule,f):
        print(f"corresponde: {f}")
    else:
        print(f"não corresponde: {f}")


#verificando o final de uma string
rule = r'!$'
phrase2 = 'Estou estudando Python!'
match = re.search(rule,phrase2)
if match:
    print(f"corresponde: {phrase2}")
else:
    print(f"não corresponde: {phrase2}")

