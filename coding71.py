def strength(password):
    list_true = []
    
    if len(password) >= 8:
        list_true.append(True)
    elif len(password) < 8:
        list_true.append(False)
    
    for char in password:
        if char.upper() is True:
            list_true.append(True)
            break
        else:
            list_true.append(False)
            


    print(list_true)

    if all(list_true):
        print("Password is safe.")


password = input("Enter password to check! ")

strength(password)