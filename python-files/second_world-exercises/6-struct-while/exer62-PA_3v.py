colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('PA - 3.0'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
first = int(input('Enter with the FIRST term: '))
reason = int(input('Enter with the REASON: '))

cont = 0
totT = 10
totA = 1
while totA != 0:
    while cont != totT:
        print('{} -> '.format(first), end='')
        first += reason
        cont += 1
    print('END')
    totA = int(input('- How many terms do you want to add: '))
    totT += totA
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print('- Total terms of PA: {}'.format(cont))
