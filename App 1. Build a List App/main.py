while True:

    user_input = input("Enter selection (add, show, edit, remove, exit): ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter item to list: ")

            file = open('todos.txt', 'a')
            file.write(todo + '\n')
            file.close()

        case "show" | "display":
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            

            # new_todos = [item.strip('\n') for item in todos]

            for idx, item in enumerate(todos):
                # item = item.strip('\n')
                print(f"{idx + 1}: {item.strip('\n')}")
        




        case "edit":
            index_to_change = int(input("Enter index to change: "))
            index_to_change = index_to_change - 1
            new_item = input("Enter new item: ")
            todos[index_to_change] = new_item.capitalize()
            print(f"New item: {todos[index_to_change]}")

        case "remove":
            index_to_remove = int(input("Select item to remove: "))
            print(f"Removed: {todos.pop(index_to_remove - 1)}")


        case "exit":
            break
        case _:
            print("wrong input.")

print("Bye!")
