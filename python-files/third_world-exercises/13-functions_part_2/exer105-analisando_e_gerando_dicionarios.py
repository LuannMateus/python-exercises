'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''


# Title;
def title():
    print('\033[1;37m-=-' * 15)
    print('PROGRAMMERS SCHOOL'.center(40))
    print('-=-' * 15)


# Function - Grades:
def grade(* grades, situ=False):
    situation = dict()
    """
    -> Function that receives an indefinite number of notes.
       :grades: Variable that receive the grades.
       :situ: Boolean values that will show or not a students situation.
       :situation[]: Dictionaries will receive the analyzed values.
    """
    situation['Amount'] = len(grades)
    situation['Biggest'] = max(grades)
    situation['Smallest'] = min(grades)
    situation['Average'] = sum(grades) / situation['Amount']
    if situ is True:
        if situation['Average'] > 6:
            situation['state'] = 'Good Situation!'
        else:
            situation['state'] = 'Bad Situation!'
    print(situation)


# Main Code:
title()
grade(2, 3, 1, 4, 5, 6, situ=True)
