print('=' * 20)
print('<-- Playing with Units of measure -->')
print('=' * 20)
num = int(input('Enter a number with four units: '))
print('-' * 30)
print('- Unit: {}'.format(num // 1 % 10))
print('- Dozens: {}'.format(num // 10 % 10))
print('- Hundred: {}'.format(num // 100 % 10))
print('- Thousand: {}'.format(num // 1000 % 10))
print('-' * 30)
