my_list = [25, 12, 14, 22, 19, 15, 10, 10, 23]
target = 55


# First solution, complexity N^2
size = len(my_list)
for start in range(0, size):
    total = 0
    for index in range(start, size):
        total += my_list[index]
        if total == target:
            print(f'Found: Start={start}, End={index}')
            break
        elif total > target:
            break


# Second solution, complexity N
total = 0
low_index = 0
for index, value in enumerate(my_list):
    total += value
    if total > target:
        total -= my_list[low_index]
        low_index += 1
    if total == target:
        print(f'Found: Start={low_index}, End={index}')
        break
