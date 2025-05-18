todos = []

while True:

    user_input = input("Enter selection (add, show, edit, exit): ")
    user_input = user_input.strip()

        
    match user_input:
        case "add":
            add_to_list = input("Enter item to list: ")
            todos.append(add_to_list.capitalize())

        case "show" | "display":
            for item in todos:
                print(item)
        
        case "edit":
                for index, item in enumerate(todos):
                    row = f"{index} - {item}"
                    print(row)



        case "exit":
            break
        case _:
            print("wrong input.")

print("Bye!")
