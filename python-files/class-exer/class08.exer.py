import math

number = int(input('Digite um número: '))
raiz = math.sqrt(number)
print('A raiz de {} é: {}'.format(number, math.ceil(raiz)))
