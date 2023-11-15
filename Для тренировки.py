password = str(input('Enter code'))

def user_func():
    while True:
        user_password = str(input('Ввудите пароль: '))
        if user_password == password:
            print('Door is open')
            break
        else:
            print('Dor blocked')

user_func()

