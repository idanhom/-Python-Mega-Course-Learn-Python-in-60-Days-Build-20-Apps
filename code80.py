def string_checker(string_to_check):
    length_of_string = len(string_to_check)
    if length_of_string < 8:
        return False
    elif length_of_string >= 8:
        return True

print(string_checker("jsdfd"))
print(string_checker("helllllllooooo"))

