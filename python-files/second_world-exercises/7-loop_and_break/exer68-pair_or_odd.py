from random import randint

# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

cont = 0

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('PAIR OR ODD'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

while True:
    computer = randint(0, 10)

    print('{}-{}='.format(colors['red'], colors['white']) * 20)
    print('{:^40}'.format('PAIR OR ODD'))
    print('{}-{}='.format(colors['red'], colors['white']) * 20)
    n = int(input('Enter with a number: '))
    playerV = str(input('Chosen PAIR OR ODD: ')).strip().upper()
    print('{}-{}='.format(colors['red'], colors['white']) * 20)
# Game logic;
    if n + computer % 2 == 0:
        print(f'The sum of {n} and {computer}.Total of {n + computer} is PAIR')
    else:
        print(f'The sum of {n} and {computer}.Total of {n + computer} is ODD')

    if n + computer % 2 == 0 and playerV == 'PAIR':
        cont += 1
        print('PLAYR WIN\nLETS GAME AGAIN...')

    elif n + computer % 2 != 0 and playerV == 'ODD':
        cont += 1
        print('PLAYR WIN\nLETS GAME AGAIN...')
    else:
        print('COMPUTER WIN\nGAME OVER!')
        break

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print(f'- Total of consecutives victories: {cont}.')
print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^50}'.format('END'))
