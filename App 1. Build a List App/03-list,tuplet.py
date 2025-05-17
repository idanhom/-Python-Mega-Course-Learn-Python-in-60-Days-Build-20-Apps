""" filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt"]

for filename in filenames:
    print(filename)
    filename = filename.replace(".", "-", 1)
    
    print(f"new: {filename}")

 """
 

seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)