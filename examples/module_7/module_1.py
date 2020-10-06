print(f'Hi from: {__name__}')

counter = 0


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


def prod_list(lst):
    total = 0
    for num in lst:
        total *= num
    return total
