print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
print('{:^30}'.format('Is Primo??'))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)
number = int(input('Enter with a whole number: '))
tot  = 0

if number > 1:
    for c in range(1, number + 1):
        if number % c == 0:
            print('\033[1;31m{}\033[m'.format(c), end=' ')            
            tot += 1
        else:
            print('\033[1;37m{}'.format(c), end=' ')
    if tot > 3:
        print('\n\033[1;37m- The number {} has been divided {}, so its not Prime Number'.format(number, tot))
    else:
        print('\n\033[1;37m- The number {} has been divided {}, so its a Prime Number'.format(number, tot))    
else:
    print('\033[1;37m- The number {} its not a prime number!'.format(number))
print('{}-{}='.format('\033[1;31m', '\033[1;37m') * 15)

   

       

   

