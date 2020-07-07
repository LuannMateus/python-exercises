from random import randint
from time import sleep

print('-=-' * 15)
print('    <-- Thinking a number.... -->')
print('-=-' * 15)

gues = randint(0, 5)
number = int(input('Make a guess in a number between 0 and 5: '))

print('-' * 20)
print('  <-- Processing... -->')
print('-' * 20)
sleep(3)
if number == gues:
    print('OHHHHHHH NOOOO!!!YOUUU WINN!!!! IMPOSSIBELLEE!')
else:
    print('I THINK IN {0} NOT IN {1}!!HAHAHAHA I WINN!!!'.format(number, gues))
print('-' * 30)
