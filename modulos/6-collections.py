from collections import Counter,namedtuple,deque
from operator import itemgetter

#1 lista de frutas(contagem)
fruits = ['banana', 'apple', 'orange', 'banana', 'apple', 'banana',"tangerine"]
print(Counter(fruits))

#2- tupla nomeada
game = namedtuple('game',['name','price','note'])
g1= game("fifa",102,8.5)
g2= game("minecraft",120,7.5)
print(g1)
print(g2.price)

#3- ordenar dicionarios
students = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 91}
a = sorted(students.items(), key=itemgetter(0))
print(a)

#4- deque
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)