'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.'''

from typing import Dict, List

player = dict()  # type: Dict
matches = list()  # type: List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"TI Football":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

player['name'] = str(input('Name: '))
player['matches'] = int(input('Matches: '))


for count in range(0, player['matches']):
    matches.append(int(input(f'Goals in matche {count + 1}: ')))

player['goals'] = matches[:]
player['total'] = sum(player['goals'])

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print(player)
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

print('-=' * 6, f'{"Statisc":^10}', '=-' * 6)
for k, v in player.items():
    print(f'- {k.capitalize()}: {v}')
print('-=' * 6, f'{"Statisc about the MATCHES":^10}', '=-' * 6)
print(f'Fotball player {player["name"]} playing {player["matches"]} matches')
for k, v in enumerate(player['goals']):
    print(f'- In match {k + 1}, he did {v} goals.')
print(f'It was a total of {player["total"]} goals.')
