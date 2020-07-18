from random import choice

# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('Random numbers'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Os números sorteados são:', end=' ')
for c in range(0, 5):
    num = choice(n)
    print(f'{num}', end=' ')
    if c == 0:
        biggest = num
        smallest = num
    else:
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
print('')
print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- The biggest number: {biggest}\n- The smallest number {smallest}')

'''
n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''
