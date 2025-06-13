def strength(password, list_true):
    list_true = []
    
    if len(password) >= 8:
        list_true.append(True)
    elif len(password) < 8:
        list_true.append(False)
    
    for char in password:
        if char.isupper():
            list_true.append(True)
            break
        else:
            continue
            
    for char in password:
        if char.isdigit():
            list_true.append(True)
            break
        else:
            continue
        
    print(list_true)
    
    if all(list_true) and len(list_true) == 3:
        return ("Strong Password")
    else:
        return("Weak Password")        

input_password = input("Enter password: ")
print(strength(input_password, list))

