color = {
    'red': '\033[1;31m',
    'yellow': '\033[1;33m',
    'white': '\033[1;37m'
}
print('{}-=-'.format(color['red']) * 15)
print('{}\t<-- Discount of prices -->'.format(color['yellow']))
print('{}-=-'.format(color['red']) * 15)
price = float(input('How much does the product cost R$: '))
discount = price - (0.05 * price)
print('{}======================='.format(color['red']))
print('{}<-- Discount of 5% -->'.format(color['yellow']))
print('{}======================='.format(color['red']))
print('{}Original price: {}$'.format(color['white'], price))
print('{}Price with discount of 5%: {:.2f}$'.format(color['white'], discount))
print('==================================')
