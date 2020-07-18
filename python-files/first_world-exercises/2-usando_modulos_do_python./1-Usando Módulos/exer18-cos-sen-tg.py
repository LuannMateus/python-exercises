from math import radians, sin, cos, tan

print('=' * 20)
print('<-- Leitor de angulos -->')
print('=' * 20)
ang = float(input('Digite o angulo: '))
ang = radians(ang)
seno = sin(ang)
cosse = cos(ang)
tang = tan(ang)
print(f'- Seno: {seno:.2f}\n- Cosseno: {cosse:.2f}')
print(f'Tangente: {tang:.2f}')
print('=' * 20)
