import random


def random_list(size: int, start: int, end: int) -> list:
    lst = []
    for item in range(size):
        lst.append(random.randint(start, end))
    return lst


random_list(1000, end=50)

