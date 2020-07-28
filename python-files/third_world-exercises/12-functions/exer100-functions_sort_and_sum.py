'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5
números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.'''

from random import randint

number = list()


# Title:
def title():
    print('\033[1;37m~' * 50)
    print('BIGGEST AND SUM'.center(50))
    print('~' * 50)


# Function - Sum:
def sumPair(listaP):
    Sum = 0
    for c in listaP:
        if c % 2 == 0:
            Sum += c
    print(f'- Soma entre os valores pares {listaP} será: {Sum}')


# Function - Sort:
def draw():
    for c in range(0, 5):
        number.append(randint(0, 60))
    print(f'- Valores: {number}')


# Main Code:
title()
draw()
sumPair(number)
