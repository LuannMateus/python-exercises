print('=' * 30)
print('<-- Travel of Happiness -->')
print('=' * 30)
dis = float(input('How many KM does the trip have: '))
print('-' * 30)
print('<-- How much cost the travel -->')
print('-' * 30)

if dis < 200:
    short = dis * 0.50
    print('- Price for KM: 0.50$')
    print('Your trip is {} km, so the price is: {:.2f}$'.format(dis, short))
else:
    long = dis * 0.45
    print('- Price for KM: 0.45$')
    print('- Your trip is {} km, so the price is: {:.2f}$'.format(dis, long))
print('-' * 30)
