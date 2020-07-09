from os import system

system('clear')
s = 0
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('ONLY THREE DIVED'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print('Soma total de ímpares: {}'.format(s))
