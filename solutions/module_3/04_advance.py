import random


def random_list():
    rnd_list = []
    for num in range(0, 1000):
        rnd_list.append(random.randint(0, 1000))
    return rnd_list


numbers = random_list()

target = int(input('Number: '))

# 1. count(target)
print(f'Count: {numbers.count(target)}')

# 2. imprimir en orden inverso de 2 en 2
print(numbers[::-2])

# 3. numbers.extend(my_list)
print(len(numbers))
my_list = [123, 123, 34, 23]
numbers.extend(my_list)
print(len(numbers))


# 4. Num min, max, sum
#   min(numbers)
#   max(numberS)
#   sum(numbers)
print(f'min: {min(numbers)}')
print(f'max: {max(numbers)}')
print(f'sum: {sum(numbers)}')

