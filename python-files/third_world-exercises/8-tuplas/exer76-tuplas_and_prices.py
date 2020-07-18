# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print(f'{colors["red"]}-{colors["white"]}=' * 20)
print(f'{"Gun Store":^40}')
print(f'{colors["red"]}-{colors["white"]}-' * 20)

productsAndPrices = ('Shotgun', 200, 'Assalt Rifle', 3000, 'Pistol', 100)

print('{:^40}'.format('Price List'))

for c in range(0, len(productsAndPrices)):
    if c % 2 == 0:
        print(f'{productsAndPrices[c]:.<30}R$: ', end='')
    else:
        print(f'{productsAndPrices[c]}')
print(end='\n')
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
