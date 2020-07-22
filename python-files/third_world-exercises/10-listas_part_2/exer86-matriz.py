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

matriz = []  # type: List
cont = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = input(f'Enter with a number in position [{linha},{coluna}]: ')
        matriz.append(n)

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
for mat in matriz:
    print(f'[ {mat} ]', end='')
    cont += 1
    if cont == 3:
        print()
        cont = 0
