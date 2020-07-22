'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.'''
# colors;
c = {
    'white': '\033[1;37m',
    'red': '\033[1;31m'
}
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)
print(f'{"Biggest and Smallest values in a LIST":^50}')
print(f'{c["white"]}-{c["red"]}=={c["white"]}-' * 15)

values = []
totB = totS = maximo = 0

for cont in range(0, 5):
    values.append(int(input(f'Enter with the {cont + 1}º number: ')))
valuesB = values[:]
valuesS = values[:]

for exist in values:
    if exist == max(values):
        totB += 1
    if exist == min(values):
        totS += 1

maximo = max(values)
minimo = min(values)

print(f'{c["white"]}-{c["red"]}-{c["white"]}' * 10)
print(f'- The biggest value is: {max(values)} and your position is: ', end='')
if totB > 1:
    for cont in range(0, totB):
        print(f'{valuesB.index(maximo) + 1:.>5}', end=' ')
        valuesB.pop(valuesB.index(maximo))
        if cont == totB - 1:
            break
        else:
            valuesB.insert(valuesB.index(maximo), minimo)
else:
    print(valuesB.index(maximo) + 1)

print(f'\n- The smallest value is {min(values)} and your position is ', end='')
if totS > 1:
    for cont in range(0, totS):
        print(f'{valuesS.index(minimo) + 1:.>5}', end=' ')
        valuesS.pop(valuesS.index(minimo))
        if cont == totS - 1:
            break
        else:
            valuesS.insert(valuesS.index(minimo), maximo)
else:
    print(valuesS.index(minimo) + 1)
print(end='\n')
print(f'{c["white"]}-{c["red"]}-{c["white"]}' * 10)
