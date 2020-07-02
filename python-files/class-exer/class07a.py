# nome = str(input('Digite o seu nome: '))
# print('Olá, é um grande prazer em tem conhecer, {:=^20}'.format(nome))

# Mostrando todos os operadores aritmeticos;
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
sub = n1 - n2
divisao = n1 / 2
multi = n1 * n2
div_int = n1 // n2
pot = n1 ** n2
print('---------------------')
print('<-- Resultado -->')
print('---------------------')
print('A soma será: {} \nA subtração será: {} \nA divisão será: {} \nA multi será: {}'.format(soma, sub, divisao, multi), end='')
print('\nA divisão inteira será: {} \nApotênciação será: {}'.format(div_int, pot))

