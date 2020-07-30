'''Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga mostrar os números
como um valor monetário formatado.'''

import coin

print('\033[32m-=' * 20)
print('PROGRAMMER BANK'.center(40))
print('-=' * 20)

money = float(input('Money R$: '))

print(f'- Money R$: {coin.rep(money)}$')
print(f'- Half of {coin.rep(money)} will be: {coin.half(money)}$')
print(f'- Double of {coin.rep(money)} will be: {coin.double(money)}$')
print(f'- The increase value 10% will be: {coin.increase(money, 10)}$')
