colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('FACTORIAL'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
num = int(input('Enter wiht a number: '))
c = num
f = 1

print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
