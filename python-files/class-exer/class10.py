carr = int(input('Quantos anos tem o seu carro: '))
if carr <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é velho!')
print('---END---')

n1 = float(input('Digite  a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa!Parabéns!')
else:
    print('Sua média foi ruim!Estude mais!')
