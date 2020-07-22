'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a
criar palpites.O programa vai perguntar quantos jogos serão gerados e vai
sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from typing import List
from random import randint
from time import sleep

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"MEGA SENA":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

gues = list()  # type: List
games = list()  # type: List
n = count = x = 0
chose = int(input('How many games do you want me to draw: '))
print(f'{" SORTING":=>15} {chose} {"GAMES ":=<15}')

for count in range(0, chose):
    while True:
        n = randint(1, 60)
        if n not in gues:
            gues.append(n)
            x += 1
        if x > 5:
            break
    x = 0
    gues.sort()
    games.append(gues[:])
    gues.clear()
for pos, g in enumerate(games):
    print(f'Game {pos}: {g}')
    sleep(1)

print(f'{c["white"]}{" < GOOD LUCK! > ":=^30}')
