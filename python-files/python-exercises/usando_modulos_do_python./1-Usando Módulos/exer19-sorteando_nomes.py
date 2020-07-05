from random import choice

print('=' * 20)
print('<-- Get names -->')
print('=' * 20)
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))
