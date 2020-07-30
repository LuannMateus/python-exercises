'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um
programa que importe esse módulo e use algumas dessas funções.'''

import coin

print('\033[1;31m~' * 40)
print('  PLAYING WITH MÓDULO'.center(40))
print('~' * 40)

v = float(input('Enter with a value: '))
print(f'Value R$: {v}$')
print(f'The increase value 10% will be R$: {coin.increase(v)}$')
print(f'The decrease value 15% will be R$: {coin.decrease(v)}$')
print(f'The double value will be R$: {coin.double(v)}$')
print(f'The half value will be R$: {coin.half(v)}$')
print('-=' * 20)
