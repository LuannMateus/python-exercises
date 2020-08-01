from lib.color import c
from lib.data import register
from os import system


# Menu:
def layout():
    print(f'{c["w"]}', end='')
    print('-' * 20)
    print('MAIN MENU'.center(20))
    print('-' * 20)
    print(f'{c["b"]}', end='')
    print(f'{c["r"]}1{c["w"]} - View registered people')
    print(f'{c["r"]}2{c["w"]} - Register new people')
    print(f'{c["r"]}3{c["w"]} - TRUNCAT')
    print(f'{c["r"]}4{c["w"]} - Exit the system')
    print(f'{c["w"]}', end='')
    print('-' * 20)
    print(f'{c["e"]}', end='')


# Title:
def title(msg):
    tam = len(msg) + 20
    print('-' * tam)
    print(f'{msg}'.center(tam))
    print('-' * tam)


# Function = Read integers:
def readInt():
    while True:
        try:
            age = int(input('Enter with a age: '))
        except Exception:
            print(f'{c["r"]}Invalid Value! Try again!')
        else:
            return age
            break


# Function - Handling the data:
def data():
    layout()
    while True:
        try:
            code = int(input(f'{c["w"]}\nYour option: '))
        except Exception:
            print(f'{c["r"]}INVALID OPTION')
        else:
            if code == 1:
                title('View registered people')
                print(f'Name{"Age":>30}')
                print('-' * 42)
                x = open('database.txt')
                for line in x:
                    data = line.split(';')
                    data[1] = data[1].replace('\n', '')
                    print(f'{data[0]:<30}{data[1]:>3} year(s)')
            elif code == 2:
                title('Register new people')
                name = str(input('Enter with a name: '))
                age = readInt()
                register(name, age)
            elif code == 3:
                x = open('database.txt', 'w')
                x.truncate()
                print('Values successfully deleted')
            elif code == 4:
                system('clear')
                title('Exit the system...')
                break
            else:
                print(f'{c["r"]}ERROR! Try again!')
