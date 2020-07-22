'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que mantenha separados os
valores pares e ímpares. No final, mostre os valores
pares e ímpares em ordem crescente.'''

from typing import List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"List of weight":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

pairAndOdd = [[], []]  # type: List

for count in range(0, 7):

    n = int(input(f'Enter with {count + 1}º number: '))

    if n % 2 == 0:
        pairAndOdd[0].append(n)
    else:
        pairAndOdd[1].append(n)
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print(f'- The pair values is: {sorted(pairAndOdd[0])}')
print(f'- The odd values is: {sorted(pairAndOdd[1])}')
