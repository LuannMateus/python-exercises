def half(value, fort=False):
    value = value / 2
    return value if fort is False else rep(value)


def double(value, fort=False):
    value = value * 2
    return value if fort is False else rep(value)


def increase(value, porc, fort=False):
    value += (porc / 100) * value
    return value if fort is False else rep(value)


def decrease(value, porc, fort=False):
    value -= (porc / 100) * value
    return value if fort is False else rep(value)


#  Funcition - Formatting
def rep(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return v
