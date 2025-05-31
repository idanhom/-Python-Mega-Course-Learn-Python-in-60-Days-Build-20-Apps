# enter while True loop.

while True:
# declare empty list for password to be stored in, to be checked against

    password_list = []

# enter password, to be stored in above list

    password_list = input("Enter password to check: ")

# start with if-elif-checking
# if: len(password_list) < 9 then print "insufficient"
    if len(password_list) < 9:
        print("Insufficient password")

    elif password_list[0].isdigit():
        
        # here, we've already confirmed password is longer than 9 char

# elif not >= [regex for digit" in password_list: insufficient
    elif password_list[0].
        # now, we're echecking if password_list has digits



# elif not >= 1 [regex for uppercase] in password_list: insufficient
