from os import system
from time import sleep

colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m'
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^40}'.format('Trating Values'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 
n1 = float(input('Enter with the first number: '))
n2 = float(input('Enter with the second number: '))
code = 1

while code != 5:
    print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 
    print('{:^30}'.format('MENU'))
    print('{}-{}-'.format(colors['red'],colors['white'] ) * 20) 

    print('[1] Sum\n[2] Multiplication\n[3] Biggest Number\n[4] New Values\n[5] Program Exit')
    code = int(input('Enter with the code: '))
    print('{}-{}='.format(colors['red'],colors['white'] ) * 20) 

    if code < 0 or code > 5:
        print('{}INVALID OPTION!!! TRY AGAIN!!'.format(colors['red']))
    else:
        if code == 1:
            print('The sum of {} + {} is: {}'.format(n1, n2, n1 + n2))
        elif code == 2:
            print('The multiplication of {} x {} is: {}'.format(n1, n2, n1 * n2))
        elif code == 3:
            if n1 > n2:
                biggest = n1
            else:
                biggest = n2
            print('Between the numbers {} and {}, the biggest is {}'.format(n1, n2, biggest))
        elif code == 4:
            n1 = float(input('Enter with the first number: '))
            n2 = float(input('Enter with the second number: '))
        else:
            sleep(1)
            system('clear')
            print('EXITING.')
            sleep(1)
            system('clear')
            print('EXITING..')
            sleep(1)
            system('clear')
            print('EXITING...')
            sleep(1)
            system('clear')
            code = 5
