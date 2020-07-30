# Function - Increase:
def increase(v, inc):
    result = v + ((inc / 100) * v)
    return rep(result)


# Function - Half:
def half(v):
    result = v / 2
    return rep(result)


# Function - Double:
def double(v):
    result = v * 2
    return rep(result)


# Function - Replace:
def rep(v):
    v = f'{v:.2f}'
    v = v.replace('.', ',')
    return v
