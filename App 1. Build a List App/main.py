# note: currently haven't implemented the full feature of index slicing 
# (for edit and remove)



while True:

    user_input = input("Enter selection (add, show, edit, remove, exit): ")
    user_input = user_input.strip()


    if 'add' in user_input:
        #todo = input("Enter item to add: ")

        todo = user_input[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)


            




        
    # match user_input:
    #     case "add":
    #         todo = input("Enter item to list: ")

    #         with open('todos.txt', 'r') as file:
    #             todos = file.readlines()

    #         todos.append(todo + '\n')

    #         with open('todos.txt', 'w') as file:
    #             file.writelines(todos)



    elif "show" in user_input or "display" in user_input:

        # this code is wrong, 
        with open('todos.txt', 'r') as file:
            todos = file.readlines()


        for idx, item in enumerate(todos):
            print(f"{idx + 1}: {item.strip()}")





    elif "edit" in user_input:

        index_to_change = int(user_input[5:]) - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        
        new_item = input("Enter new item: ")
        todos[index_to_change] = new_item.strip() + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"New item: {todos[index_to_change].strip()}")





    elif "remove" in user_input:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index_to_remove = int(user_input[7:]) - 1

        # index_to_remove = int(input("Select item to remove: ")) - 1
        removed_item = todos.pop(index_to_remove)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"Removed: {removed_item.strip()}")

    elif "exit" in user_input:
        break

    # if _ in user_input:
    #     print("wrong input.")


    else:
        print("Command is not valid.")


print("Bye!")
