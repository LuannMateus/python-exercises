# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('REGISTER'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 

m18 = totM = totW20 = 0
gender = resp = ' '
while True:
    age = int(input('Enter with your age: '))
    while gender not in 'MmFf':
        gender = str(input('Enter with your gender [M/F]: ')).strip().upper()[0]
    print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 

    if age > 18:
        m18 += 1
    if gender in 'Mm':
        totM += 1
    if gender in 'Ff' and age < 20:
        totW20 += 1
    while resp not in 'YyNn':
        resp = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]
    print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 
    if resp != 'Y':  
        break
    gender = resp = ' '
    
print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 
print(f'- Total of people over 18 yers: {m18}\n- Total of mens: {totM}\n- Total of womans under 20 years: {totW20}')
