print('\033[1;34m-\033[1;32m=\033[1;34m-' * 16)
print('\t\033[1;35m<=-= Is yout weight right? =-=>')
print('\033[1;34m-\033[1;32m=\033[1;34m-' * 16)

weight = float(input('How much do you weight: (kg) '))
height = float(input('What is your height: (m) '))

IMC = weight / pow(height, 2)

print('\033[1;32m-\033[1;34m=\033[1;32m-' * 16)
print('\t<=-= How is your weight? =-=>')
print('\033[1;32m-\033[1;34m=\033[1;32m-' * 16)

if IMC < 18.5:
    print('\033[1;33mYou are underweight!! Be careful!')
elif IMC >= 18.5 and IMC <= 25:
    print('\033[1;32mCongratulations!! You are at ideal weight!')
elif IMC > 25 and IMC <= 30:
    print('\033[1;33mBe careful! Are you Overweight!')
elif IMC > 30 and IMC <= 40:
    print('\033[31mALERT!!You are Obese!!Please you have to lose weight!')
else:
    print('\033[1;31mDANGEROUS ZONE!!You have morbid obesity!!Call a doctor!')
print('-' * 20)
