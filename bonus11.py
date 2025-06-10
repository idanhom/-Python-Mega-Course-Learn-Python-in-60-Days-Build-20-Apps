def get_average():
    with open('data.txt', 'r') as file_local:
        data_local = file_local.readlines()
        data = data_local[1:]
    return data_local

print(get_average())