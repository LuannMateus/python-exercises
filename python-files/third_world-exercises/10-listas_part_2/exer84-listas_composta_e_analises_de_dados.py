'''Exercício Python 084: Faça um programa que leia nome e peso de várias
pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

from typing import List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

data = list()  # type: List
people = list()  # type: List
heave = light = '0'

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"List of weight":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    data.append(str(input('Enter with a name: ')))
    data.append(float(input('Enter with a weight: kg ')))

    if len(people) == 0:
        heave = light = data[1]
    else:
        if data[1] > heave:
            heave = data[1]
        if data[1] < light:
            light = data[1]

    people.append(data[:])
    data.clear()

    ans = str(input('Do you want to continue? [Y/N]: '))
    if ans in 'Nn':
        break

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print(f'- Total people registered: {len(people)}')
print(f'- The biggest weight is {heave}kg, being the weight of:', end='')
for wei in people:
    if wei[1] == heave:
        print(f'[{wei[0]}]')
print(f'- The smallest weight is {light}kg, being the weight of: ', end='')
for wei in people:
    if wei[1] == light:
        print(f'[{wei[0]}]')
