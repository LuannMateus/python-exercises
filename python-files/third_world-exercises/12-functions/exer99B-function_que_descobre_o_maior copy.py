'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que
analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep


# Function - Biggset Value;
def biggest(* num):
    print('\033[1;37m-=' * 20)
    print('Analyzing past values: \n---'.center(50))
    big = cont = 0
    for c in num:
        print(c, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            big = c
        else:
            if c > big:
                big = c
    print(f'- [{len(num)}] values were analyzed!')
    print(f'The biggest values is: {big}')


# Main Code;
biggest(1, 3, 4, 5, 9)
biggest(1, 3, 4, 11)
biggest(1000, 1)
biggest()
