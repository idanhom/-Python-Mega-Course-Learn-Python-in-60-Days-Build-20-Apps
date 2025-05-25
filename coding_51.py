languages = ['English', 'German', 'Spanish']


for language in languages:
    with open(f"{language}.txt", 'w') as file:
        file.writelines(f"{language}")

