from random import randint
from time import sleep
from os import system

color = {
    'clear': '\033[m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'red': '\033[1;31m',
    'blueandwhite': '\033[1;34;40m'
}

print('{}-=-{}'.format(color['yellow'], color['clear']) * 15)
print('\t<-- {}Thinking a number....{} -->'.format(color['red'], color['clear']))
print('{}-=-{}'.format(color['yellow'], color['clear']) * 15)

gues = randint(0, 5)
number = int(input('Make a guess in a number between 0 and 5: '))

system('clear')
sleep(0.5)
print('  <-- Processing. -->')
sleep(0.5)
system('clear')
print('  <-- Processing.. -->')
sleep(0.5)
system('clear')
print('  <-- Processing... -->')
sleep(0.5)
system('clear')

if number == gues:
    print('{}OHHHHHHH NOOOO!!!YOUUU WINN!!!! IMPOSSIBELLEE!'.format(color['red']))
else:
    print('{0}I THINK IN {1} NOT IN {2}!!HAHAHAHA I WINN!!!'.format(color['blueandwhite'], gues, number))
print('-' * 30)
