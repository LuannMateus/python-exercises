print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Biggest and smallest weight'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

for c in range(0, 5):
    weight = float(input('Enther with the weight:(kg) '))
    if c == 0:
        biggest = weight
        smallest = weight
    else:
        if weight > biggest:
            biggest = weight

        if weight < smallest:
            smallest = weight
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('- Biggest weiht: {:.1f} Kg\n- Smallest weight: {:.1f} Kg'.format(biggest, smallest))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

