'''Exercício Python 114: Crie um código em Python que teste se o site pudim
está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception:
    print('Could not access site.')
else:
    print('Everything is fine!')
    print(site.read())
