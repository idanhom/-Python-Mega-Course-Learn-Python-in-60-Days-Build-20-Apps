countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for countries, filenames in zip(countries, filenames):
    file = open(filenames, 'w')
    file.write(countries)
    file.close()

