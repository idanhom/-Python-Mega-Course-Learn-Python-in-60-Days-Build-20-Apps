""" ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
 
for id in ids:
    if '_' in id:
        x = x + 1
print(x) """

# Program should print out "OK" 
# when the perimeter is less than 14 and the area is less than 8. 

length = float(input("Enter length: "))
width = float(input("Enter width: "))
 
perimeter = (length + width) * 2
area = length * width
 
print("Perimeter is", perimeter)
print("Area is", area)
 
if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")