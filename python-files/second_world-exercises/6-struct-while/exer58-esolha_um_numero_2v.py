from random import randint
from os import system
from time import sleep

colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'white': '\033[1;37m',
    'yellow': '\033[1;33m'
}

print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('{:^50}'.format('GAME: CHOOSE UNTIL YOU GET IT RIGHT'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20)   
print('{:^50}'.format('Lets Playing a GAME'))
print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
print('Computer: HAHAH, HELLO PLAYER!! HAHAHA, READY FOR LOST AGAIN??!!')
print('Player: Why are you screaming?? Fuck you, i always win, so shut fuck up!')
print('Computer: HAHAHA, Your human bug, lets goo...')

computer = randint(0, 10)
player = 0
right = 0
guess = 0

while right == 0:
   
    print('{}-{}='.format(colors['red'],colors['white'] ) * 20)   
    print('{:^50}'.format('Choose a number'))
    print('{}-{}='.format(colors['red'],colors['white'] ) * 20)   

    player = int(input('Enter with a number between [0] and [10]: '))

    if player < 0 or player > 10:
        system('clear')
        print('{}INVALID NUMBER!!TRY AGAIN!!'.format(colors['red']))
        sleep(2)
        system('clear')
    else:
        print('{}-{}='.format(colors['red'],colors['white'] ) * 20)    
        print('{:^40}'.format('HAHA ITS MY TURN'))
        print('{}-{}='.format(colors['red'],colors['white'] ) * 20)
        sleep(2)
        system('clear')
        sleep(1)
        print('I THINKING, DONT DISTURB ME, HUMAM BUG.')
        sleep(1)
        system('clear')
        print('THIS BUG THINKS CAN WIN FROM ME..')
        sleep(1)
        system('clear')
        print('FOOLISH, HAHAHHA...')
        sleep(1)
        system('clear')

        if computer > player:
            tip = 'Player, try a large number...'
        elif player > computer:
            tip = 'Player, try a smaller number...'

        if computer == player:
            print('{}-{}='.format(colors['white'], colors['red']) * 25)
            print('\t{}       PLAYER WINSS!! '.format(colors['green']))
            print('{}-{}='.format(colors['white'], colors['red']) * 25)
            print('{}Computer: NOOOOOOO, FUCKKK I AM THE COMPUTER, WHO I LOST THIS SHIT???!!'.format(colors['red']))
            print('{}Player: HAHAHA I TOLD YOU, I ALWAYS WIN!!'.format(colors['green']))
            print('{}Computer: FUNCKKKKKK YOUUUUU!!!'.format(colors['red']))
            right = 1
        else:
            guess += 1
            print('{}-{}='.format(colors['white'], colors['red']) * 25)
            print('\t{}      PLAYER LOSEE!!'.format(colors['red']))
            print('{}-{}='.format(colors['white'], colors['red']) * 25)
            print('{}Computer: HAHAHA, I AM THE BEST!!'.format(colors['red']))
            print('{}Player: YOU CHETING!!'.format(colors['green']))
            print('{}Computer: FUNCKKKKKK YOUUUUU!!!'.format(colors['red']))
            print('{}GAME MASTER: {}'.format(colors['yellow'], tip))
            print('{}Computer: HEYYYYYY, THIS IS CHEATERRRR!!!'.format(colors['red']))
            print('{}Player: Thanksss!!'.format(colors['green']))
print('{}-{}='.format(colors['white'], colors['red']) * 25)  
print('{:^50}'.format('END GAME'))         
print('{}-{}='.format(colors['white'], colors['red']) * 25)
print('- Total Player GUESSES to win: {}'.format(guess))
