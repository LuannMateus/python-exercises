'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele
marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.'''


# Title;
def title():
    print('\033[1;37m~~' * 20)
    print('FOTBALL'.center(20))
    print('~~' * 20)


# Function - Data;
def data():
    n = str(input('Name: '))
    g = (input('Goals: '))

    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() in '':
        token(goals=g)
    else:
        token(n, g)


# Function - token;
def token(name='<unknown>', goals=0):
    print(f'Player {name} scored {goals} goals.')


# Main Code;
title()
data()
