




while True:
    values = []

    password = input("Enter password to check: ")

    if len(password) >= 8:
        values.append(True)
    else:
        values.append(False)



    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if has_digit and has_upper:
            break
    values.append(has_digit)
    values.append(has_upper)



    if all(values):
        print("Password is good.")
    else:
        print("Password does not fulfill requirements.")

    print(values)