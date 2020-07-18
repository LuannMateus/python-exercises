# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('CHAMPIONSHIP'))
print('{}-{}='.format(colors['red'], colors['white']) * 20)

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional',
         'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
         'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('{}-{}-'.format(colors['red'], colors['white']) * 20)
print(f'- The first five places: {times[0:5]}')
print(f'- The last placed: {times[-4:]}')
print(f'- List sorted in alplhabetical order: {sorted(times)}')
print(f'- The position of Chapecoense its: {times.index("Chapecoense")}º!')
