# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('TIME TABLES - MULTIPLICATION'))
print('{:^40}'.format('-1 IS A FLAG'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

while True:
    n = int(input('Enter with a number: '))
    if n < 0:
        break
print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('TIMES TABLE'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
for c in range(1, 11):
    print(f'{c:^2} x {n} = {c * n}')
print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('END OF TIMES TABLE! EXIT....')
