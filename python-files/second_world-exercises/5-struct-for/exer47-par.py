from os import system

system('clear')
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('ONLY PAR'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

for c in range(2, 51, 2):
    print('{:^30}'.format(c))
