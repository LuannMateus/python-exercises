# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('POR EXTENSO'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
numbers = ('zero', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
           'twelve', 'thirteen', 'fourteen', 'fifteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
resp = 'Y'

while resp == 'Y':
    while True:
        num = int(input('Enter with a number between 0 and 20: '))
        if 0 <= num <= 20:
            print(f'- You entered the number: {numbers[num]}')
            break
        else:
            print('Try again!', end='')
    resp = str(input('You wish to continues [Y/N]: ')).upper()

print('{}-{}-'.format(colors['red'], colors['white']) * 20)
