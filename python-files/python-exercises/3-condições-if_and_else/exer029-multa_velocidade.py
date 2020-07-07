print('=' * 30)
print('<-- Were you finer?? -->')
print('=' * 30)
vel = int(input('What was your speed in km per hour: '))
if vel > 80:
    print('Você ultrapassou o limite de velocidade!! Você foi multado!!')
    print('Valor da multa R$: {}$'.format((vel - 80) * 7))
else:
    print('Você está dentro dos limites! Sem nenhuma incorrência')
    print('Tenha um bom dia e dirija com segurança!')
print('-' * 30)
