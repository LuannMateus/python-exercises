'''Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um
valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


# Title;
def title():
    print('\033[1;37m~~' * 20)
    print('Voting System'.center(40))
    print('~~' * 20)


# Function - Voting;
def voting(year):
    from datetime import datetime

    actualYear = datetime.now().year
    age = actualYear - year

    print(f'The age is {age} and your voting is: ', end='')
    if age < 16:
        print('Denied Voting!')
    elif age > 15 and age < 18 or age >= 65:
        print('Optional Voting...')
    else:
        print('Mandatory Vote!')


# Main Code;
title()
voting(int(input('Year of birth: ')))
