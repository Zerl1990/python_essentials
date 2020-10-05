def multiple(num_a, num_b):
    if type(num_a) != int or type(num_b) != num_b:
        raise ValueError
    return num_a * num_b


def sum_lst(lst, start, end):
    if not lst:
        return ValueError(f'Invalid value for lst')
    if start < 0:
        return IndexError(f'Start index {start} out of range')
    if end >= len(lst):
        return IndexError(f'End index {end} out of range')
    return sum(lst[start:end:])


multiple(5, 'adc')
multiple('dada', 5)
sum_lst(None, 0, 15)
sum_lst([1, 2], -1, 1)
sum_lst([1, 2, 3], 0, 9)

