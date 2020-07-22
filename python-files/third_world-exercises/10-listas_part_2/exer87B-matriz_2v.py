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

print(f'{c["white"]}-{c["red"]}==' * 14)
print(f'{c["white"]} {"Matriz 3x3":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 14)

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # type: List
cont = totalS = totalT = big = 0

for li in range(0, 3):
    for co in range(0, 3):
        mat[li][co] = randint(1, 60)

        if mat[li][co] % 2 == 0:
            totalS += mat[li][co]

# Showing the matriz;
for li in range(0, 3):
    for co in range(0, 3):
        print(f'\t[{mat[li][co]:^5}]', end='')
    print()
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)

print(f'- Total sum of all values: {totalS}')
for li in range(0, 3):
    totalT += mat[li][2]
print(f'- Total sum of values in the third column: {totalT}')
for li in range(0, 3):
    if li == 0 or mat[1][li] > big:
        big = mat[1][li]
print(f'- The highest value of the second line: {big}')
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)
