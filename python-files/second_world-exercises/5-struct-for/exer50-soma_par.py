print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Par Sum'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
s = 0

for c in range(0, 6):
    number = int(input('Enter with the {} number: '.format(c + 1)))
    if number % 2 == 0:
        s += number
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('Total sum of PAR numbers: {}'.format(s))