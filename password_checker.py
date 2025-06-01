



password_list = []
values = []

while True:

    password_list = input("Enter password to check: ")

    if len(password_list) >= 8:
        values.append(True)
    elif len(password_list) <= 7:
        values.append(False)

    for password in password_list:
        for char in password:
            if char.isdigit():
                values.append(True)
                break
        else:
            values.append(False)
            print(f"Password {password_list[0]} contains at least one digit.")
            break
            
    for password in password_list:
        for char in password:
            if char.isupper():
                values.append(True)
                break
        else:
            values.append(False)
            print(f"Password {password_list[0]} contains at least one uppercase letter.")
            break
        

    



    if all(values) == True:
        print("Password is good.")
    else:
        print("Password does not fulfill requirements.")

    print(values)