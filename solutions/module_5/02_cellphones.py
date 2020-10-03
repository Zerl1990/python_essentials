my_dict = {}

total = int(input('Total numbers:'))

for index in range(total):
    name = input(f'{index}: Name:')
    num = input(f'{index}: Cellphone:')
    my_dict[name] = num

print(my_dict)

