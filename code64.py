filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

for filename in filenames:
    filename_no_exension = filename[:-4]
    print(filename_no_exension)
    
# v 2
for filename in filenames:
    filename_no_exension_2 = filename.removesuffix('.txt')
    print('\n' + filename_no_exension_2)