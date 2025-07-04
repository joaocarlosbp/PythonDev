import hashlib
#verificar algoritmos disponiveis
print(hashlib.algorithms_available)

# verificar algoritmos de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)

# utilizando o sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "a melhor forma de prever o futuro é inventá-lo.".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
