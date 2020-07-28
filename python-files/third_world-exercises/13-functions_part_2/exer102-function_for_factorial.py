'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que
receba dois parâmetros: o primeiro que indique o número a calcular e outro
chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.'''


# Title;
def title():
    print('\033[1;37m~~' * 20)
    print('FACTORIAL'.center(40))
    print('~~' * 20)


# Function - Factorial;
def factorial(num, show=False):
    """
    -> This function shows the factorial of a number.
        - num: Argument that will receive the number to be factored.
        - show: Argument that depending on the boolen value, showing the calc.
        - f: Variable that will calculate the factorial
    -> Thank you for using my function - Luan Mateus.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        print(f'{num}!: ', end='')
        for x in range(num, 0, -1):
            if x == 1:
                print(f'{x} = {f}')
                break
            else:
                print(f'{x} x ', end='')
    else:
        print(f'Factorial Value: {f}')


# Main Code;
title()
n = int(input('Number: '))
show = str(input('You want to show the calculation? [Y/N]: ')).upper()
factorial(n, True if show in 'Y' else False)
