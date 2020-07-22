'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta.'''

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)
print(f'{"Splitting lists ":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 10)

stack = []
totA = totF = 0

values = str(input('Enter with the expression: '))

for x in values:
    if x == '(':
        stack.append('(')
    elif x == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('The expression is correct.')
else:
    print('The expression is incorrect!')
