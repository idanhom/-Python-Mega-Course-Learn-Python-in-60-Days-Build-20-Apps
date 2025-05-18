todos = []

while True:

    user_input = input("Enter selection (add, show, edit, exit): ")
    user_input = user_input.strip()

        
    match user_input:
        case "add":
            add_to_list = input("Enter item to list: ")
            todos.append(add_to_list.capitalize())

        case "show" | "display":
            for idx, item in enumerate(todos, start = 1):
                print(f"{idx}: {item}")
        
        case "edit":
            index_to_change = int(input("Enter index to change: "))
            index_to_change = index_to_change - 1
            new_item = input("Enter new item: ")
            todos[index_to_change] = new_item.capitalize()
            print(f"New item: {todos[index_to_change]}")
            #here, again, return functionality
            #to input idx to change
            #then replace that index with new input


        case "exit":
            break
        case _:
            print("wrong input.")

print("Bye!")
