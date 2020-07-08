from os import system

print('\033[1;33m-=-' * 12)
print('\033[1;34m\t  <-- Média -->')
print('\033[1;33m-=-' * 12)
nota1 = float(input('\033[1;32mDigite a primera nota: '))
nota2 = float(input('Digite a segunda nota: '))
system('clear')
print('\033[1;33m-------------------------')
print('   \033[1;34m<-- Média Final -->')
print('\033[1;33m-------------------------')
print('\033[1;37mNota 1: {}'.format(nota1))
print('Nota 2: {}'.format(nota2))
print('Média entre as notas: {:.1f}'.format((nota1 + nota2) / 2))
