# https://chatgpt.com/g/g-68224f68f00481919450c37b53dfa936-python-teacher/c/682dc43f-62fc-800b-bcb1-dfc5526e3978
# https://redeploy.udemy.com/course/the-python-mega-course/learn/lecture/38005862#notes

file = open('members.txt', 'r')
names = file.readlines()


new_member = input("Enter new name: ")



names.append(new_member + '\n')

file.close()

file.write(names, 'w')


