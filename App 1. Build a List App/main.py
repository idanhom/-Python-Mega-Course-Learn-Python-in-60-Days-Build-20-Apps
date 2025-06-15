def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_list, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)




while True:

    user_input = input("Enter selection (add, show, edit, remove, exit): ")
    user_input = user_input.strip()


    if user_input.startswith("add"):
        todo = user_input[4:]

        todos = get_todos()
        
        todos.append(todo + '\n')
        write_todos(todos)

        

    elif user_input.startswith("show") or user_input.startswith("display") or user_input.startswith("ls"):
        todos = get_todos()


        for idx, item in enumerate(todos):
            row = f"{idx + 1}: {item.strip('\n')}"
            print(row)




    elif user_input.startswith("edit"):
        try:
            index_to_change = int(user_input[5:]) - 1 # Slices to number after 'edit' inc. space after. Then subtract 1 since Python does 0-indexing

            todos = get_todos()
            
            new_item = input("Enter new item: ")
            todos[index_to_change] = new_item.strip() + '\n'

            write_todos(todos)

            print(f"New item: {todos[index_to_change].strip()}")
        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_input.startswith("remove"):
        try:
                
            todos = get_todos()


            index_to_remove = int(user_input[7:]) - 1
            removed_item = todos.pop(index_to_remove)

            write_todos(todos)

            print(f"Removed: {removed_item.strip()}")

        except IndexError:
            print("No item with that number.")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Command is not valid.")


print("Bye!")
