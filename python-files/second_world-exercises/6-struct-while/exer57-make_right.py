print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Do it right!!'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

gender = str(input('Enter wiht a gender [M/F]: ')).strip().upper()[0]

while gender not in 'MmFf':
    gender = str(input('Invalid option!! Try again!!: ')).strip().upper()[0]
print('Data accepted! Check back often!')
