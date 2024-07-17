from input import preguntas

def login():
    email = 'jo'
    password = 'p1'
    
    while True:
        login_cread = input('Enter your email:')
        login_password_cread = input('Enter your password:')
        
        if login_cread == '':
            print('Need to add an email!')
            continue  # Pedir entrada de nuevo
        elif login_cread != email:
            print('Email is not registered')
            continue  # Pedir entrada de nuevo
        else:
            if login_password_cread == '':
                print('Need to add a password!')
                continue  # Pedir entrada de nuevo
            elif login_password_cread == password:
                print('You have access!')
                return True
            else:
                print('Your email or password is wrong')
                continue  # Pedir entrada de nuevo

if __name__ == "__main__":
    if login():
        user_info = preguntas()
        print(f"User information: {user_info}")
    else:
        print('Need to login!')
