# todos = []

# while True:
#     todo = input("Enter list: ")
#     todos.append(todo)
#     print(todos)

# todo = input("Enter a to-do: ")
# print(todo.capitalize())

# lists = []

# while True:
#     list = input("Enter item: ")
#     list = list.capitalize()
#     lists.append(list)
#     print(lists)


# user should input password
# to be stored in variable 'password'
# if 'password' != "p123"
# print(f"your password is {password}")

# password = input("Enter password: ")
# while password != "p123":
#     password = input("Enter password: ")
# print("password is correct")

# x = 1
# while x <= 6:
#     print(x)
#     x = x + 1

# name = input("Enter name: ")
# while True:
#     print(name)

# while True:
#     name = input("Enter name: ")
#     print(name.capitalize())

# while True:
#     print("Hello")  

# greeting = "hello"
# print(greeting.upper())

# countries = []
 
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)    

# print(dir(str))
# help(str.capitalize)

#
# a = [1, 2, 3]
# # dir(a)
# a.append(4)
# print(a)
# help(list.append)

# print(dir(str))

#help(str.capitalize)

# import builtins
# print(dir(builtins))

# print(help(list.count))

todos = []

while True:

    user_input = input("Enter selection: ")
    user_input = user_input.strip()
        
    match user_input:
        case "add":
            add_to_list = input("Enter item to list: ")
            todos.append(add_to_list)
            for item in todos:
                print(item)
            # print(todos)

        case "show" | "display":
            # print(todos)
            for item in todos:
                print(item.capitalize())

        case "spell":
            for char in todos[0]:
                print(char.upper())


        case "exit":
            break
        
        case _:
            print("wrong input.")
        