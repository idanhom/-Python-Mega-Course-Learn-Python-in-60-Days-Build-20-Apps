

while True:
    
    user_input = input("Decide if you want to enter name or exit program: ")
    match user_input:
        case 'add':
            new_name = input("Enter name: ")
            

            file = open('members.txt', 'a')
            file.write(new_name + '\n')
            file.close()

        case 'show':
            file = open('members.txt', 'r')
            names = file.read()

            print(names)

            file.close()
                


        case 'exit':
            print("Bye!")
            break        
