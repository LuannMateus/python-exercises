print('---------------------\n')
print('<-- Is something... ->\n')
print('---------------------\n')
algo = input('Digite algo: ')
print('O {} é do tipo: {}'.format(algo, type(algo)))
print('O {} é alfa númerico: {}'.format(algo, algo.isalnum()))
print('O {} é alfabetico: {}'.format(algo, algo.isalpha()))
print('O {} é ascii: {}'.format(algo, algo.isascii()))
print('O {} é decimal: {}'.format(algo, algo.isdecimal()))
print('O {} é um digito: {}'.format(algo, algo.isdigit()))
print('O {} é um identificador: {}'.format(algo, algo.isidentifier()))
print('O {} é maiúsculo: {}'.format(algo, algo.isupper()))
print('O {} é minúsculo: {}'.format(algo, algo.islower()))
print('O {} é um número: {}'.format(algo, algo.isnumeric()))
print('O {} é um espaço: {}'.format(algo, algo.isspace()))

