def parse(feet_inches_str):
    feet, inches = feet_inches_str.split(" ")
    return float(feet), float(inches)

def convert(feet, inches):
    return feet * 0.3048 + inches * 0.0254

user_input = input("Enter feet and inches: ")

f, i = parse(user_input)
meters = convert(f, i)
if meters < 1:
    print("Kid is too small")
else:
    print("Kid can ride")