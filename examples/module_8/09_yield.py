def custom_range(start, end):
    index = start
    while index < end:
        yield index
        index += 1


for num in custom_range(0, 10):
    print(num)


print(sum(custom_range(3, 10)))

