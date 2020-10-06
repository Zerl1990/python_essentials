import random

print(f'Hi from: {__name__}')

counter = 0


def random_list(size, start, end):
    lst = []
    for index in range(size):
        lst.append(random.randint(start, end))
    return lst

