'''Aula 20 - Funções: def mostra():'''


def lin():
    print('-' * 30)


lin()
print(f'{"PLAYING":^30}')
lin()
print(f'{"WITH":^30}')
lin()
print(f'{"FUNCTIONS":^30}')
lin()


# Funções com parâmetros:
def titulo(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


titulo('TESTING')
titulo('PARANMETERS')
titulo('IN')
titulo('PYTHON')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')
    print(s)


soma(b=8, a=5)

# Conceito de empacotamento - Passando vários parâmetros:


def contador(* num):
    lin()
    print(f'Recebi os valores {num} e possui {len(num)} números.')


contador(1, 3, 5)
contador(1, 10)
contador(3, 1, 2, 5)

# Usando listas com funções:

valores = list()


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6]
print(f'Lista sem chamar a função dobra: {valores}')
dobra(valores)
print(f'List com o valores dobrados pela função: {valores}')
