def format_filename():
    filename = 'report.txt'
    filename_sliced = filename[:6].capitalize()
    return filename_sliced

print(format_filename())