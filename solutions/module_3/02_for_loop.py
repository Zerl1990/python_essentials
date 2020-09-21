num = int(input('Please provide a number between 0 a 100: '))

for index in range(1, 11):
    print(f'{num} * {index} = {num * index}')


for num in range(0, 10, 2):
    print(num * '*')
