s = 0

color = {
    'white': '\033[1;37m'
}
while True:
    s += 1
    if s == 100:
        break
print(f'\033[1;37mThe sum between all valueis is {s}')