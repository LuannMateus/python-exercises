'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.'''
# colors;
c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)
print(f'{"Biggest and Smallest values in a LIST":^50}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)

values = []
big = small = 0

for count in range(0, 5):
    values.append(int(input('Enter with a number: ')))

print(f'- The biggest values: [{max(values)}] and your position is: ', end='')
for pos, count in enumerate(values):
    if count == max(values):
        print(f'{pos + 1}... ', end='')
print()
print(f'- The smallest values: [{min(values)}] and your position is: ', end='')
for pos, count in enumerate(values):
    if count == min(values):
        print(f'{pos + 1}... ', end='')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)
