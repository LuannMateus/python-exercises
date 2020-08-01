def readInt():
    while True:
        try:
            numInt = int(input('Enter wiht a Integer number: '))
        except (ValueError, TypeError):
            print('\033[1;31mInvalid Type! Try again\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mThe user chose not to enter this number.\033[m')
            numInt = 0
            break
        else:
            return numInt
            break


def readFloat():
    while True:
        try:
            numFloat = float(input('Enter with a Float number: '))
        except (ValueError, TypeError):
            print('\033[1;31mInvalid Type! Try again')
        except KeyboardInterrupt:
            print('\033[1;31mThe user chose not to enter this number.\033[m')
            numFloat = 0
            return numFloat
            break
        else:
            return numFloat
            break
