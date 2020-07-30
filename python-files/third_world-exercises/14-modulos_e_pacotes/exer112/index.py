from utilidadesCev import data

# Main code:
print('\033[1;31m-=' * 20)
print('PROGRAMMER BANK'.center(40))
print('-=' * 20)
money = input('Money R$: ').strip()
data.data(money, 80, 35, fort=True)
