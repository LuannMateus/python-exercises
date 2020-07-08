from os import system
from time import sleep

print('{}==========================={}'.format('\033[1;32m', '\033[m'))
print('{}<-- Soma entre números -->{}'.format('\033[1;31m', '\033[m'))
print('{}==========================={}'.format('\033[1;32m', '\033[m'))
n1 = int(input('{}Digite o primeiro número: {}'.format('\033[1;34m', '\033[1;32m')))
n2 = int(input('{}Digite o segundo número: {}'.format('\033[1;34m', '\033[1;32m')))
sleep(0.5)
system('clear')
s = n1 + n2
print('{}A soma entre {}{}{} e {}{}{} será: {}{}'.format('\033[1;35m', '\033[1;31m', n1, '\033[1;32m', '\033[1;35m', n2, '\033[1;32m', '\033[1;37m', s))
