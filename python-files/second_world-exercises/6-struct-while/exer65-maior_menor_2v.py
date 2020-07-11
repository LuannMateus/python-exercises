colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('THE BIGGEST AND THE SMALLEST'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 

resp = 'S'
cont = accumulator = 0

while resp in 'Ss':   
    number = int(input('Enter with the {} value: '.format(cont + 1)))
    accumulator += number
    if cont == 0:
        biggest = smallest = number
    else:
        if number > biggest:
            biggest = number
        if number < smallest:
            smallest = number
    cont += 1
    print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 
    resp = str(input('Do you want continue? [S/N]: ')).upper().strip()[0]
    print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 

print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 
print('- Avarege betweem the numbers: {}'.format(accumulator / cont))
print('- The biggest velue between the numbers is: {}'.format(biggest))
print('- The smallest value between the numbers is: {}'.format(smallest))

