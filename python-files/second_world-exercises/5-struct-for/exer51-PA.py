print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('PA - Arithmetic Progression'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

first = int(input('Enter with the first term: '))
reason = int(input('Enter with a reason: '))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

for c in range(0, 10):
    print('{:^30}'.format(first))
    first += reason
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
