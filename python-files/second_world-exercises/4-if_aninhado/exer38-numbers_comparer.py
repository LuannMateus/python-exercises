from os import system

print('\033[1;34m-=-' * 12)
print('\033[4;31m\t<-- Numbers... -->\033[m')
print('\033[1;34m-=-' * 12)

n1 = int(input('\033[1;37mEnter with the first number: '))
n2 = int(input('Enter with the second number: '))
system('clear')
print('\033[1;34m-=-' * 15)
print('\033[4;31m\t<-- Numbers Comparing... -->\033[m')
print('\033[1;34m-=-' * 15)

if n1 > n2:
    print('\033[1;37mThe first number [{}] is biggest with second number [{}]'.format(n1, n2))
elif n2 > n1:
    print('\033[1;37mThe second number [{}] is biggest with first number [{}]'.format(n2, n1))
else:
    print('\033[1;37mThere is no greater value, the two are equal!')
print('-=-' * 15)
  