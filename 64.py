

while True:

    file = open('members.txt', 'r')
    existing_members = file.readlines()
    
    user_input = input("Decide if you want to enter name or exit program: ")
    match user_input:
        case 'enter':
            new_name = input("Enter name: ")
            

            file = open('members.txt', 'w')
            file.writelines(new_name)
            existing_members.append(file)
            file.close()

        case 'exit':
            print("Bye!")
            break        
