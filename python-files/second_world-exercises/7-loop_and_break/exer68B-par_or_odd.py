from random import randint

# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

cont = 0

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('Guess what the GAME MASTER chose'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

while True:

    result = randint(0, 1)
    computer = randint(0, 1)

    player = str(input('Chosen PAIR OR ODD: ')).strip().upper()
    print('{}-{}-'.format(colors['red'], colors['white']) * 20)
# Game logic;
    if computer == 0:
        computerR = 'PAIR'
    else:
        computerR = 'ODD'
    if result == 0:
        resultR = 'PAIR'
    else:
        resultR = 'ODD'
    if computerR == resultR:
        print('THE COMPUTER WIN')
        break
    else:
        cont += 1
        print('THE PLAYER WIN')

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print(f'- Total of consecutives victories: {cont}')
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
