while True:
    name = input("Hello! What is your name?\n")
    if name.isalpha() and name.istitle():
        break
    elif name.isalpha():
        name = name.capitalize()
        break
    else:
        print("Need to add a valid name with the first letter capitalized (only letters)!")
        
print(f"Nice to meet you, {name}!\n")

while True:
    age_input = input("How old are you?\n")
    if age_input.isdigit():
        age = int(age_input)  # Convertir el resultado en int.
        break
    else:
        print("Please enter a valid input only numbers.")

if age <= 40:
    print(f"Wow!\n{age} years old, you are young!")
else:
    print(f"You look younger for being {age} years old.")
