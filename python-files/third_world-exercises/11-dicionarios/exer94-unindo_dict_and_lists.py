'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de
várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

from typing import Dict, List

features = dict()  # type: Dict
people = list()  # type: List
ans = ''
totA = average = 0.0

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"Registry":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    features['name'] = str(input('Enter with a name: '))

    while True:
        features['gender'] = str(input('Gender [M/F]: ')).upper()[0]
        if features['gender'] in 'MF':
            break
        else:
            print('ERROR! Please, enter onlye [M] or [F]')

    features['age'] = int(input('Enter with your age: '))
    totA += features['age']

    people.append(features.copy())
    features.clear()

    while True:
        ans = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]

        if ans in 'YN':
            break
        else:
            print('ERROR! Answer onlye [Y] or [N]')

    if ans in 'Nn':
        break
average = totA / len(people)

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print('-=' * 6, f'{"Status":^10}', '=-' * 6)
print(f'- Total of register people: {len(people)}')
print(f'- Average ages: {average:.2f}')
print('- The registered womans were: ', end='')
for w in people:
    if w['gender'] in "Ff":
        print(f'{w["name"]}', end=' ')
print('\n- List of people how are above average age: ', end='\n')
for k, v in enumerate(people):
    if v['age'] > average:
        print(f'Name = {v["name"]}; Gender = {v["gender"]}; Age = {v["age"]};')
print('<<< ENDING... >>>')
