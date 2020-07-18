# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('BANK'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
sacar = float(input('Digite o valor: R$'))
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
total = sacar
ced = 100
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if total >= 0:
            print(f'- Total de cédulas de R${ced}: {cont}')
        if total >= 50:
            ced = 50
        elif total >= 20:
            ced = 20
        elif total >= 10:
            ced = 10
        elif total >= 5:
            ced = 5
        elif total >= 2:
            ced = 2
        elif total >= 1:
            ced = 1
        cont = 0
        if total == 0:
            break
print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('End of cash withdrawal! Check back often!')
