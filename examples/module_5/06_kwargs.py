def my_method(my_list, **kwargs):
    left_padding = kwargs.get('left_padding', 0)
    right_padding = kwargs.get('right_padding', 0)
    delimiter = kwargs.get('delimiter', ',')
    tmp = [item.ljust(left_padding).rjust(right_padding) for item in my_list]
    return delimiter.join(tmp)


names = ['name1', 'name2', 'name3']


print(my_method(names, left_padding=10))
print(my_method(names, left_padding=10, right_padding=25))
print(my_method(names, delimiter='##'))


