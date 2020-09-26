numbers = [1, 2, 3, 4, 5]

print(f'Len: {len(numbers)}')

print(f'Number at index 0: {numbers[0]}')
print(f'Number at index 1: {numbers[0]}')
print(f'Number at index 2: {numbers[0]}')
print(f'Number at index 3: {numbers[0]}')
print(f'Number at index 4: {numbers[0]}')

numbers[0] = 5
print(f'New value for index 0: {numbers[0]}')


print(f'Len: {len(numbers)}')
del numbers[0]
print(f'Len: {len(numbers)}')




