from random import choice
from time import sleep
from os import system

colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
}

print('{}-{}='.format(colors['white'], colors['red']) * 25)
print('\t\t{}  JOKENPÔN'.format(colors['white']))
print('{}-{}='.format(colors['white'], colors['red']) * 25)

items = ['ROCK', 'PAPER', 'SCISSORS']
computer = choice(items)

player = str(input('Chosen -> {}Rock, {}Paper or {}Scissors: '.format(colors['red'], colors['green'], colors['white']))).upper()

if player != 'ROCK' and player != 'PAPER' and player != 'SCISSORS':
    print('{}INVALID CHOICE!!! TRY AGAIN!!'.format(colors['red']))
    sleep(1)
    system('clear')
    exit()

print('{}-{}='.format(colors['white'], colors['red']) * 25)
print('\t   The computer will choose.'.upper())
print('{}-{}='.format(colors['white'], colors['red']) * 25)
sleep(2)
print('Im thinking, dont disturb me, human bug')
sleep(1)
system('clear')
print('Im thinking, dont disturb me, human bug.')
sleep(1)
system('clear')
print('Im thinking, dont disturb me, human bug..')
sleep(1)
system('clear')
print('Im thinking, dont disturb me, human bug...')
sleep(1)
system('clear')
print('Im Chose, lets goo, human bug.')
sleep(1)
system('clear')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('{}-{}='.format(colors['white'], colors['red']) * 20)
print('{}Computer chosen: {}\n{}Player chosen: {}'.format(colors['red'], computer, colors['green'], player))
print('{}-{}='.format(colors['white'], colors['red']) * 20)

if computer == 'ROCK' and player == 'SCISSORS' or computer == 'SCISSORS' and player == 'PAPER' or computer == 'PAPER' and player == 'ROCK':
        print('{}-{}='.format(colors['white'], colors['red']) * 20)
        print('\t  {}PLAYER LOSEE!!'.format(colors['red']))
        print('{}-{}='.format(colors['white'], colors['red']) * 20)
        print('{}Computer:HAHA, You cant beat me!!'.format(colors['red']))
        print('{}Player:Fuck!Next time i will win!!'.format(colors['green']))
        print(f'{colors["red"]}Computer:You could try HAHA! You human bug!')
elif computer == player:
    print('{}-{}='.format(colors['white'], colors['red']) * 20)
    print('\t\t{}TIEEE!!'.format(colors['red']))
    print('{}-{}='.format(colors['white'], colors['red']) * 20)
    print(f'{colors["red"]}Computer:Shit!! How it still ties???!!')
    print(f'{colors["green"]}Player:Fuck! Next time i will win!!')
    print(f'{colors["red"]}Computer:You could try HAHA! You human bug!')
else:
    print('{}-{}='.format(colors['white'], colors['red']) * 20)
    print('\t{}  PLAYER WINSS!! '.format(colors['green']))
    print('{}-{}='.format(colors['white'], colors['red']) * 20)
    print('{}Computer:Shit!!'.format(colors['red']))
    print('{}Player:Hehe, I am amazing!!'.format(colors['green']))
    print('{}Computer:Its just Luck, you human bug'.format(colors['red']))
