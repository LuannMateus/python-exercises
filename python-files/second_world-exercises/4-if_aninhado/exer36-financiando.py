from os import system
from time import sleep
color = {
    'blue': '\033[1;34m',
    'yellow': '\033[1;33m'
}

print('{}-=-'.format(color['yellow']) * 12)
print('{}<-- Approve or dispprove -->'.format(color['blue']))
print('{}-=-'.format(color['yellow']) * 12)
houseValue = float(input('\033[1;37mHow much cost the house: R$'))
salary = float(input('How much do you earn: R$'))
years = float(input('In how many years will you pay the house: '))
parcel = houseValue / (years * 12)

system('clear')
print('Processing.')
sleep(0.5)
system('clear')
print('Processing..')
sleep(0.5)
system('clear')
print('Processing...')
sleep(0.5)
system('clear')

if (0.3 * salary) <= parcel:
    print('\033[1;31mThe 30% limit has been exceeded! You funding is refused')
else:
    print('\033[1;32mCongratulation!! You funding has been accepted!')
print('-=-' * 15)
