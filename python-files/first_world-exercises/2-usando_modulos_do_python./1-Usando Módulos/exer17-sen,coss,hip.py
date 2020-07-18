from math import hypot

print('=' * 20)
print('<-- Trigonométria da Alegria -->')
print('=' * 20)
'''
cato = float(input('Digite o valor do cateto oposto: '))
catd = float(input('Digite o valor do cateto adjacente: '))
hip = (cato ** 2 + catd ** 2) ** (1/2)
print('A hipotenusa vale: {:.2f}'.format(hip))
'''
# Using method hypot

cato = float(input('Digite o valor do cateto oposto: '))
catd = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(cato, catd)
print('A hipotenusa vale: {:.2f}'.format(hip))
