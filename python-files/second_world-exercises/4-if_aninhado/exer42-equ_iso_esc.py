from os import system

print('\033[1;37m-=-' * 15)
print('\t  <== Triangle ==>')
print('-=-' * 15)
r1 = float(input('Enter with first reta : '))
r2 = float(input('Enter with second reta : '))
r3 = float(input('Enter with third reta : '))

system('clear')

print('=' * 24 )
print('<-- What kind of triangle... -->')
print('-' * 24)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 and r1 == r3:
        print('- Its Equilátero Triangle!')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r3 != r1:
        print('- Its Isósceles Triangle!')
    else:
        print('Its Escaleno Triangle!')
else:
    print('- Its not a TRIANGLE!!!')
print('-' * 15)