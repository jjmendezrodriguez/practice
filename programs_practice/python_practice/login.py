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

def register():
    preguntas()

def help():
    print('login -> to log into your account\n--')
    print('register -> register a new account\n--')
    print('help -> print posible commands\n--')
    print('quit -> to exit VisionPlus')

def VisionPlus():
    print("======use help for commands====\n")
    while True:
        command = input("Enter your command: ")
        match command:
            case "help":
                help()
            case "login":
                login()
            case "register":
                register()
            case "quit":
                return 0
            case _:
                print("command not found: use help for commands")

if __name__ == "__main__":
    VisionPlus()
    # if login():
    #     user_info = preguntas()
    #     print(f"User information: {user_info}")
    # else:
    #     print('Need to login!')
