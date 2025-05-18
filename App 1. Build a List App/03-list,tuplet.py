""" filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt"]

for filename in filenames:
    print(filename)
    filename = filename.replace(".", "-", 1)
    
    print(f"new: {filename}")

 """
 

# seconds = [1.23, 1.45, 1.02]
# current = 1.11

# seconds.append(current)

# elements = ['a', 'b', 'c']
# print(elements[1])

# elements = ['a', 'b', 'c']
# elements[1] = "x"
# print(elements)

# elements = ['a', 'b', 'c']
# new = 'x'
# new = elements[1]
# print(elements)

# rainfall = [
#     3.14,
#     3,
#     "item1",
#     []
#     ]
    
# print(type(rainfall[0]))

# products = ['table', 'chair', 'door']

# for product in products:
#     print(f"Product: {product}")

# filenames = ['document', 'report', 'presentation']

# for idx, filename in enumerate(filenames):
#     print(f"{idx}-{filename.capitalize()}.txt")

# help(list.pop)

print(dir(list))

help(list.pop)