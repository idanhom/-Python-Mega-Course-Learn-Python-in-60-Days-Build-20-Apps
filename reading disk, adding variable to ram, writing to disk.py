# https://chatgpt.com/g/g-68224f68f00481919450c37b53dfa936-python-teacher/c/682dc43f-62fc-800b-bcb1-dfc5526e3978
# https://redeploy.udemy.com/course/the-python-mega-course/learn/lecture/38005862#notes

# 1. First, we need to read the list from HDD into RAM.
# also close the file after having read it.
file = open('members.txt', 'r')
names = file.readlines()
file.close()

# 2. Then we need to prompt new input, which is first stored into ram (variable)
new_name = input("Enter new name: ")

# 3. Then we need to append new input into list variable of already existing names)
names.append(new_name + '\n')


# 4. Then we need to write variable into disk again.
file = open('members.txt', 'w')
file.writelines(names)
file.close()
