# https://redeploy.udemy.com/course/the-python-mega-course/learn/quiz/5902640#overview


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
        print("Password is safe.")
    else:
        print("Password is unsafe")

    print(list_true)



password = input("Enter password to check! ")

strength(password)