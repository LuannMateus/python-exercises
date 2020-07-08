from os import system
# Entre com um nome e apresente um mensagem
system('clear')
nome = input('\033[1;34mDigite seu nome\033[1;32m: ')
print('{}É um prazer em te conhecer, {}{}{}!'.format('\033[1;34m', '\033[1;31m', nome, '\033[m'))
