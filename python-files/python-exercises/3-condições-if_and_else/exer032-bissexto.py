from datetime import date

print('=' * 30)
print('<-- Leap Year -->')
print('=' * 30)
year = int(input('Enter the year: '))
print('-' * 30)
print('<-- Its Leap? -->')
print('-' * 30)
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print('The year {} its Leap Year!!'.format(year))
else:
    print('The year {} Its not Leap Year!'.format(year))
print('-' * 30)
