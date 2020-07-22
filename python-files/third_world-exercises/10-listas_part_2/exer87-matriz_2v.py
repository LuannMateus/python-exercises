'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

from typing import List
from random import randint

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"Matriz 3x3":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

matriz = []  # type: List
cont = totalS = totalT = big = 0

for lin in range(0, 3):
    for col in range(0, 3):
        n = randint(1, 60)

        if lin == 1:
            if n > big:
                big = n
        if n % 2 == 0:
            totalS += n

        if col == 2:
            totalT += n
        matriz.append(n)

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
# Showing the matriz;
for mat in matriz:
    print(f'[ {mat} ]', end='')
    cont += 1
    if cont > 2:
        print()
        cont = 0
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

print(f'- Total sum of all values: {totalS}')
print(f'- Total sum of values in the third column: {totalT}')
print(f'- The highest value of the second line: {big}')
