from datetime import date

print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Adulthood or Not'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

totM = 0
totN = 0
yearToday = date.today().year

for c in range(0, 3):
    yearBorn = int(input('What year were you born: '))
    age = yearToday - yearBorn
    if age < 21:
        totN += 1
    else:
        totM += 1 
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('\033[1;34m- Total persons who have not reached the age of majority: {}'.format(totN))
print('\033[1;34m- Total persons who have reached the age of majority: {}'.format(totM))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
