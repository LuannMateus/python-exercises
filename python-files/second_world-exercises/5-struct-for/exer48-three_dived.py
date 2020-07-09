from os import system

system('clear')
s = 0
cont = 0
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('ONLY THREE DIVED'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += 1
            s += c
print('The sum of {} odd values is: {}'.format(cont, s))
