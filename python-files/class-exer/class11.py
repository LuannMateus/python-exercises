print('\033[7;37mOlá mundo!\033[m')

cores = {
    'limpa': '\033[m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'red': '\033[4;31m'
}

print('{}-{}={}-{}'.format(cores['amarelo'], cores['azul'], cores['amarelo'], cores['limpa']) * 15)
print('<-- {}\tPlaying with colors{} -->'.format(cores['red'], cores['limpa']))
print('{}-{}={}-{}'.format(cores['amarelo'], cores['azul'], cores['amarelo'], cores['limpa']) * 15)
