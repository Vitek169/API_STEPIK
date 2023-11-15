def cod():
    while True:
        cod_safe = '07011991'
        cod_user = str(input('Enter your cod: '))
        if cod_user == cod_safe:
            print('Open this safe')
            break
        else:
            print('Cod is not')



cod()

