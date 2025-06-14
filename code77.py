
def get_nr_items(user_input):
    split_words = user_input.split(",")
    output = len(split_words)
    return output


print(get_nr_items("john, lisa, teresa"))



