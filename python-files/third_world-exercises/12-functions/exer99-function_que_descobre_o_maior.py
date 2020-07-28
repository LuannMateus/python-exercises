'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior.'''

from random import randint

values = list()
listV = list()
cont = 6


# Function - Biggset Value;
def biggest(* num):
    print('\033[1;37m-=' * 20)
    print('Analyzing past values: \n---'.center(50))
    for c in num:
        for x in c:
            print(x, end=' ')
    print(f'- [{len(num[0])}] values were analyzed!')
    print(f'The biggest values is: {max(num[0])}')


# Main Code;
for c in range(0, 7):
    if cont == 0:
        values.append(0)
    else:
        for v in range(0, cont, 1):
            values.append(randint(0, 60))
    cont -= 1
    listV.append(values[:])
    values.clear()

for c in range(0, len(listV)):
    biggest(listV[c])
