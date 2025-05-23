filenames = ["a.jpg", "b.jpg", "c.jpg"]

filenames = ['renamed_' + filename.replace('.jpg', '.png') for filename in filenames]


print(filenames)