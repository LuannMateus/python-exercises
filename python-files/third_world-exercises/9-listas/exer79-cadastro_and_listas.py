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
while answer == 'Y':
    values.append(int(input('Enter with a number: ')))
    print(f'{c["white"]}-{c["red"]}--{c["white"]}-' * 15)

    if values.count(values[cont]) > 1:
        print('That number already exist!! Not added to list')
        values.pop(cont)
        cont -= 1
    else:
        print('Added value successfully!!')
    print(f'{c["white"]}-{c["red"]}-{c["white"]}-' * 15)

    answer = str(input('Do you want to continue [Y/N]: ')).upper()
    if answer == 'Y':
        cont += 1
print(f'{c["white"]}-{c["red"]}-{c["white"]}-' * 15)
print(f'- You entered the values: {sorted(values)}')
