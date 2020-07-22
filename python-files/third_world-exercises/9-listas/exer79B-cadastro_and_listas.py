'''
Exercício Python 079: Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)
print(f'{"Adding values to a list":^50}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)

answer = 'Y'
values = []
cont = 0
while True:
    num = int(input('Enter with a number: '))

    if num not in values:
        values.append(num)
        print('Added successfully!')
    else:
        print('The number already exist!! Not added to list.')
    answer = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
    if answer in 'Nn':
        break
print(f'{c["white"]}-{c["red"]}-{c["white"]}-' * 15)
print(f'- You entered the values: {sorted(values)}')
