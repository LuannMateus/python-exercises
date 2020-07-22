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
n = x = 0
chose = int(input('How many games do you want me to draw: '))
print(f'{" SORTING":=>15} {chose} {"GAMES ":=<15}')

for count in range(0, chose):
    while x < 6:
        n = randint(1, 60)
        if n not in gues:
            gues.append(n)
            x += 1
    x = 0
    sleep(1)
    print(f'Game {count + 1}: {gues}')
    gues.clear()
print(f'{c["white"]}{" < GOOD LUCK! > ":=^30}')
