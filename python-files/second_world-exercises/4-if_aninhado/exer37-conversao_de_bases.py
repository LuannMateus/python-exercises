from os import system
from time import sleep

print('\033[1;33m-=-' * 12)
print('\033[4;32m<-- Chose the number base -->\033[m')
print('\033[1;33m-=-' * 12)
print('\033[1;31m1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('-=-' * 12)
code = int(input('Code: '))

if code != 1 and code != 2 and code != 3:
    print('\033[1;31mError!! Code not exist! Try again...')
    print('Erasing.')
    sleep(2)
    system('clear')
    print('Erasing..')
    sleep(0.5)
    system('clear')
    print('Erasing...')
    sleep(0.5)
    system('clear')
    exit()

number = int(input('\033[1;37mWhat number do you want convert: '))

system('clear')

if code == 1:
    print('The number {} in Binário: {}'.format(number, bin(number)[2:]))
elif code == 2:
    print('The number {} in Octal: {}'.format(number, oct(number)[2:]))
elif code == 3:
    print('The number {} in Hexadecimal: {}'.format(number, hex(number)[2:]))
print('-=-' * 15)
