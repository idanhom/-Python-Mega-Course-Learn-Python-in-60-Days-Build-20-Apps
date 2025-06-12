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
        elif char.isupper() != True:
            list_true.append(False)
            break
            
    # for digit in password:
    #     if digit.isdigit():
    #         list_true.append(True)
    #         break
    #     elif digit.isdigit() != True:
    #         list_true.append(False)
    #         break





    print(list_true)

    if all(list_true):
        print("Password is safe.")


password = input("Enter password to check! ")

strength(password)