print('\033[1;37m============================')
print('<-- Salary increase Day -->')
print('============================')
salary = float(input('Enter your monthly salary R$: '))
increase = salary + (0.15 * salary)
print('===========================')
print('<-- Increase of 15% -->')
print('==========================')
print('Your original salary: {}$'.format(salary))
print('You salary with 15% increase: {:.2f}$'.format(increase))
print('======================================')