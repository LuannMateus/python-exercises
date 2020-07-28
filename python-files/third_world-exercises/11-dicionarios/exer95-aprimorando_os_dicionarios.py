'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
'''
from typing import Dict, List

features = dict()  # type: Dict
players = list()  # type: List
gols = list()   # type: List
ans = ''
totG = data = 0

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"TI FOTBALL 2.0":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    features['name'] = str(input('Name: '))
    matches = int(input('Matches: '))

    for x in range(0, matches):
        gols.append(int(input(f'Goals in matche {x + 1}: ')))

    features['matcheG'] = gols[:]
    features['totG'] = sum(features["matcheG"])
    players.append(features.copy())
    features.clear()
    gols.clear()

    ans = str(input('Do you want to continue? [Y/N]: ')).strip()

    if ans in 'Nn':
        break
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print(f'Cod. {"Name":>3} {"Goals":>10} {"Total":>10}')
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)

for k, v in enumerate(players):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)

while True:

    data = int(input('Show data for which player? - [999 for STOP]: '))

    if data == 999:
        break
    elif data >= len(players):
        print('ERRO!! The player does not exist! Try again')
    else:
        print(f'-- PLAYER SURVEY - {players[data]["name"]}')
        for k, v in enumerate(players[data]['matcheG']):
            print(f'In game {k + 1} make {v} goals.')
print('<< Check back often >>')
