print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Name, Age and Gender'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
avarege = 0.0
old = 0
totW = 0
age = 0

for c in range(1, 5):
    print('------------- {}º -------------'.format(c))
    name = str(input('Enter with a name: '))
    age = int(input('Enter with a age: '))
    gender = str(input('Enter with a gender: ')).upper()
    print('-' * 15)
    avarege += age

    if age > old and gender == 'M' or gender == 'MALE':
        old = age
        oldMen = name
    if age < 20 and gender == 'F' or gender == 'FEMALE':
        totW += 1

print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('- Age avarege: {}\n- The name of the oldest man is {} year old and is called: {}\n- Total of womans under 20 years old: {}'.format(avarege / 4, old, oldMen, totW))    
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
