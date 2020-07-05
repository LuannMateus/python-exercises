'''from math import trunc'''

print('=' * 30)
print('<-- Rounded number -->')
print('=' * 30)
'''
number = float(input('Digite um número: '))
print('-' * 20)
print('<-- Showing rounded number --> ')
print('-' * 20)
print('{} for {}'.format(number, trunc(number)))
print('-' * 20)'''


# Another way;
num = float(input('Digite um número real: '))
print('O valor digitador foi {} e sua porção inteira é '.format(num), end='')
print(int(num))
print('-' * 30)
