'''Exercício Python 108: Adapte o código do desafio #107,
criando uma função adicional chamada moeda() que consiga mostrar os números
como um valor monetário formatado.'''

import coin

print('\033[1;31m-=' * 20)
print('PROGRAMMER BANK'.center(40))
print('-=' * 20)
money = float(input('- Money R$: '))
print(f'- Half of value {coin.rep(money)}: {coin.half(money, fort=True)}$')
print(f'- Double of value {coin.rep(money)}: {coin.double(money, fort=True)}$')
print(f'- The increase 10% will be: {coin.increase(money, 10, fort=True)}$')
print(f'- The decrease 13% will be: {coin.decrease(money, 13, fort=True)}$')
print('-=' * 20)
