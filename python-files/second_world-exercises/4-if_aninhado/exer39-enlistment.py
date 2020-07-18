from datetime import datetime
from time import sleep

colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

nowYear = datetime.now().year

print('{}-{}={}-'.format(colors['white'], colors['red'], colors['white']) * 17)
print('\t{}    Welcome to Enlistment'.format(colors['white']))
print('{}-{}={}-'.format(colors['white'], colors['red'], colors['white']) * 17)
print('\033[1;34m-=-' * 10)
print('\033[4;35m\t<-- Gender -->\033[m')
print('\033[1;34m-=-' * 10)
print('\033[1;34m[1] - Male')
print('\033[1;35m[2] - Female')
print('\033[1;37m-=-' * 10)
gender = int(input('Code: '))

print('\033[1;34m-=-' * 10)
print('\033[4;31m\t<-- Age -->\033[m')
print('\033[1;34m-=-' * 10)
born = int(input('\033[1;37mWhat year were you born: '))
sleep(0.5)

age = nowYear - born

print('\033[1;34m-=-\033[1;37m' * 15)
if age >= 0 and age < 18 and gender == 1:
    enlistYear = 18 - age + nowYear
    print('- Actual age: {}'.format(age))
    print('- You will need to enlist in the army!')
    print('- {} year(s) left to enlist'.format(18 - age))
    print('- Your enlistment is going to be in {}'.format(enlistYear))
elif age == 18 and gender == 1:
    enlistYear = 18 - age + nowYear
    print('- Actual age: {}'.format(age))
    print('- Its time to enlist in the army!')
    print('- Your enlistment is in {} year(s)'.format(enlistYear))
elif age > 18 and gender == 1:
    enlistYear = 18 - age + nowYear
    print('- Actual age: {}'.format(age))
    print('- Enlistment time has passed!')
    print('- {} year(s) passed to enlist.'.format(age - 18))
    print('- His enlistment was in  {}'.format(enlistYear))
elif gender == 2 and age >= 0:
    print('- Actual age: {}'.format(age))
    print('You dont need to enlist!')
elif age < 0:
    print('- Erro!! The age is not logic!')
print('\033[1;34m-=-' * 15)
