from os import system

print('\033[1;33m-=-' * 15)
print('\033[1;34m\t<-- Calculating the area ->')
print('\033[33m-=-' * 15)
compri = float(input('How many meters long is the wall: '))
larg = float(input('How many meters wide is the wall: '))
area = compri * larg
system('clear')
print('\033[36m====================')
print('\033[1;32m   <-- Results -->')
print('\033[36m====================')
print('\033[1;37mTo paint a wall of {}m² area'.format(area), end=' ')
print('will be {} liters of ink'.format(area / 2))
