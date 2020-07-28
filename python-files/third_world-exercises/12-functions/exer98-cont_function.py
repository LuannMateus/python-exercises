'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
três contagens através da função criada:'''

from time import sleep


# Title;
def title(h1):
    print('\033[1;37m~' * 20)
    print('COUNTING'.center(20))
    print('~' * 20)


# Function - Fixe Counting;
def cont(start, end, step):
    print(f'A)From {start} to {end} in step 1: ')
    for c in range(start, end, step):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('-> END\n')


# Function - Pesonal Counting;
def count(start, end, step):
    print('-=-' * 10)
    if end > start:
        if step <= 0:
            print('Logic Error! Considering Step 1')
            step = 1
        for c in range(start, end + 1, step):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('-> END')
    elif end < start:
        if step == 0:
            print('Logic Erro! Considering Step -1')
            step = -1
        if step > 0:
            step *= -1
        for c in range(start, end, step):
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print('-> END')


# Main Code;
title('COUNTING')
cont(1, 11, 1)
cont(10, -1, -1)

print('-=' * 20)
print('C) Now its your turn to costomize the count:')

count(int(input('Start: ')), int(input('End: ')), int(input('Step: ')))
