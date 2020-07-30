# Cores:
c = (
     '\033[m',          # 0 - No color
     '\033[0;31m',    # 1 - Red
     '\033[0;30;42m',   # 2 - Green
     '\033[0;30;43m',    # 3 - Yellow
     '\033[0;30;44m',    # 4 - Blue
     '\033[0;30;45m',    # 5 - Purple
     '\033[7;30m'       # 6 - White
    )


def mostracor(n):
    print(c[n])

