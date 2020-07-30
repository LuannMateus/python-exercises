# Function - Half of value:
def half(value, fort=False):
    value = value / 2
    if fort:
        return rep(value)
    else:
        return value


# Function - Double of value:
def double(value, fort=False):
    value = value * 2
    if fort:
        return rep(value)
    else:
        return value


# Function - Porcentage decrease:
def increase(value, porc, fort=False):
    value += (porc / 100) * value
    if fort:
        return rep(value)
    else:
        return value


# Function - Porcentage increase:
def decrease(value, porc, fort=False):
    value -= (porc / 100) * value
    if fort:
        return rep(value)
    else:
        return value


# Function - Sumary of values:
def sumary(value, inc, dec):
    print('\033[1;32m', end='')
    print('~~' * 20)
    print('Value Sumary'.center(38))
    print('~~' * 20)
    print(f'Price analyzed: {"R$":>8} {rep(value)}$')
    print(f'Half of price:  {"R$":>8} {half(value, fort=True)}$')
    print(f'Double price:   {"R$":>8} {double(value, fort=True)}$')
    print(f'{inc}% increase:{"R$":>11} {increase(value, inc, fort=True)}$')
    print(f'{dec}% decrease:{"R$":>11} {decrease(value, dec, fort=True)}$')
    print('~~' * 20)
    print('\033[m', end='')


#  Funcition - Formatting:
def rep(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return v
