import random


def random_list(size, start=0, end=100):
    lst = []
    for item in range(size):
        lst.append(random.randint(start, end))
    return lst


random_list(1000, end=50)


def get_min_max_values(lst):
    min_number = None
    max_number = None
    for item in lst:
        if not min_number or item < min_number:
            min_number = item
        if not max_number or item > max_number:
            max_number = item
    return min_number, max_number


lst = random_list(10, 0, 10)  # Full positional

lst = random_list(size=10, start=0, end=10)  # Keyword

lst = random_list(10, start=0, end=10)  # Mix

min_val, max_val = get_min_max_values(lst)

print(min_val)
print(max_val)
