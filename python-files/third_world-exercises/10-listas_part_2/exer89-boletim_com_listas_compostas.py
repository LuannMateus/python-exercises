'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

from typing import List

students = list()  # type: List
notes = list()  # type: List
names = list()  # type: List
answer = ''
average = grade = 0
c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"SCHOOL OF PROGRAMRS":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    names.append(str(input("Enter with studant's name: ")))
    notes.append(float(input('Enter with grade 1: ')))
    notes.append(float(input('Enter with grade 2: ')))

    names.append(notes[:])
    students.append(names[:])

    answer = str(input('- Do you want to continue? [Y/N]: ')).strip()
    if answer in 'Nn':
        break

    names.clear()
    notes.clear()
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
print('No. \tName \t\tAverage')
for pos, count in enumerate(students):
    average = (count[1][0] + count[1][1]) / 2
    print(f'{pos} \t{count[0]}\t{average:>5}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

while True:
    grade = int(input('# Which students grade shows? [999 TO STOP]: '))

    if grade == 999:
        break
    else:
        print(f'- The grade of {students[grade][0]} its {students[grade][1]}')
    print(f'{c["white"]}-{c["red"]}-{c["white"]}' * 15)
