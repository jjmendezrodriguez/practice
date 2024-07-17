import json

def preguntas():
    user_data = {}

    while True:
        name = input("Hello! What is your name?: ")
        if name.isalpha() and name.istitle():
            user_data['name'] = name
            break
        elif name.isalpha():
            name = name.capitalize()
            user_data['name'] = name
            break
        else:
            print("Need to add a valid name with the first letter capitalized (only letters)!")
            
    print(f"Nice to meet you, {name}!\n")

    while True:
        age_input = input("How old are you?: ")
        if age_input.isdigit():
            age = int(age_input)
            user_data['age'] = age
            break
        else:
            print("Please enter a valid input only numbers.")
    
    if age < 0:
        print("You are not born yet!")
    elif age == 0 or age <= 5:
        print("You are a baby!")
    elif age <= 40:
        print(f"Wow!\n{age} years old, you are young!")
    else:
        print(f"You look younger for being {age} years old.")
    
    # Guardar los datos del usuario en un archivo JSON
    with open('user_data.json', 'w') as json_file:
        json.dump(user_data, json_file)
    
    return user_data
