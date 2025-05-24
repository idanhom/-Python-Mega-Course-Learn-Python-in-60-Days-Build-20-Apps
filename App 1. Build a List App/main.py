while True:

    user_input = input("Enter selection (add, show, edit, remove, exit): ")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter item to list: ")

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)



        case "show" | "display":

            # this code is wrong, 
            with open('todos.txt', 'r') as file:
                todos = file.readlines()


            for idx, item in enumerate(todos):
                print(f"{idx + 1}: {item.strip()}")





        case "edit":

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            index_to_change = int(input("Enter index to change: ")) - 1
            new_item = input("Enter new item: ")
            todos[index_to_change] = new_item.strip() + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"New item: {todos[index_to_change].strip()}")





        case "remove":
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            index_to_remove = int(input("Select item to remove: ")) - 1
            removed_item = todos.pop(index_to_remove)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

            print(f"Removed: {removed_item.strip()}")

        case "exit":
            break

        case _:
            print("wrong input.")

print("Bye!")
