# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print(f'{colors["red"]}-{colors["white"]}=' * 20)
print('{:^40}'.format('Numbers and Inputs'))
print(f'{colors["red"]}-{colors["white"]}=' * 20)

tot9 = 0

number = (int(input('First number: ')),
          int(input('Second number: ')),
          int(input('Third number: ')),
          int(input('Fourth number: '))
          )
if 3 in number:
    existThree = str(number.index(3) + 1)
else:
    existThree = 'Not exist'

print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- The nine appeared: {number.count(9)} time(s)')
print(f'- The three first appeared in the index: {existThree}')
print('- The pars numbers: ', end='')
for c in number:
    if c % 2 == 0:
        print(f'({c})', end=' ')

print(end='\n')
print(f'{colors["red"]}-{colors["white"]}=' * 20)
