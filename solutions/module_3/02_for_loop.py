print('*' * 80)
print('1) Even numbers from 0 to 100')
for num in range(0, 101, 2):
    print(num)


print('*' * 80)
num = int(input('2) Please provide a number between 0 a 100: '))
for index in range(0, 11):
    print(f'{num} * {index} = {num * index}')


print('*' * 80)
print("3) Print Pattern")
for num in range(2, 9, 2):
    print(f"PATTERN: {'*' * num}")


