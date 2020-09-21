import random


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


def add_rnd_to_list(lst, size=200, start=0, end=100):
    for num in range(size):
        lst.append(random.randint(start, end))
    return len(lst)


my_list = [1, 2, 3]
print(f'Original Size: {len(my_list)}')
print(f'Original list: {my_list}')

new_size = add_rnd_to_list(my_list)
print(f'New list size: {new_size}')
print(f'Modified list: {my_list}')


def default_list(lst=[], size=200, start=0, end=100):
    for num in range(size):
        lst.append(random.randint(start, end))
    return len(lst)


print(default_list())  # Size 200
print(default_list())  # Size 400
print(default_list())  # Size 600
print(default_list())  # Size 800

