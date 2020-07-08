from math import radians, sin, cos, tan

print('=' * 20)
print('<-- Leitor de angulos -->')
print('=' * 20)
ang = float(input('Digite o angulo: '))
ang = radians(ang)
seno = sin(ang)
cosse = cos(ang)
tang = tan(ang)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosse, tang))
print('=' * 20)
