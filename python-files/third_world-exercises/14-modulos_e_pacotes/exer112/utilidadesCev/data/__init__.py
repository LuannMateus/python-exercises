def data(value, inc, dec, fort=False):
    from utilidadesCev import coins

    while True:
        if value in '':
            print('\033[1;31mERROR! Value is EMPTY ')
        elif value.isalpha() is True:
            print('\033[1;31mERROR! The value is a alpha')
        else:
            value = value.replace(',', '.')
            coins.sumary(float(value), inc, dec, fort)
            break

        value = input('Try again! Money: ').strip()
