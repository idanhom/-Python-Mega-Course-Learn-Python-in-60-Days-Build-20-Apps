def temp_checker(temp):
    if temp > 7:
        return("Warm")
    elif temp <= 7:
        return("Cold")

print(temp_checker(9))