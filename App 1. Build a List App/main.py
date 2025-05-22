while True:

    user_input = input("Enter selection (add, show, edit, remove, exit): ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter item to list: ") + "\n"

            file = open('todos.txt', 'w')
            todos = file.readlines()
            file.close()

            todos.append(todo.capitalize())
            
            file = open('todos.txt', 'w')
            file.writelines(todos)

        case "show" | "display":
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for idx, item in enumerate(todos):
                print(f"{idx + 1}: {item}")
        
        case "edit":
            index_to_change = int(input("Enter index to change: "))
            index_to_change = index_to_change - 1
            new_item = input("Enter new item: ")
            todos[index_to_change] = new_item.capitalize()
            print(f"New item: {todos[index_to_change]}")

        case "remove":
            # select which index to remove
            index_to_remove = int(input("Select item to remove: "))
            # remove 1 from it (because of zero-indexing)
            # index_to_remove = index_to_remove - 1
            print(f"Removed: {todos.pop(index_to_remove - 1)}")


        case "exit":
            break
        case _:
            print("wrong input.")

print("Bye!")
