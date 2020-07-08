print('=' * 55)
print('<-- Which is the biggest and which is the smallest -->')
print('=' * 55)
n1 = float(input('Enter with ter first number: '))
n2 = float(input('Enter with ter second number: '))
n3 = float(input('Enter with ter third number: '))
# Initialization of variables;
big = n1
small = n1
# Calculation the biggest number;
if n2 > big and n2 > n3:
    big = n2
if n3 > big and n3 > n2:
    big = n3
# Calculation the smallest number;
if n2 < small and n2 < n3:
    small = n2
if n3 < small and n3 < n2:
    small = n3
print('-' * 30)
print('        Analysing....')
print('-' * 30)
print('- The biggest number is {:.1f}'.format(big))
print('- The smallest number is {:.1f}'.format(small))
print('-' * 30)
