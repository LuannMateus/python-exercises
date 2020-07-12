# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('999 IS A FLAG'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 

Sum = cont = 0
while True:
    n = int(input('Enter with the number: '))
    if n != 999:
        Sum += n
        cont += 1
    else:
        break
print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 
print(f'- Total Sum between all numbers: {Sum}')