# Pegue o quanto de reais existe e converta para dollars - Date: 01/07/2020;
from os import system

print('\033[1;31m==============================')
print('<-- Conversion of Sadness -->')
print('==============================')
money = float(input('\033[32mHow much money you have R$: '))
system('clear')
print('\033[32m-$-'* 20)
print('\t   <-- Conversion to Dollars -->')
print('-$-' * 20)
print(' $ BRL {}$ for dollars is: USD {:.2f}$'.format(money, money / 5.32))
print('$-$' * 20)
