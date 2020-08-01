def existFile(name):
    try:
        x = open(name, 'rt')
        x.close()
    except FileNotFoundError:
        return False
    else:
        return True


def creatFile(name):
    try:
        x = open(name, 'wt+')
        x.close()
    except Exception:
        print('There was a mistake! The file could not be created')
    else:
        print('The archive "database.txt" was created successfully')


def register(name, age):
    try:
        x = open('database.txt', 'at')
        x.write(f'{name};{age}\n')
    except Exception:
        print("Something wente wrong! Couldn't add data")
    else:
        print('Data added successfully')
    finally:
        x.close()
