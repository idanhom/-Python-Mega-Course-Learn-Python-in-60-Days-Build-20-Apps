def strength(password):
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
        
    if all(list_true) and len(list_true) == 3:
        return("Strong Password")
    else:
        return("Weak Password")        

