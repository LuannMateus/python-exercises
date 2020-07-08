print('=' * 30)
print('<-- Day of salary reajustment-->')
print('=' * 30)
salary = float(input('Enter with your salary: '))

if salary > 1250:
    print('Your salary is superior a 1.250$, so your increase is 10%')
    print('Salary after adjustment: {:.2f}$'.format(salary + (0.1 * salary)))
else:
    print('Your salary is inferior a 1.250$, so your increase is 15%')
    print('Salary after adjustment: {:.2f}$'.format(salary + (0.15 * salary)))
print('-' * 30)
