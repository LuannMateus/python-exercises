from time import sleep
import os

print('-=-' * 15)
print('\t   <-- Is a Triangle? -->')
print('-=-' * 15)
r1 = float(input('Enter in the firt reta: '))
r2 = float(input('Enter in the second reta: '))
r3 = float(input('Enter in the third reta: '))

os.system('clear')
print('\t  Analysing. ')
sleep(1)
os.system('clear')
print('\t  Analysing.. ')
sleep(1)
os.system('clear')
print('\t  Analysing... ')
sleep(1)
os.system('clear')

print('-' * 35)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\tCan form a Triangle')
else:
    print('\tCannot form a Triangle')
print('-' * 35)
