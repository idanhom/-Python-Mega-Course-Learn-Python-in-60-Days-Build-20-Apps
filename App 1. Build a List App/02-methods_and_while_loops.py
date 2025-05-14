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

    user_input = input("Enter selection (add, show, edit, exit): ")
    user_input = user_input.strip()
        
    match user_input:
        case "add":
            add_to_list = input("Enter item to list: ")
            todos.append(add_to_list)
        case "show" | "display":
            for item in todos:
                print(item.capitalize())
        
        case "edit":
            # print "what index to change?"
            # loop and print index of each item  
            
            for idx, item in enumerate(todos):
                number = input("Select index to change")
                print(idx, item)
            # ask user to select
            #     note: python indexes from 0
            #     number = number - 1
            # replace item[number] = new_value
            number = int(number) - 1



        case "exit":
            break
        case _:
            print("wrong input.")

print("Bye!")

# buttons = ["cancel", "reply", "submit"]

# for i in buttons:
#     print(i.capitalize())

# buttons = ["cancel", "reply", "submit"]
 
# for i in buttons:
#     print(i.capitalize())

# for item in ["sandals", "glasses", "trousers"]:
#     print(item.capitalize())
 