'''Exercício Python 082: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'{"Splitting lists ":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)

answer = 'Y'
values = []
pair = []
odd = []

while answer == 'Y':
    values.append(int(input('Enter with a number: ')))

    answer = str(input('Do you want to continue [Y/N]: ')).strip().upper()[0]

for v in values:
    if v % 2 == 0:
        pair.append(v)
    elif v % 2 == 1:
        odd.append(v)

print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'- List all values: {values}')
print(f'- List with pair values: {pair}')
print(f'- List with odd values: {odd}')
