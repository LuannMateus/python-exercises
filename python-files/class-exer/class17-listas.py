''' Bricando os os conceitos de lista: append, insert,
.pop, .remove(), .sort(reverse=True);
'''
num = [1, 4, 5, 10, 9]
num[0] = 2
num.append(21)
num.insert(0, 1000)
num.sort()
num.pop()
num.remove(2)
# num.sort(reverse=True)
print(num)
'''

Utilizando concetios de listas
from random import randint
valores = []

for v in range(0, 5):
    valores.append(randint(0, 10 + 1))

for pos, v in enumerate(valores):
    print(f'Na posição {pos} existe o valor {v}...', end='\n')
print('Cheguei ao final da lista!!')
'''

''' Utilizando um input com o append;
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v + 1} número: ')))
'''
'''
# Conceito de copia de listas:
a = [1, 2, 4, 5]
b = a[:]
b[2] = 3
print(a)
print(b)
'''
