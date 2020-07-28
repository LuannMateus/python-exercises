''' Dicionários em python: dict.keys(), dict.values(), dict.items() '''
from typing import List, Dict
# Estrutura:
locadora = {'titulo': 'Sexta-Feira 13', 'ano': '1980', 'Diretor': 'Lucas'}

# Dicionários: Comandos
print(locadora.keys())
print(locadora.values())
print(locadora.items())

# Usando um laço para mostrar as keys e os valores;
for k, v in locadora.items():
    print(f'O {k} = {v}')

# Posso substituir ou adicionar keys e novos valores:

pessoa = {'nome': 'Luan Mateus', 'Idade': '18', 'sexo': 'M'}  # type: Dict
print(pessoa.items())
pessoa['nome'] = 'Sofia Cruz'
pessoa['peso'] = 56
print(pessoa.items())
'''
# Dicionários dentro de listas;
brasil = list()
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0])
'''
# Usando input:
estado = dict()  # type: Dict
brasil = list()  # type: List

for count in range(0, 2):
    estado['uf'] = str(input('Entre com um estado: '))
    estado['sigla'] = str(input('Entre com a sigla: '))
    brasil.append(estado.copy())

for esta in brasil:
    for k, v in esta.items():
        print(f'A key é {k} e o valor pe {v}')
