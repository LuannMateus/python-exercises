print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Palíndromo'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

name = str(input('Enter with a name: ')).upper()
noSpace = name.replace(' ', '')
# inverse = name[::-1]
inverse = ''

for c in range(len(noSpace)-1, -1, -1):
    inverse += noSpace[c]
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

if inverse == noSpace:
    print('- A palavra {} É um PALÍNDROMO!'.format(noSpace))
else:
    print('- A palavra {} NÃO é um PALÍNDROMO!'.format(noSpace))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
