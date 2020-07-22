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

pair = values[:]
odd = values[:]

for v in pair:
    if v % 2 != 0 or v == 1:
        pair.remove(v)

for v in odd:
    if v % 2 == 0:
        odd.remove(v)

print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'List all values: {values}')
print(f'List with pair values: {pair}')
print(f'List with odd values: {odd}')
