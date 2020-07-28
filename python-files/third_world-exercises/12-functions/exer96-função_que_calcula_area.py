'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''


# Title;
def title():
    print('\033[1;37m-' * 30)
    print(f'{"Measuring the area²":^30}')
    print('-' * 30)


# Function - Area;
def área(larg, comp):
    area = larg * comp
    print('-' * 30)
    print(f'- The are between {larg} wide and {comp} long will be: {area}m²')


# Main Code;
title()
área(float(input('Wide: (m)')), float(input('Long: (m)')))
