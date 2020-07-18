from os import system
from time import sleep

system('clear')

print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Times Table 2.0'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('[1] - Adição(+)\n[2] - Subtração(-)', end='')
print('\n[3] - Multiplicação(*)\n[4] - Divisão(/)')
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
code = int(input('Chose the option: '))

if 1 < code > 4:
    print('ERROR!!Invalid Code!! Try again!!')
    sleep(1)
    system('clear')
    exit()
else:
    number = int(input('What number do you want to do the table: '))
    n = number
    print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
    print('{:^30}'.format('Times Table'))
    print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
    if 1 == code:
        for c in range(1, 11):
            print('{:^8}{:^2} + {} = {:.0f}'.format('', c, number, number + c))
    elif 2 == code:
        for c in range(1, 11):
            n += 1
            print('{:^8}{:^2} - {} = {:.0f}'.format('', n, number, n - number))
    elif 3 == code:
        for c in range(1, 11):
            print('{:^8}{:^2} * {} = {:.0f}'.format('', c, number, number * c))
    else:
        for c in range(1, 11):
            print('{:^8}{:^4} / {} = {:.1f}'.format('', n, number, n / number))
            n += number
