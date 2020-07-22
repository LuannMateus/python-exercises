'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'{"Insert Values":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)

values = list()

for cont in range(0, 5):
    n = int(input('Enter with a number: '))

    if cont == 0 or n > values[-1]:
        values.append(n)
        print(f'Value added in postion {cont}...')
    else:
        pos = 0
        while pos < len(values):
            if n <= values[pos]:
                values.insert(pos, n)
                print(f'Value added in position {pos}...')
                break
            pos += 1
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'- Ordered values: {values}')
