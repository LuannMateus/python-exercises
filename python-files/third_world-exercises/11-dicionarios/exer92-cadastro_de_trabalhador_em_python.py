'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário.Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''

from typing import Dict
from datetime import datetime

actualYear = datetime.today().year
job = dict()  # type: Dict

c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}

print(f'{c["white"]}-{c["red"]}==' * 15)
print(f'{c["white"]} {"Working Portfolio":^40}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)

job['name'] = str(input('Name: '))
born = int(input('Year of birth: '))
job['age'] = actualYear - born
job['ctp'] = int(input('Work Portfolio (0 is your not have): '))
if job['ctp'] != 0:
    job['hiring'] = int(input('Year of hiring: '))
    job['salary'] = float(input('Saláry: R$'))
    job['retirement'] = (job['hiring'] - born) + 35
print(f'{c["white"]}-{c["red"]}=={c["white"]}' * 15)
for k, v in job.items():
    print(f'- {k.capitalize()} has a value {v}')
