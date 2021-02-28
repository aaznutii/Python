import random

test_list = []
new_list = [el for el in range(1, 21)]


def get_choice(list):
    result = None if list == [] else random.choice(list)
    return result
