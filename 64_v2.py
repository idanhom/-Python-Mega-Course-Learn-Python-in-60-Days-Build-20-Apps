file = open('members.txt', 'r')
names = file.readlines()


new_member = input("Enter new name: ")



names.append(new_member + '\n')

file.close()

file.write(names, 'w')


