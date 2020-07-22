'''Listas compostas;'''

pessoas = list()
dados = list()
totOver = totUnder = 0
for count in range(0, 2):
    dados.append(str(input('Nomes: ')))
    dados.append(str(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for c in pessoas:
    if c[1] > '21':
        print(f'{c[0]} tem mais de 21 anos!')
        totOver += 1
    else:
        print(f'{c[0]} tem menos de 22 anos!')
        totUnder += 1
print(f'Total de pessoas com mais de 21 anos: {totOver}')
print(f'Total de pessoas com menos de 22 anos de idade {totUnder}')
