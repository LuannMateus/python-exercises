'''Exercício Python 097: Faça um programa que tenha uma função
chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.'''


# Title;
def title():
    print('\033[1;37m~' * 20)
    print(f'{"Adjunting Texts".center(20)}')
    print('~' * 20)


# Function - Center;
def writh(msg):
    tam = int(len(msg) + 4)
    print('~' * tam)
    print(f'{msg.center(tam)}')
    print('~' * tam)


# Main Code;
title()
writh(str(input('Type a mensage: ')))
