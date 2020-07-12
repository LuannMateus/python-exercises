# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('BANK'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
sacar = float(input('Digite o valor: '))

cedulas = [1, 10, 20, 50]
c = 3
while sacar > 0:
    qcedulas = sacar // cedulas[c]
    sacar -= qcedulas * cedulas[c]
    if qcedulas > 0:
        print(f'Quantidades de células de {cedulas[c]} foi: {qcedulas}')
    c -= 1
print('end')