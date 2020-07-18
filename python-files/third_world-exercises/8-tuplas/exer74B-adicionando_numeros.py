from random import randint

# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('Random numbers'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)
n = tuple(randint(0, 10) for c in range(5))
print(f'Os números sorteados são: {n}', end=' ')
print(end='\n')

print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- The biggest number: {max(n)}\n- The smallest number {min(n)}')
