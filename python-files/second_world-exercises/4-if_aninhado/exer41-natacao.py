from datetime import datetime

print('\033[1;37m')
print('-=-' * 10)
print('   <== Doom Swimming ==>')
print('-=-' * 10)

nowYear = datetime.now().year
born = int(input('what year were you born: '.capitalize()))
age = nowYear - born

print('-' * 15)
print('<== Category: Doom Swimming ==>')
print('-' * 15)

if age < 10:
    print('- Age: {}\n- Category: Mirim'.format(age))
elif age < 15:
    print('- Age: {}\n- Category: Infantil'.format(age))
elif age < 20:
    print('- Age: {}\n- Category: Junior'.format(age))
elif age < 21:
    print('- Age: {}\n- Category: Sênior'.format(age))
else: 
    print('- Age: {}\n- Category: Master'.format(age))
print('-=-' * 15)