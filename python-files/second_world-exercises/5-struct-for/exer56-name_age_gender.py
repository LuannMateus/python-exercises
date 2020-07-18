color = {
    'red': '\033[1;31m',
    'white': '\033[1;37m'
}
print(f'{color["red"]}-{color["white"]}=' * 15)
print('{:^30}'.format('Name, Age and Gender'))
print(f'{color["red"]}-{color["white"]}=' * 15)
avarege = 0.0
old = 0
totW = 0
age = 0

for c in range(1, 5):
    print(f'------------- {c}º -------------')
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

print(f'{color["red"]}-{color["white"]}=' * 15)
print('- Age avarege: {}'.format(avarege / 4))
print(f'- The age of the oldest man is {old} year old and is called: {oldMen}')
print(f'- Total of womans under 20 years old: {totW}')
print(f'{color["red"]}-{color["white"]}=' * 15)
