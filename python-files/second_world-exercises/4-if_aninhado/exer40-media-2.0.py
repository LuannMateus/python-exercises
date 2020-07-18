
print('\033[1;37m')
print('-=-' * 15)
print('\t  <-- School of Joy -->')
print('-=-' * 15)

n1 = float(input('Enter with first note: '))
n2 = float(input('Enter with second note: '))
m = (n1 + n2) / 2

print('-' * 15)
print('<-- Status -->')
print('-' * 15)
if m < 5:
    print('\033[1;31m- Avarege: {}\n- Reproved!\033[m'.format(m))
elif m >= 5 and m < 7:
    print('\033[1;33m- Avarege: {}\n- Recovery!\033[m'.format(m))
else:
    print('\033[1;32m- Avarege: {}\n- Approved!!!\033[m'.format(m))
print('-=-' * 15)
