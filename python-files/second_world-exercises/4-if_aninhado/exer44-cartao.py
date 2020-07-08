from os import system

print('\033[0;32m$*$' * 15)
print('\t\033[1;31m<-==- Wicked CAPITALISM -==->')
print('\033[0;32m$*$' * 15)

productPrice = float(input('How much does the product cost R$: '))
print('-' * 10)
print('Payment Method')
print('-' * 10)
print('[1] - In cash/Bank check')
print('[2] - Parcel')
print('-' * 10)
code = int(input('Choice: '))

system('clear')

if code == 1:
    print('- Your payment method is In cash')
    print('# Your discont is 10%')
    print('# Price: {}$'.format(productPrice - (0.1 * productPrice)))
elif code == 2:
    print('Your payment method is Parcel')
    part = int(input('How often: '))
    if part == 1:
        print('- 1x Parcel')
        print('- Your discont is 5%')
        print('- Price: {:.2f}$'.format(productPrice - (0.1 * productPrice)))
    elif part == 2:
        print('- 2x Parcel')
        print('- Your dont have discount')
        print('- Price: {:.2f}$'.format(productPrice))
    elif part > 2:
        print('- {}x Parcel'.format(part))
        print('- Your have interest of 20% per month')
        print('- Price: {:.2f}$'.format(productPrice))
        print('- Because of interest you will pay: {}$'.format(productPrice + (0.2 * productPrice)))
else:
    print('INVALID CODE!! TRY AGAIN!!')