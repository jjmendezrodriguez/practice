name = input("first name:")

convert = input("\ndo you like to conver miles in km? (yes/no):")

while True:
    if convert == "yes":
        if True:
            miles = input("\nenter miles:")
            km = 1.609
            convert_dist = float(miles) * float(km)
            print(f"\n{name.capitalize()} traveled {convert_dist} km on their bike.")
            break

    elif convert == "no":
        miles = input("\nenter miles:")
        print(f"\n{name.capitalize()} go {float(miles)} faraway in his bike")
        break

    else:
        msg = "please answer yes or no"
        print(f"\n{msg.capitalize()}")
        convert = input("do you like to conver miles in km? (yes/no):")
