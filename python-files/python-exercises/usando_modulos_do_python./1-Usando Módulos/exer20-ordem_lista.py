from random import shuffle

print('=' * 20)
print('<-- Get names -->')
print('=' * 20)
n1 = input('Type the first name: ')
n2 = input('Type the second name: ')
n3 = input('Type the third name: ')
n4 = input('Type the fourth name: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
