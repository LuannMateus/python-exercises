'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e
tenham resultados aleatórios. Guarde esses resultados em um dicionário em
Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.'''

from typing import Dict, List
from random import randint
from time import sleep
from operator import itemgetter

players = dict()  # type: Dict
ranking = list()  # type: List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"SORTING DICE":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

for count in range(1, 5):
    players[f'players{count}'] = randint(1, 6)

for k, v in players.items():
    print(f'The {k} taked {v}')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
# ranking = sorted(players.items(), key=lambda x: x[1], reverse=True)

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print(f'{c["white"]} {"Players Rank":^30}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
for k, v in enumerate(ranking):
    print(f'- The {k + 1}º place: {v[0]} with dice {v[1]}')
    sleep(1)
