'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

from typing import List

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

ficha = list()  # type: List
ans = ''
print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"SCHOOL OF PROGRAMRS":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2

    ficha.append([nome, [n1, n2], media])
    ans = str(input('Você deseja continuar? [S/N]: ')).strip()
    if ans in 'Nn':
        break

print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print('-=' * 3, 'BOLETIM', '-=' * 3)
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
for pos, a in enumerate(ficha):
    print(f'{pos:<4}{a[0]:<10}{a[2]:>8.1f}')
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)

while True:
    esc = int(input('Mostrar notas de qual qual aluno? (999 para parar): '))
    if esc == 999:
        print('FINALIZANDO...')
        break
    if esc <= len(ficha) - 1:
        print(f'O aluno {ficha[esc][0]} tem as notas: {ficha[esc][1]}')
print('<<< VOLTE SEMPRE >>>')
