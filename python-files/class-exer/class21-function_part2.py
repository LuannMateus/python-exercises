'''Comando help(), DocStrings, Parâmetro opcional,
escopo local e global e return'''

# Comando help: Comando que ver a docsString da função chamada.
help(print)
help(input)


# DocStrings:
'''DocsStrings; Cria um manul de uma função. Para fazer isso
é necessário abrir três aspas duplas, colocar o manual e fechar com
mais três aspas duplas.
'''


def fatorial(num=0):
    """
    -> É uma função usada para mostrar o fatorial de um número.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


help(fatorial)


# Parâmetros opcional: Basicamente, você pre-define um valor no parâmetro.
'''O parâmetro opcional se trata de uma pre-definição do argumento, onde
você sabe quantos argumentos serão passados, mas caso, ele não seja, a função
já tem um valor pre-definido, fazendo que a função execute normalmente.
'''


def soma(n1, n2, n3=0):
    s = n1 + n2 + n3
    return s


print(soma(2, 3))


# Escopos - Locais e os globais;
'''Existem dois tipos de variáves, as locais, ondem só existem na função
e as globais, ondem englobam todo o código. Quando uma variável é criada
dentro de alguma função, ele é o que chamamos de variável local, existindo
apenas dentro da função. Caso, por exemplo, quisermos passar um variável global
como argumento e influciar tal variável, usamos o global (variáve) para
avisar que aquele variável irá ser global'''


def mostraV(b):
    global a

    a = 4
    c = 2 + 1
    print(f'- A({a}) B({b})\n - C{c}')


a = 2
mostraV(a)
print(a)

# Comand Return - Retornar valores em funções;
'''O comando return, retorna valores que as funções podem proporcionar,
caso sejá de uso tais valores. Para isso, você pode mostrar de forma
instântanea os valor do retorno ou guarda-ló em uma variável.'''


def retornaSoma(n1, n2):
    s = n1 + n2
    return s


# Mostrando o retorno:
print(retornaSoma(2, 5))

# Guardando o retorno em um variável:

result = retornaSoma(2, 5)
print(result)
