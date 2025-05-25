with open("file.txt", 'r') as file:
    print(file.read())
    file.seek(0)
    print(len(file.read()))