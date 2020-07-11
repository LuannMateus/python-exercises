colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('FIBONACCI'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 
elements = int(input('How many elemenst will the fibonacci sequence have: '))
t1 = 0
t2 = 1
print('{} -> {} -> '.format(t1, t2), end='')
cont = 3
while cont <= elements:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('END')
