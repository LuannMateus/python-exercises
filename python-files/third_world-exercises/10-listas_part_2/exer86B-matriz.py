'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão
3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na
tela, com a formatação correta.'''

from typing import List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"Matriz 3x3":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # type: List
cont = 0
for li in range(0, 3):
    for co in range(0, 3):
        mat[li][co] = input(f'Enter with a number in position [{li},{co}]: ')

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
for li in range(0, 3):
    for co in range(0, 3):
        print(f'[{mat[li][co]:^6}]', end='')
    print()
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)
