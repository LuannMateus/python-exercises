'''No python, é possível controlar casos erros aconteçam na compilação do seu
código, seja esse um erro de sintaxe, erro de divisão por zero,
entre outros.'''

# Comandos: try: except: else: finally:

try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = n / d
except (ValueError):
    print('Houve um erro de Valor!')
except Exception as erro:
    print(f'O erro foi {erro.__class__}')
except KeyboardInterrupt:
    print('A entrada dos dados foram interrompida!')
else:
    print(f'A divisão entre {n} / {d} será {r} ')
finally:
    print('< Obrigado e volte sempre! >')
