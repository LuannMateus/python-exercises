'''Exercício Python 081: Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'{"Insert Values":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
values = []
answer = 'Y'
while answer in 'Yy':
    values.append(int(input('Enter with a number: ')))
    answer = str(input('Do you want to contiue [Y/N]: ')).strip().upper()[0]

print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'How many values were entered: {len(values)}')
print(f'Values ordered in descending order: {sorted(values, reverse=True)}')
print('Is there a value of 5 in the list: ', end='')
print("True" if values.count(5) > 0 else "False")
