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

values = []
true = 1
for cont in range(0, 5):
    values.append(int(input('Add a value: ')))

    true = 1
    for cou in values:
        if values[cont] < cou:
            print(f'# Value added in position {values.index(cou)}...')
            values.insert(values.index(cou), values[cont])
            values.pop(cont + 1)
            true = 0
    if true == 1:
        print('# Value added at the end of list...')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'- Ordered values: {values}')
