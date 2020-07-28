'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do
Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra 'FIM',
o programa se encerrará. Importante: use cores.'''

from time import sleep

# Cores:
c = (
     '\033[m',          # 0 - No color
     '\033[0;30;41m',    # 1 - Red
     '\033[0;30;42m',   # 2 - Green
     '\033[0;30;43m',    # 3 - Yellow
     '\033[0;30;44m',    # 4 - Blue
     '\033[0;30;45m',    # 5 - Purple
     '\033[7;30m'       # 6 - White
    )


# Title;
def title(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


# Function - Help:
def sys(system):
    title(f"Acessing the manual - '{system}'", 4)
    sleep(2)
    print(c[6], end='')
    help(system)
    print(c[0])


# Main Code:
while True:
    title('Help System - Pyhelp', 2)
    hp = str(input('Function or Library: (END TO STOP): ')).strip()
    if hp in 'ENDend':
        break
    else:
        sys(hp)
title('ATÉ LOGO', 1)
