'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''

from typing import Dict

student = dict()  # type: Dict

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"SCHOOL OF PROGRAMRS":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

student['name'] = str(input('Enter with a name: '))
student['average'] = float(input(f'Enter with average of {student["name"]}: '))

if student['average'] >= 7:
    student['situation'] = 'Approved!'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recuperation'
else:
    student['situation'] = 'Disapproved!!!'
print(f'{c["white"]}-{c["red"]}--{c["white"]}' * 15)
for k, v in student.items():
    print(f'- {k.capitalize()} is the same than {v}')
