# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('GUN STORE'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

totSpend = totTh = 0.0
smallest = 0.0
cheap = answer = ' '

while True:
    productName = str(input('What is the product name: '))
    productPrice = float(input('What is the product price: '))
    if totSpend == 0.0 or productPrice < smallest:
        smallest = productPrice
        cheap = productName

    totSpend += productPrice

    if productPrice > 1000:
        totTh += 1
    print('{}-{}='.format(colors['red'], colors['white']) * 20)
    while answer not in 'YN':
        answer = str(input('Do you want to continue?[Y/N]')).strip().upper()[0]
    print('{}-{}='.format(colors['red'], colors['white']) * 20)
    if answer in 'Nn':
        break
    else:
        answer = ' '
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- Total of spend: {totSpend:.2f}$')
print(f'- Total of products over 1000$: {totTh:.0f}')
print('- The cheapest product: ', cheap)
