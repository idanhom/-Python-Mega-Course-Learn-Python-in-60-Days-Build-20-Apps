try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = (value/total_value) * 100
    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number.\nRun the program again")