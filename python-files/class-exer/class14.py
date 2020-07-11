n = 1
totP = totI = 0

while n != 0:
    n = int(input('Enter with a number: '))
    if n != 0:
        if n % 2 == 0:
            totP += 1
        else:
            totI += 1
print('- total of pair number: {}\n- Total of odd numbers: {}'.format(totP, totI))