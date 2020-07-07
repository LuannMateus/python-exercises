from os import system

print('\033[31m=-=' * 15)
print('<-- Enter the number of meters --> ')
print('=-=' * 15)
meters = float(input('How many meters: '))
system('clear')
print('\033[1;37m=================================')
print('\t<-- Conversion -->')
print('=================================')
print('{} meters for Km: {}km'.format(meters, meters / 1000))
print('{} meters for Hm: {}hm'.format(meters, meters / 100))
print('{} meters for Dam: {}dam'.format(meters, meters / 10))
print('{} meters'.format(meters))
print('{:.1f} meters for centimeter: {:.1f}c'.format(meters, meters * 100))
print('{:.1f} meters for millimeter: {:.1f}mm'.format(meters, meters * 1000))
print('=========================================')
