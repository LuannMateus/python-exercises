# Colors
colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['red'], colors['white']) * 20)
print('{:^40}'.format('There are vowels'))
print('{}-{}-'.format(colors['red'], colors['white']) * 20)

names = ('DOING', 'EXERCISES', 'IS', 'THE', 'BEST', 'WAY', 'TO', 'LEARN')

for word in names:
    print(f'\nIn the word {word} we have ->', end=' ')
    for letter in word:
        if letter in 'AEIOU':
            print(f'{letter}'.lower(), end=' ')
print(end='\n')
print('{}-{}='.format(colors['red'], colors['white']) * 20)
