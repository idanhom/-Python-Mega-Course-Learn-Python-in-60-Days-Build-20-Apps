# https://redeploy.udemy.com/course/the-python-mega-course/learn/lecture/38005988#notes


files = ['a.txt', 'b.txt', 'c.txt']

for file in files:
    file = open(file, 'r')
    content = file.readlines()
    print(content[0])
    
