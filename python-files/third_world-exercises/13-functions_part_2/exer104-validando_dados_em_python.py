'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai
funcionar de forma semelhante 'a função input() do Python, só que fazendo a
validação para aceitar apenas um valor numérico.'''

cores = {
    'white': '\033[1;37m'
}


# Title;
def title():
    print(f'{cores["white"]}~~' * 10)
    print('Validating numbers'.center(20))
    print('~~' * 10)


# Function - inputInt():
def inputInt(name):
    while True:
        num = (input(f'{cores["white"]}{name}'))

        if num.isnumeric():
            num = int(num)
            return num
            break
        if num in '':
            print('\033[1;31mERROR! Is empty!!')
        elif num.isspace() is True:
            print('\033[1;31mERROR! This is a space!!')
        elif num.count('.') > 0:
            print('\033[1;31mERROR! This is a decimal number!!')
        elif num.isalpha() is True:
            print('\033[1;31mERROR! This is a str type!!')
        else:
            return num
            break


# Main Code;
title()
n = inputInt('Enter an integer: ')
print(f'The integer number is {n}')
