colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('FLAG IS THE EXIT'))
print('{:^40}'.format('IF YOU WANT STOP, TYPE 999'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

number = accumulator = cont = 0

while number != 999:
    number = int(input('Enter with a {}º number: '.format(cont + 1)))
    if number != 999:
        cont += 1
        accumulator += number

print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- Total numbers entered: {cont}')
print(f'- Total sum between numbers: {accumulator}')
